import pytest

from lesson9.models.page_objects.page_objects import AdminPage, ProductPage

PRODUCT = [{"ProductName": "TestName", "MetaTag": "TestMeta", "ProductModel": "TestModel"}]
NEW_MODEL = ["NewTestModel"]


@pytest.fixture()
def admin_address(request):
    return request.config.getoption("address") + "opencart/admin"


@pytest.fixture()
def admin_data(request):
    return request.config.getoption("login"), request.config.getoption("password")


@pytest.fixture(params=PRODUCT)
def product(request):
    return request.param


@pytest.fixture(params=NEW_MODEL)
def new_model(request):
    return request.param

@pytest.fixture()
def delay(request):
    return float(request.config.getoption("delay"))


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

    def test_add_product(self, product_page, product, delay):
        product_page.add_product(product.get("ProductName"), product.get("MetaTag"), product.get("ProductModel"))
        assert product_page.get_product(product.get("ProductName"), delay)

    def test_set_product_model(self, product_page, product, new_model, delay):
        product_element = product_page.get_product(product.get("ProductName"), delay)
        product_page.edit_product_model(product_element, new_model)
        product_element = product_page.get_product(product.get("ProductName"), delay)
        assert product_page._get_product_model(product_element) == new_model

    def test_remove_product(self, product_page, product, delay):
        product_element = product_page.get_product(product.get("ProductName"), delay)
        product_page.remove_product(product_element, delay)
        product_element = product_page.get_product(product.get("ProductName"), delay)
        assert product_element is False

    def test_wait_dropdown_toggle(self, product_page, delay):
        headers = product_page.open_dropdown_toggle(delay)
        assert len(headers) == 2
