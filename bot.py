import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Option = Options()
Option.add_argument('--disable-infobars')
Option.add_argument("start-maximized")
Option.add_argument("--disable-extensions")
# Option.add_argument("--headless")
Option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

browser = webdriver.Chrome(chrome_options=Option, executable_path='chromedriver')
browser.implicitly_wait(30)
browser.get('https://www.facebook.com/')

time.sleep(1.5)

email = browser.find_element_by_id('email')
email.clear()
email.send_keys('email here')

password = browser.find_element_by_id('pass')
password.clear()
password.send_keys('password here')

loginButton = browser.find_element_by_id('loginbutton')
loginButton.click()

time.sleep(1.5)

browser.get('https://www.facebook.com/nazeem.shakur/likes')

time.sleep(1.5)

Actions = ActionChains(browser)

while True:
    x = browser.find_element_by_xpath("//*[contains(@class, 'PageLikedButton')]")
    Actions.move_to_element(x).click().perform()
    time.sleep(2)
    Actions.send_keys(Keys.TAB).perform()
    time.sleep(2)
    Actions.send_keys(Keys.RETURN).perform()
    time.sleep(2)
