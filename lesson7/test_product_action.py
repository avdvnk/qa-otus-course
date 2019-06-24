import pytest

from lesson7.models.page_objects.page_objects import AdminPage, ProductPage


@pytest.fixture()
def admin_address(request):
    return request.config.getoption("address") + "opencart/admin"


@pytest.fixture()
def admin_data(request):
    return request.config.getoption("login"), request.config.getoption("password")


@pytest.fixture()
def product_page(driver, admin_address, admin_data):
    page = AdminPage(driver)
    page.driver.get(admin_address)
    page.login(admin_data[0], admin_data[1])
    catalog = page.get_catalog()
    catalog.click()
    products = page.get_subselection(catalog, "Products")
    products.click()
    return ProductPage(page.driver)


class TestProductPage:

    def test_add_product(self, product_page):
        product_page.click_add_btn()
        product_page.set_product_name("Test")
        product_page.set_meta_tag("Meta")
        product_page.open_tab("Data")
        product_page.set_model("Model")
        product_page.click_save()
        assert product_page.get_product("Test")
