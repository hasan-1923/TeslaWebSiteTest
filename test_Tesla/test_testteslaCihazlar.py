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
class TestTestteslaCihazlar():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.folderPath = str(date.today())
    Path(self.folderPath).mkdir(exist_ok=True)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testteslaCihazlar(self):
    self.driver.get("https://www.tesla.com/tr_tr")
    self.driver.set_window_size(1552, 832)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-homepage-hero__content:nth-child(1)")))
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#dx-nav-item--energy > .tds-site-nav-item-text")))
    self.driver.find_element(By.CSS_SELECTOR, "#dx-nav-item--energy > .tds-site-nav-item-text").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Cihazlar")))
    self.driver.find_element(By.LINK_TEXT, "Cihazlar").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".tcl-hero__heading")))
    self.driver.save_screenshot(f"{self.folderPath}/test-teslacihazlar.png")
    