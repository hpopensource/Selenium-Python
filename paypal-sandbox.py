from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

##binary = FirefoxBinary('geckodriver.exe')
driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
#browser = webdriver.Firefox(firefox_binary=binary)
#driver = webdriver.Firefox(firefox_binary=binary)
##driver = webdriver.Firefox(firefox_binary=binary)
user = "xxxx"
pwd = "tttt"
#driver = webdriver.Firefox()
driver.get("https://www.sandbox.paypal.com/us/signin")
assert "Log in to your PayPal account" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()