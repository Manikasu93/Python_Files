from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright
import pytest_html

from config import url

@pytest.fixture(scope="session")


def page(request):
    
    p = sync_playwright().start()
    browser=p.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()

    page.goto(url)
    page.wait_for_load_state("load")
    
    
    yield page

    context.close()
    browser.close()
    p.stop()


# @pytest.hookimpl(hookwrapper=True)

# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()

#     extra = getattr(report, "extra", [])

#     if report.when == "call" and report.failed:
#         page = item.funcargs.get("page")

#         if page:
#             screenshots_dir = Path("screenshots")
#             screenshots_dir.mkdir(exist_ok=True)

#             file_name = screenshots_dir / f"{item.name}.png"

#             page.screenshot(path=str(file_name))

#             extra.append(pytest_html.extras.image(str(file_name)))

#         report.extra = extra

    # @pytest.hookimpl(hookwrapper=True)

    # def pytest_runtest_makereport(item, call):
    #     outcome = yield
    #     report = outcome.get_result()

    #     extra = getattr(report, "extra", [])

    #     if report.when == "call" and report.failed:
    #         page = item.funcargs.get("page")

    #         if page:
    #             screenshots_dir = Path("screenshots")
    #             screenshots_dir.mkdir(exist_ok=True)

    #             file_name = screenshots_dir / f"{item.name}.png"

    #             page.screenshot(path=str(file_name))

    #             extra.append(pytest_html.extras.image(str(file_name)))

    #             # Retrieve video path and append to report
    #             if page.video:
    #                 extra.append(pytest_html.extras.html(f'<video width="320" height="240" controls><source src="{page.video.path()}"type="video/webm"></video>'))

    #         report.extra = extra



    import shutil
    from pathlib import Path
    import pytest

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        outcome = yield
        report = outcome.get_result()

        extra = getattr(report, "extra", [])

        if report.when == "call" and report.failed:
            page = item.funcargs.get("page")

            if page:
                screenshots_dir = Path("screenshots")
                screenshots_dir.mkdir(exist_ok=True)

                file_name = screenshots_dir / f"{item.name}.png"

                page.screenshot(path=str(file_name))

                extra.append(pytest_html.extras.image(str(file_name)))

            report.extra = extra
            item.call_report = report  # Store reference to report for the teardown phase

        # During teardown, the browser context is closed, so the video file is ready on disk
        if report.when == "teardown" and hasattr(item, "call_report"):
            page = item.funcargs.get("page")
            if page and page.video:
                try:
                    video_path = page.video.path()
                    if Path(video_path).exists():
                        screenshots_dir = Path("screenshots")
                        screenshots_dir.mkdir(exist_ok=True)

                        # Copy the video to the screenshots folder
                        dest_video = screenshots_dir / f"{item.name}.webm"
                        shutil.copy(video_path, dest_video)

                        # Attach the copied video to the call report
                        item.call_report.extra.append(
                            pytest_html.extras.html(
                                f'<video width="320" height="240" controls>'
                                f'  <source src="{dest_video}" type="video/webm">'
                                f'</video>'
                            )
                        )
                except Exception as e:
                    print(f"\n[Warning] Failed to attach video: {e}")