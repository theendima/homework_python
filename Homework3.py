import pytest
from selene import browser, be, have

@pytest.fixture(autouse=True)
def setup_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 720
    yield
    browser.quit()

def test_browser():
    browser.open('https://duckduckgo.com/')
    browser.element('#searchbox_input').should(be.blank).type('dnjmgbhndhnvgvjknsujgbUANHBEDfnjBHZJIKUfr;ujikaedftgb').press_enter()
    browser.element('#react-layout').should(have.text('ничего не найдено'))
