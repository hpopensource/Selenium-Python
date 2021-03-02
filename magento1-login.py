from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

driver = webdriver.Firefox(executable_path=r'C:\Users\hparmar.HQ\Downloads\geckodriver.exe')

user = "xxx"
pwd = "xxxx"

driver.get("http://localhost/m1")
assert "Log into Magento Admin Page" in driver.title
elem = driver.find_element_by_id("username")
elem.send_keys(user)
elem = driver.find_element_by_id("login")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)