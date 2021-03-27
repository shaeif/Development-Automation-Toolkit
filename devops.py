#!/usr/bin/env python

import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv


githubEmail = ""
githunUsername = ""
githubPassword = ""
<<<<<<< HEAD
workspace = ""
=======
>>>>>>> af638639b14061c569729cb7e2345094162f832d

def createRepo(fileName):
    driver = webdriver.Chrome()
    driver.get('https://github.com/login')
    driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[2]').send_keys(githubEmail)
    driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/div/input[1]').send_keys(githubPassword)
    driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/div/input[12]').send_keys(Keys.RETURN)
    driver.get('https://github.com/new')
    driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input').send_keys(fileName)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button').send_keys(Keys.RETURN)
    driver.quit()

def createLocalRepo():
    os.system(f'echo "# {fileName}" >> README.md')
    os.system('git init')
    os.system('git add README.md ')
    os.system('git commit -m "first commit"')
    os.system('git branch -M main')
    time.sleep(2)
    os.system(f'git remote add origin https://github.com/{githunUsername}/{fileName}.git')
    os.system('git push -u origin main')
    os.system('code .')

def setUp():
    os.mkdir(fileName)
    os.chdir(fileName)

def start(fileName):
    os.chdir(workspace)
    options = ["0. Normal","1. Angular","2. laravel","3. React","4. React-Native"]
    for x in options:
        print(x)
    o = input("Enter Choice \n")
    if o == "1" or o == "Angular": os.system(f'ng new {fileName}') 
    elif o == "0" or o == "Normal": os.mkdir(fileName)
    elif o == "2" or o == "laravel": os.system(f'composer create-project laravel/laravel {fileName}')
    elif o == "3" or o == "React": os.system(f'npx create-react-app {fileName}')
    elif o == "4" or o == "React-native" : os.system(f'expo init {fileName}')
    else : 
        print("Enter a valid option \n")
        start(fileName)
    os.chdir(fileName)
    createLocalRepo()

if len(sys.argv) != 2: 
    print("Usage : devops.py \"file name to be created\"")
else:
    fileName = sys.argv[1]
    createRepo(fileName)
    start(fileName)
        




