from selenium import webdriver
from selenium.webdriver.common.by import By


def test_first_meme():
    driver = webdriver.Chrome()
    driver.get('https://9gag.com/trending')
    first_meme = driver.find_element(By.XPATH, '//*[@id="jsid-post-a6ZoO6L"]/header/a')
    first_meme_url = first_meme.get_attribute('href')

    with open('meme.txt', 'w') as meme_file:
        meme_file.write(first_meme_url)
