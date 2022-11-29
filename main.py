import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# open the site and block pop-ups

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-notifications')
driver = webdriver.Chrome(options=chrome_options)
url = 'http://facebook.com'

driver.get(url)

# log in to the site
# on facebook, username = 'email', password = 'pass'

username = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

# login button is type 'submit'
# enter username and password

username.clear()
username.send_keys("joemudah@woodycooks.com")
password.clear()
password.send_keys("CEN3031!")
time.sleep(2)
# click the log in button
button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# once we are logged in, now go to our target events site to scrape:

url2 = 'https://www.facebook.com/indivisiblegainesville/events/?ref=page_internal/'
time.sleep(2)
driver.get(url2)

# now grab events data
# first i need to click see more at the bottom of the page a few times.
time.sleep(2)
# scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)


# need to click the "see more" button at the bottom


# driver.find_element(By.XPATH, '//button[normalize-space()="See more"]').click()

# button2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
# '//*[@id="mount_0_0_18"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div/div[3]/div/div/div/div[5]'


