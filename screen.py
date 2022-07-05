import os
import random

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

options = Options()
options.headless = True
fp = webdriver.FirefoxProfile()
fp.set_preference('network.proxy.type', 1)
fp.set_preference('network.proxy.socks', '127.0.0.1')
fp.set_preference('network.proxy.socks_port', 9050)
fp.set_preference('network.proxy.socks_remote_dns', True)

driver = webdriver.Firefox(executable_path='path_to_driver',
                           options=options,
                           firefox_profile=fp)

driver.set_page_load_timeout(25)
driver.set_window_size(1080, 1080)

def take_screen(link):
    number = random.randint(1, 1000)
    file_path = 'screenshot_{0}.png'.format(number)
    driver.get(link)
    filename = f"screenshot_{number}.png"
    driver.save_screenshot(filename=filename)
    return file_path


