import sys
import os
dir_path = os.path.dirname(__file__)
executable = os.path.abspath(os.path.join(dir_path, '..', 'bin', 'OSX'))
print executable
sys.path.append(executable)
print os.path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')
# browser = webdriver.Firefox(firefox_binary=binary)


# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()
