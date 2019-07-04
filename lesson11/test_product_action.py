import os

import pytest

from lesson11.models.page_objects.page_objects import AdminPage, DashboardPage

PRODUCT = [{"ProductName": "TestName", "MetaTag": "TestMeta", "ProductModel": "TestModel"}]


@pytest.fixture()
def admin_address(request):
    return request.config.getoption("address") + "/admin"


@pytest.fixture()
def admin_data(request):
    return request.config.getoption("login"), request.config.getoption("password")


@pytest.fixture(params=PRODUCT)
def product(request):
    return request.param


@pytest.fixture()
def delay(request):
    return float(request.config.getoption("delay"))


@pytest.fixture()
def dashboard_page(driver, admin_address, admin_data):
    page = AdminPage(driver)
    page.driver.get(admin_address)
    page.login(admin_data[0], admin_data[1])
    # catalog = page.get_catalog()
    # catalog.click()
    # products = page.get_subselection(catalog, "Products")
    # products.click()
    return DashboardPage(page.driver)


class TestProductPage:

    def test_add_product_with_pictures(self, dashboard_page, delay):
        dashboard_page.click_add_menu()
        dashboard_page.click_menu_item("Товар", delay)
        dashboard_page.set_product_name("TestName")
        nav_bar = dashboard_page.get_nav_bar()
        dashboard_page.open_nav_bar_element(nav_bar, "Данные")
        dashboard_page.set_product_code("001")
        dashboard_page.open_nav_bar_element(nav_bar, "Изображения")
        dashboard_page.click_add_image_btn()
        dirname = os.path.dirname(__file__)
        dashboard_page.set_product_image(1, dirname + "1.jpg")
        dashboard_page.click_add_image_btn()
        dashboard_page.set_product_image(2, dirname + "2.jpg")
        dashboard_page.click_add_image_btn()
        dashboard_page.set_product_image(3, dirname + "3.jpg")
        dashboard_page.click_save_btn()
        dashboard_page.click_btn_menu()
        catalog = dashboard_page.get_catalog_menu()
        dashboard_page.click_catalog_item(catalog, "Товары")
        product = dashboard_page.get_product("TestName", delay)
        assert product is not False
