import pytest

from pages.vertical import vertical

@pytest.mark.smoke
def test_vertical_hover(page):
    v1=vertical(page)
    v1.mouse_hover()

@pytest.mark.smoke
def test_vertical_trading(page):
    v1=vertical(page)
    v1.trading()

@pytest.mark.smoke
def test_vertical_retail(page): 
    v1=vertical(page)
    v1.retail()
 
@pytest.mark.smoke
def test_vertical_healthcare(page):
    v1=vertical(page)
    v1.healthcare()     

@pytest.mark.smoke
def test_vertical_fintech(page):
    v1=vertical(page)
    v1.fintech()    

@pytest.mark.smoke
def test_vertical_custom_app(page):
    v1=vertical(page)
    v1.custom_app()     


