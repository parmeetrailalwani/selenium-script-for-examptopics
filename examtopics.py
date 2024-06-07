import os
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta , date
import sys , json,glob, csv
from selenium.webdriver.common.keys import Keys
# from PIL import Image
# from Screenshot import Screenshot_clipping
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc


options = uc.ChromeOptions()
# options.add_argument("--incognito")
# options.add_argument(f'--user-data-dir={CHROME_PROFILE_PATH}')

options.add_argument('--disable-notifications')  # Disable notifications
options.add_argument('--disable-popup-blocking')  # Disable popup blocking
# options.add_argument('--headless')  # Run in headless mode (optional)
options.add_experimental_option('prefs', {
    # 'download.default_directory': DOWNLOAD_FOLDER,  # Specify download folder
    'download.prompt_for_download': False,  # Disable prompt for download
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})
driver = uc.Chrome(options = options)

for i in range(1,40):
    
    driver.get("https:\\www.google.com")
    driver.maximize_window()

    search_bar = driver.find_element(By.CLASS_NAME,'gLFyf')
    search_bar.send_keys(f'examptopics ai-102 topic 1 q {i}')
    search_bar.send_keys(Keys.ENTER)
    try:
        link1 = driver.find_element(By.CLASS_NAME,'LC20lb')
        link1.click()

        driver.execute_script("window.scrollTo(0, 350)")
        ss_name = f'screenshots\\T1_Q{i}_aques.png'
        # global i 
        driver.save_screenshot(ss_name)
        # btn btn-primary reveal-solution
        reveal_solution = driver.find_element(By.CLASS_NAME,'reveal-solution')
        reveal_solution.click()
        # search_bar.send_keys(Keys)

        driver.save_screenshot(f'screenshots\\T1_Q{i}_bans.png')

        # btn btn-link btn-sm comment-submit-button
        driver.execute_script("window.scrollTo(0, 1200)")

        driver.save_screenshot(f'screenshots\\T1_Q{i}_discussion.png')

    except:
        print('Not found')

