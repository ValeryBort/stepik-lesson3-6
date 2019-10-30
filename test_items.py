link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_contains_add_to_basket_button(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    find_button = browser.find_elements_by_css_selector("#add_to_basket_form  .btn")
    assert find_button, "Can't find button."

