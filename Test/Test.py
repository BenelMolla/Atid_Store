import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Atid_Store.Basic_Test.Locaters import *


def test_store_buy_product():
    driver = webdriver.Chrome()
    driver.get(get_website)
    driver.find_element(By.XPATH, click_On_Store).click()
    time.sleep(2)
    driver.find_element(By.XPATH, click_On_item).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Click_Add_to_cart).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Click_view_cart).click()
    product_name = driver.find_element(By.XPATH, Verify_the_Product).text
    assert "Anchor Bracelet" == product_name
    driver.close()

test_store_buy_product()

def test_men_buy_product():
    driver = webdriver.Chrome()
    driver.get("https://atid.store/")
    driver.find_element(By.XPATH, click_On_Men).click()
    time.sleep(2)
    driver.find_element(By.XPATH, click_On_ATID_Blue_Shoes).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Add_to_cart).click()
    time.sleep(3)
    driver.find_element(By.XPATH, Enter_view_cart).click()
    driver.close()

test_men_buy_product()

def test_Women_buy_product():
    driver = webdriver.Chrome()
    driver.get(Get_Website_Atid)
    driver.find_element(By.XPATH, Click_On_Women).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Click_On_Black_Over_the_shoulder_Handbag).click()
    time.sleep(2)
    driver.find_element(By.XPATH, add_to_Cart).click()
    time.sleep(3)
    driver.find_element(By.XPATH, enter_View_cart).click()
    driver.close()

test_Women_buy_product()

def test_Accessories_buy_product():
    driver = webdriver.Chrome()
    driver.get(Get_website_atid)
    driver.find_element(By.XPATH, click_On_accessories).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Click_on_Boho_Bangle_Bracelet).click()
    time.sleep(2)
    driver.find_element(By.XPATH, add_To_cart).click()
    time.sleep(3)
    driver.find_element(By.XPATH, Click_on_view_cart).click()
    driver.close()

test_Accessories_buy_product()

def test_Store_coupon_product():
    driver = webdriver.Firefox()
    driver.get(GET_WEBSITE)
    driver.find_element(By.XPATH, CLICK_on_Store).click()
    time.sleep(2)
    driver.find_element(By.XPATH, choose_ITEM_from_store).click()
    time.sleep(2)
    driver.find_element(By.XPATH, press_add_to_cart).click()
    time.sleep(2)
    driver.find_element(By.XPATH, press_view_cart).click()
    time.sleep(2)
    coupon_code_store = driver.find_element(By.XPATH, coupon_code)
    time.sleep(3)
    coupon_code_store.send_keys("benel")
    time.sleep(2)
    driver.find_element(By.XPATH, Apply_coupon).click()
    time.sleep(5)
    product_name = driver.find_element(By.XPATH, ensure_the_product).text
    assert 'Coupon "benel" does not exist!' == product_name
    driver.close()


