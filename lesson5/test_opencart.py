import pytest

from lesson5.models.page_objects.page_objects import MainPage


@pytest.fixture(scope="session")
def open_main_page(driver, request):
    url = "opencart/"
    # return driver.get("".join([request.config.getoption("--address"), url]))
    return request.config.getoption("--address")


@pytest.fixture(scope="module")
def main_page(driver):
    return MainPage(driver)


class TestMainPage:

    def test_mainpage(self, main_page, open_main_page):
        main_page.driver.get(open_main_page)
        title = main_page.get_dashboard()
        assert title == "Please enter your login details."
