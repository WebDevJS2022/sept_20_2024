from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.close()


def test_click_button(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    click_button = browser.find_element(By.ID, 'submit-id-submit')
    click_button.click()
    wait = WebDriverWait(browser, 5)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="result"]')
        ))
    button = browser.find_element(By.CSS_SELECTOR, 'div[class="result"]')
    assert button.text == 'Submitted'
