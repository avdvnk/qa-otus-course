import pytest

from lesson5.models.page_objects.page_objects import MainPage


@pytest.fixture(scope="module")
def main_page(driver):
    return MainPage(driver)


class TestMainPage:

    def test_mainpage(self, main_page, request):
        main_page.driver.get(request.config.getoption("--address"))
        title = main_page.get_dashboard()
        assert title == "Your Store"
