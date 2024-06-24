from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

URL = 'https://www.booking.com/'
PAUSE_TIME = 1
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 10)

driver.get(URL)
try: 
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Dismiss sign in information."]')))
    popup_close = driver.find_element(By.CSS_SELECTOR,value='button[aria-label="Dismiss sign in information."]')
    popup_close.click()
except TimeoutException as ex:
    print("Exception has been thrown. " + str(ex))



dest = driver.find_element(By.CSS_SELECTOR, value='input[name="ss"]')
dest.send_keys('Jaipur', Keys.ENTER)

time.sleep(PAUSE_TIME)
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.b90aaa8bb3[data-testid="searchbox-dates-container"]')))


# date_picker = driver.find_element(By.CSS_SELECTOR, value='div.baca574774')

# date_picker.click()
'#calendar-searchboxdatepicker >  table > tbody > tr > td > span[data-date="2024-06-27"]'

time.sleep(PAUSE_TIME)
try:
    check_in = driver.find_element(By.CSS_SELECTOR, value='div.e8314cc830 > span[data-date="2024-06-27"]')
    check_in.click()

    # time.sleep(PAUSE_TIME)


    check_out = driver.find_element(By.CSS_SELECTOR, value='div.e8314cc830 > span[data-date="2024-07-27"]')
    check_out.click()
except NoSuchElementException as ex:
    print("Exception has been thrown. " + str(ex))

search = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]') 
search.click()

wait.until(EC.element_to_be_clickable, 'h1[aria-live="assertive"]')


last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

    wait.until(EC.element_to_be_clickable, 'span.ad82e69f7d')
    try:
        load = driver.find_element(By.CSS_SELECTOR, value='button.bf33709ee1.a190bb5f27.b9d0a689f2.bb5314095f.b81c794d25.da4da790cd')
        load.click()
    except NoSuchElementException as ex:
        print("Error message: " + str(ex))












