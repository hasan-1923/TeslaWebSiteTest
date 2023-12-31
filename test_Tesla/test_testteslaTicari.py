# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pathlib import Path
from datetime import date
class TestTestteslaTicari():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.folderPath = str(date.today())
    Path(self.folderPath).mkdir(exist_ok=True)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testteslaTicari(self):
    self.driver.get("https://www.tesla.com/tr_tr")
    self.driver.set_window_size(1552, 832)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#dx-nav-item--energy > .tds-site-nav-item-text")))
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--energy > .tds-site-nav-item-text").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Ticari").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-hero__content-end")))
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-badges__button span")))
    self.driver.save_screenshot(f"{self.folderPath}/test-Ticari.png")
    self.driver.find_element(By.CSS_SELECTOR, ".tcl-badges__button span").click()
  
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "firstName")))
    time.sleep(1)
    self.driver.find_element(By.NAME, "firstName").send_keys("test")
    self.driver.find_element(By.NAME, "lastName").click()
    self.driver.find_element(By.NAME, "lastName").send_keys("test")
    self.driver.find_element(By.NAME, "phone").click()
    self.driver.find_element(By.NAME, "phone").send_keys("111111111111111")
    element = self.driver.find_element(By.NAME, "email")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".tcl-form-layout__item:nth-child(5) .tds-form-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".tcl-form-layout__item:nth-child(5) .tds-form-item").click()
    self.driver.find_element(By.NAME, "email").send_keys("test@hotmail.com")
    self.driver.find_element(By.NAME, "street1").click()
    self.driver.find_element(By.NAME, "street1").send_keys("test")
    self.driver.find_element(By.NAME, "city").click()
    self.driver.find_element(By.NAME, "city").send_keys("test")
    self.driver.find_element(By.NAME, "state").send_keys("test")
    self.driver.find_element(By.NAME, "zip").send_keys("test")
    self.driver.find_element(By.NAME, "companyName").send_keys("test")
    self.driver.find_element(By.NAME, "enterprise").send_keys("test")
    
    
    self.driver.execute_script("window.scrollBy(0,500)","") 
    time.sleep(2)
    self.driver.find_element(By.NAME, "notes").send_keys("test")
    time.sleep(1)
    self.driver.save_screenshot(f"{self.folderPath}/test-TicariFrom.png")
    
    
  
