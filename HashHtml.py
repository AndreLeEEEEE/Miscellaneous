from selenium import webdriver
from bs4 import BeautifulSoup
import hashlib

PATH = "chromedriver.exe"  # Put chromedriver.exe into the same directory
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")
driver.implicitly_wait(10)

big_box = driver.find_element_by_class_name("SDkEP")
box = driver.find_element_by_class_name("gLFyf")
#soup = BeautifulSoup(box.get_attribute("outerHTML"), 'html.parser')
#print(soup.prettify())  # Get the html of the webelement
print(big_box.get_attribute('outerHTML')+"\n")
print(box.get_attribute('outerHTML')+"\n")

sha_256 = hashlib.sha256()  # Get the hash ready
sha_256.update(b"box.get_attribute('outerHTML')")
print(sha_256.hexdigest())
sha_256 = hashlib.sha256()  # Get the hash ready
sha_256.update(b"big_box.get_attribute('outerHTML')")
print(sha_256.hexdigest())
