from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
driver = webdriver.Firefox()

driver.get('http://www.baidu.com')
print driver.title

inputElement = driver.find_element_by_name("q")

inputElement.send_keys("python")
inputElement.submit()

try:
    WebDriverWait(driver,10).until(EC.title_contains("python"))
    print driver.title
finally:
    driver.quit()
#elem = browser.find_element_by_name('p')  # Find the search box
#elem.send_keys('selenium' + Keys.RETURN)

#browser.quit()



