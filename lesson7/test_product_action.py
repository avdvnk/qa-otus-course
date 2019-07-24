import pytest

from lesson7.models.page_objects.page_objects import AdminPage, ProductPage

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

    def test_add_product(self, product_page, product):
        product_page._click_add_btn()
        product_page._set_product_name(product.get("ProductName"))
        product_page._set_meta_tag(product.get("MetaTag"))
        product_page._open_tab("Data")
        product_page._set_model(product.get("ProductModel"))
        product_page._click_save_btn()
        assert product_page.get_product(product.get("ProductName"))

    def test_set_product_model(self, product_page, product, new_model):
        product_element = product_page.get_product(product.get("ProductName"))
        product_page._click_edit_btn(product_element)
        product_page._open_tab("Data")
        product_page._set_model(new_model)
        product_page._click_save_btn()
        product_element = product_page.get_product(product.get("ProductName"))
        assert product_page._get_product_model(product_element) == new_model

    def test_remove_product(self, product_page, product):
        product_element = product_page.get_product(product.get("ProductName"))
        product_page._select_product(product_element)
        product_page._click_remove_btn()
        product_page._confirm_remove()
        product_element = product_page.get_product(product.get("ProductName"))
        assert product_element is False
