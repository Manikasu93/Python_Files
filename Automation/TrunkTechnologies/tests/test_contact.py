import pytest

from pages.contact import contact

@pytest.mark.smoke
def test_contact_form(page):
    c1=contact(page)