import shutil
from pathlib import Path

import pytest
import pytest_html
from playwright.sync_api import sync_playwright

from config import url


def _ensure_output_dirs() -> None:
    Path("screenshots").mkdir(exist_ok=True)
    Path("videos").mkdir(exist_ok=True)


@pytest.fixture
def page():
    _ensure_output_dirs()

    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(Path("videos")),
        record_video_size={"width": 1280, "height": 720},
    )
    page = context.new_page()

    page.goto(url)
    page.wait_for_load_state("load")

    yield page

    try:
        context.close()
    except Exception:
        pass
    finally:
        browser.close()
        p.stop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            _ensure_output_dirs()

            screenshot_path = Path("screenshots") / f"{item.name}.png"
            page.screenshot(path=str(screenshot_path))
            extra.append(pytest_html.extras.image(str(screenshot_path)))

            try:
                context = page.context
                context.close()
            except Exception as exc:
                print(f"[Warning] Could not close context before reading video: {exc}")

            try:
                video = getattr(page, "video", None)
                if video:
                    video_path = video.path()
                    if video_path and Path(video_path).exists():
                        video_name = Path("videos") / f"{item.name}.webm"
                        shutil.copy2(video_path, video_name)
                        extra.append(
                            pytest_html.extras.html(
                                f'<video width="320" height="240" controls><source src="{video_name}" type="video/webm"></video>'
                            )
                        )
                    else:
                        print("[Warning] No video was recorded for this failure.")
            except Exception as exc:
                print(f"[Warning] Failed to attach video: {exc}")

        report.extra = extra