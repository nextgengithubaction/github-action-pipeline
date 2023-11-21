from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import sys
import time

firefox_options = Options()
firefox_options.headless = True

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
website = sys.argv[1]
driver.get(website)
pause = int(sys.argv[2])
time.sleep(pause)

print('Current URL = ' + driver.current_url)
print('Title = ' + driver.title)
print('Name = ' + driver.name)

if sys.argv[3] == 'true':
    print('Page Source = ' + driver.page_source)

tag_name = sys.argv[4]
elements = driver.find_elements(By.TAG_NAME, tag_name)
for e in elements:
    print('H1 = ' + e.text)

driver.quit()
