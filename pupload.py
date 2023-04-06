from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import string
import pyautogui
import urllib.request
from selenium.webdriver.chrome.options import Options
from PIL import Image
from pathlib import Path
urllist=[]
import os
import csv
import pyautogui
import csv
with open('caption.csv', 'r') as f:
  file = csv.reader(f)
  data1 = list(file)
with open('description.csv', 'r') as f:
  file2 = csv.reader(f)
  data2 = list(file2)

dir_path = "E:/new projects of python/tasks/Pinterest/data"
# list to store files
res = []
videoname=[]
i=0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

import pandas as pd
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=../googleProfile")
chrome_options.add_argument("--remote-debugging-port=9222")

browser = uc.Chrome(use_subprocess=True,options=chrome_options)
for name in res:
    browser.get("https://www.pinterest.com/")
    create=browser.find_element(by=By.XPATH,value='/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[3]/div/div/div/div/span')
    create.click()
    time.sleep(5)
    create1=browser.find_element(By.XPATH,'*//span[text()="Create Pin"]')
    create1.click()
    time.sleep(5)
    upload=browser.find_element(by=By.XPATH,value='/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/input')
    upload.send_keys(dir_path+"/"+name)
    time.sleep(5)
    caption=browser.find_element(by=By.XPATH,value='/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/textarea')
    caption.send_keys(data1[i])
    time.sleep(5)
    
    des=browser.find_element(by=By.XPATH,value='/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/div/div/div/div')
    des.send_keys(data2[i])
    time.sleep(5)
    create2=browser.find_element(By.XPATH,value='*//div[text()="Save"]')
    create2.click()
    time.sleep(5)
    i=i+1
 
    
 
