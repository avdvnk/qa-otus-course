import pytest

from lesson12.models.page_objects.page_objects import AdminPage, DashboardPage

PRODUCT = [{"ProductName": "TestName", "MetaTag": "TestMeta", "ProductModel": "TestModel"}]
CATEGORY = ["test 20"]


@pytest.fixture()
def admin_address(request):
    return request.config.getoption("address") + "/admin"


@pytest.fixture()
def admin_data(request):
    return request.config.getoption("login"), request.config.getoption("password")


@pytest.fixture(params=PRODUCT)
def product(request):
    return request.param


@pytest.fixture(params=CATEGORY)
def category(request):
    return request.param


@pytest.fixture()
def delay(request):
    return float(request.config.getoption("delay"))


@pytest.fixture()
def dashboard_page(driver, admin_address, admin_data):
    page = AdminPage(driver)
    page.driver.get(admin_address)
    page.login(admin_data[0], admin_data[1])
    return DashboardPage(page.driver)


class TestProductPage:

    def test_open_product_page(self, dashboard_page, delay):
        dashboard_page.click_btn_menu()
        catalog = dashboard_page.get_catalog_menu()
        catalog.click()
        dashboard_page.click_catalog_item(catalog, "Файлы для скачивания")
        download_file_list = dashboard_page.get_download_file_list()
        assert len(download_file_list) == 1
