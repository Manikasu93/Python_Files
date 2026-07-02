import pytest

from pages.technology import technology

@pytest.mark.smoke
def test_technology_hover(page):
    t1=technology(page)
    t1.mouse_hover()

@pytest.mark.smoke
def test_technology_ecommerce(page):
    t2=technology(page)
    t2.click_on_ecommerce() 

@pytest.mark.smoke
def test_technology_mobile(page):
    t3=technology(page)
    t3.click_on_mobile()