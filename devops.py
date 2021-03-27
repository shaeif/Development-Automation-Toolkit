#!/usr/bin/env python

import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

cmd = sys.argv[1]
fileName = sys.argv[2]
githubEmail = ""
githunUsername = ""
githubPassword = ""

def createRepo(fileName):
    #Creating Repo
    driver = webdriver.Chrome()
    driver.get('[https://github.com/login](https://github.com/login)')
    driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[2]').send_keys(githubEmail)
    driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/div/input[1]').send_keys(githubPassword)
    driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/div/input[12]').send_keys(Keys.RETURN)
    driver.get('[https://github.com/new](https://github.com/new)')
    driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input').send_keys(fileName)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button').send_keys(Keys.RETURN)
    driver.quit()
    #Setting enviroment
    os.chdir("/home/shaeif/workspace")
    os.mkdir(fileName)
    os.chdir(fileName)
    #Setting Repo
    os.system(f'echo "# {fileName}" >> [README.md](http://readme.md/)')
    os.system('git init')
    os.system('git add [README.md](http://readme.md/)')
    os.system('git commit -m "first commit"')
    os.system('git branch -M main')
    time.sleep(2)
    os.system(f'git remote add origin [https://github.com/{githunUsername}/{fileName}.git](https://github.com/%7BgithunUsername%7D/%7BfileName%7D.git)')
    os.system('git push -u origin main')
    os.system('code .')
createRepo(fileName)