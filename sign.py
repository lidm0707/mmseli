import logging

import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def waitLoad(worker):
    WebDriverWait(worker, 200).until(EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class, 'mm-box') and contains(@class, 'loading-overlay')]")))
    time.sleep(1)
     
def typingCustome(worker,location,string):
    WebDriverWait(worker, 5).until(EC.presence_of_element_located((By.XPATH, location))).send_keys(string)
    
def waitForClickeAble(worker,location = 0):
    waitLoad(worker)
    WebDriverWait(worker, 200).until(EC.element_to_be_clickable((By.XPATH,location))).click()
    time.sleep(1)

    
def importdata():
    with open('.env', 'r') as file:
        data = file.read()
    parsed_json = json.loads(data)
    return parsed_json

def main():
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
    global driver
    logging.info('strad')
    EXTENSION_PATH = 'MMask.crx'
    opt = Options()
    opt.add_argument("--headless=new")
    opt.add_argument('--disable-gpu')
    opt.add_argument("--no-sandbox")
    opt.add_argument('--disable-dev-shm-usage')
    opt.add_argument("--start-maximized")
    opt.add_extension(EXTENSION_PATH)
    # driver = webdriver.Chrome(service = Service(executable_path='/usr/bin/chromedriver'),options=opt)
    driver = webdriver.Chrome(options=opt)
    try:  
        while len(driver.window_handles) == 1 :
            time.sleep(0.5)
            print(driver.window_handles)
        
        driver.switch_to.window(driver.window_handles[1])
        logging.info(driver.window_handles)
        original_window = driver.current_window_handle 


        waitForClickeAble(driver,'//*[@id="onboarding__terms-checkbox"]')
        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[3]/button')
        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div/button[1]')
        arr = importdata()['ph'].split("@")
        for i in range (0,len(arr)):
            r ='//*[@id="import-srp__srp-word-%s"]' % i
            typingCustome(driver,r,arr[i])
            # print(r)   

        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[4]/div/button')
        typingCustome(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input','12345678')
        typingCustome(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input','12345678')
        
        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input')
        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button')
   

        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button')
        driver.execute_script("location.reload()")

        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button')
        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button')

        waitForClickeAble(driver,'//*[@id="popover-content"]/div/div/section/div[1]/div/button/span')
        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[2]/div/div[3]/div/div/button/span')
        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[6]')  
        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[1]/div/button[6]') 
        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/button')
        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[3]/a/h6')
        typingCustome(driver,' //*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input',importdata()['chain'])
        typingCustome(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input',importdata()['rpc'])
        typingCustome(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input',importdata()['number'])
        typingCustome(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/div/input',importdata()['fee'])
        typingCustome(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/label/input',importdata()['scan'])
        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]')
        waitForClickeAble(driver,'//*[@id="popover-content"]/div/div/section/div[2]/div/button[1]')
        time.sleep(10)
        #https://app.uniswap.org/swap
        logging.info('mid')
        
        driver.switch_to.window(driver.window_handles[0])
        driver.get('https://app.uniswap.org/swap')
        waitForClickeAble(driver,'//*[@id="root"]/span/span/div[1]/nav/div/div[3]/div/div[3]/div/button')
        waitForClickeAble(driver,'//*[@id="wallet-dropdown-scroll-wrapper"]/div/div/div[2]/div[1]/div/div[2]/button')
        driver.switch_to.window(driver.window_handles[2])
        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[1]/div/div[3]/div[2]/footer/button[2]')
        waitForClickeAble(driver,'//*[@id="app-content"]/div/div[1]/div/div[3]/div[2]/footer/button[2]')
        driver.switch_to.window(driver.window_handles[0])
        logging.info('befor uni')
        logging.info('This is an info message')
        logging.info('finish')
    except Exception as e:
        print(e)
        # driver.save_screenshot("./picture/%s.png" % str(int(round(time.time() * 1000))))
        logging.error('This is an error message')

while True:
    main()
