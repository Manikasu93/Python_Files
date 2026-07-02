import pytest

from pages.blog import blog

@pytest.mark.smoke
def test_blog_click_elements(page):
    b1=blog(page)
    b1.click_elements()
