from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

driver = webdriver.Firefox(executable_path=r'C:\Users\hparmar.HQ\Downloads\geckodriver.exe')

user = "hitesh@weborion.in"
pwd = "Facebookjobs1@#4"

driver.get("http://www.facebook.com")
assert "Facebook - Log In or Sign Up" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
#driver.close()