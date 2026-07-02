import pytest

from pages.portfo import portfo

@pytest.mark.smoke
def test_portfolio_hover(page):
    p1 = portfo(page)
    p1.click_portfolio()