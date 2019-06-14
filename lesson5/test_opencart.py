def test_open_opencart(driver):
    element = driver.find_element_by_xpath()
    assert element.text == "All right"
