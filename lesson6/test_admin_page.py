import pytest

from lesson6.models.page_objects.page_objects import AdminPage


@pytest.fixture()
def admin_address(request, driver):
    return request.config.getoption("address") + "opencart/admin"


@pytest.fixture()
def admin_page(driver, admin_address):
    page = AdminPage(driver)
    page.driver.get(admin_address)
    page.login(username, password)
    return page


class TestAdminPage:

    def test_find_dashboard(self, admin_page):
        dashboard = admin_page.get_dashboard()
        assert dashboard

    def test_find_customers(self, admin_page):
        customers = admin_page.get_customers()
        assert customers

    def test_menu_items(self, admin_page):
        items_count = admin_page.get_menu_count()
        assert items_count == 5

    def test_username(self, admin_page):
        result = admin_page.get_username()
        assert result is False

    def test_get_attributes(self, admin_page):
        attributes = admin_page.get_attributes()
        assert attributes is False

    def test_recent_activity(self, admin_page):
        recent_activity = admin_page.get_recent_activity()
        assert recent_activity is False
