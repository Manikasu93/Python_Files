import pytest

from pages.about import about   

@pytest.mark.smoke

def test_click_social_media_pages(page):
    a1 = about(page)
    a1.click_social_media_pages()