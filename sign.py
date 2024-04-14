
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



def click(worker,location):
     WebDriverWait(worker, 5).until(EC.presence_of_element_located((By.XPATH, location))).click()
     
def typing(worker,location,string):
    WebDriverWait(worker, 5).until(EC.presence_of_element_located((By.XPATH, location))).send_keys(string)
    
def importdata():
    with open('.env', 'r') as file:
        data = file.read()
    parsed_json = json.loads(data)
    return parsed_json
def test_login_button():

    print('strad')
    EXTENSION_PATH = 'MMask.crx'

    opt = Options()
    opt.add_argument("--headless=new")
    opt.add_argument('--disable-gpu')
    opt.add_argument("--no-sandbox")
    opt.add_extension(EXTENSION_PATH)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
    while len(driver.window_handles) == 1 :
        time.sleep(0.5)
        print(driver.window_handles)
       
    driver.switch_to.window(driver.window_handles[1])
    print(driver.window_handles)
    original_window = driver.current_window_handle 
    
    time.sleep(1)
    click(driver,'//*[@id="onboarding__terms-checkbox"]')
    click(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[3]/button')
    click(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div/button[1]')
    arr = importdata()['ph'].split("@")
    for i in range (0,len(arr)):
        r ='//*[@id="import-srp__srp-word-%s"]' % i
        typing(driver,r,arr[i])
        print(r)
        
        
        
        
    time.sleep(0.2)   
    click(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[4]/div/button')
    typing(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input','12345678')
    typing(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input','12345678')
    click(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input')
    click(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button') 
    click(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button')
    time.sleep(0.2)
    click(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button')
    time.sleep(0.2)
    click(driver,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button')
    time.sleep(2)
    click(driver,'//*[@id="popover-content"]/div/div/section/div[1]/div/button/span')
    time.sleep(2)        
    click(driver,'//*[@id="app-content"]/div/div[2]/div/div[3]/div/div/button/span')  
    click(driver,'//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[6]')  
    click(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[1]/div/button[6]')  
    
    click(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/button')
    
    click(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[3]/a/h6')
   
    typing(driver,' //*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input','eth2')
    typing(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input',importdata()['rpc'])
    typing(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input','1')
    typing(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/div/input','eth')
    typing(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/label/input','https://etherscan.io')
    click(driver,'//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]')
    time.sleep(0.2)
    click(driver,'//*[@id="popover-content"]/div/div/section/div[2]/div/button[1]')
    #https://app.uniswap.org/swap
    print('mid')
    driver.switch_to.window(driver.window_handles[0])
    driver.get('https://app.uniswap.org/swap')
    click(driver,'//*[@id="root"]/span/span/div[1]/nav/div/div[3]/div/div[3]/div/button')
    time.sleep(1)
    click(driver,'//*[@id="wallet-dropdown-scroll-wrapper"]/div/div/div[2]/div[1]/div/div[2]/button')
    time.sleep(5)
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[2])
    click(driver,'//*[@id="app-content"]/div/div[1]/div/div[3]/div[2]/footer/button[2]')
    click(driver,'//*[@id="app-content"]/div/div[1]/div/div[3]/div[2]/footer/button[2]')
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)
    print('befor uni')
    
    while True :
        millisec = str(int(round(time.time() * 1000)))
        driver.execute_script("location.reload()")
        time.sleep(1)
        # driver.save_screenshot("./picture/%s.png" % millisec)
        print(millisec)
        logging.info(millisec)
        time.sleep(20)
        
test_login_button()  
