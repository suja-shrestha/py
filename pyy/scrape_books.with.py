from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://books.toscrape.com/")

    for book in driver.find_elements(By.CSS_SELECTOR, "article.product_pod"):
        title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        price = book.find_element(By.XPATH, ".//p[@class='price_color']").text
        print(title, "-", price)