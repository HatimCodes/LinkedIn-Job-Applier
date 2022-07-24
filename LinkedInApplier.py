from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import xlrd, xlwt
from xlutils.copy import copy
from datetime import date
import pandas as pd
import openpyxl
import csv
from csv import DictWriter
from selenium.common.exceptions import NoSuchElementException
import subprocess

def check_location_ember26():
    try:
        driver.find_element(By.ID,
                            'jobs-search-box-location-id-ember26')
    except NoSuchElementException:
        return False
    return True
def check_location_ember25():
    try:
        driver.find_element(By.ID,
                            'jobs-search-box-location-id-ember25')
    except NoSuchElementException:
        return False
    return True
def check_next_button():
    try:
        driver.find_element(By.XPATH,"//span[text()='Next']")
    except NoSuchElementException:
        return False
    return True
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
subprocess.call(['kill.bat'])
time.sleep(0.5)
options = webdriver.ChromeOptions()
options.binary_location = ('C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe')
driver = webdriver.Chrome('chromedriver.exe',options=options)
file = open("Data\infos.txt", "r")
for line in file:
    word = line.split(";")
    email = word[0]
    password = word[1]
    keywords = word[2]
    where = word[3]
    fullname=word[4]
file.close()
black_list = []
blackli = open("Data\Black List.txt")
for b in blackli:
    black_list.append(b)
blackli.close()
driver.get("https://www.linkedin.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID, 'session_key').send_keys(email)
driver.find_element(By.ID, 'session_password').send_keys(password)
driver.find_element(By.CLASS_NAME,'sign-in-form__submit-button').click()
time.sleep(5)
driver.get("https://www.linkedin.com/jobs/search/?geoId=101165590&keywords=php")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,'.jobs-search-box__text-input.jobs-search-box__keyboard-text-input').clear()
driver.find_element(By.CSS_SELECTOR,'.jobs-search-box__text-input.jobs-search-box__keyboard-text-input').send_keys(keywords)

time.sleep(1)
if check_location_ember25():
    driver.find_element(By.ID,'jobs-search-box-location-id-ember25').clear()
    driver.find_element(By.ID,'jobs-search-box-location-id-ember25').send_keys(where)
if check_location_ember26():
    driver.find_element(By.ID,'jobs-search-box-location-id-ember26').clear()
    driver.find_element(By.ID,'jobs-search-box-location-id-ember26').send_keys(where)

time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='Search']").click()
time.sleep(5)
time.sleep(5)
f = open('Data\Data.csv', 'a')
writer = csv.writer(f)
driver.find_element(By.XPATH,"//button[text()='All filters']").click()
time.sleep(10)
driver.find_element(By.CSS_SELECTOR,'.artdeco-toggle.artdeco-toggle--32dp.artdeco-toggle--default.ember-view').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'.reusable-search-filters-buttons.search-reusables__secondary-filters-show-results-button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view').click()
time.sleep(10)
def saveto_excel(jbnm,cmpnm,dtapp,skp,lk,flnm):
 try:
     row = [jbnm,cmpnm,dtapp,skp,lk,flnm]
     with open('Data\Data.csv', 'a', newline='') as f:
         writer = csv.writer(f)
         writer.writerow(row)
 except:
     print("hmm")

def check_apply():
    try:
        driver.find_element(By.CLASS_NAME,
                            'jobs-search__left-rail')
    except NoSuchElementException:
        return False
    return True

links = []
def check_linkout():
    try:
        driver.find_element(By.CSS_SELECTOR,
                            '.jobs-apply-button.artdeco-button.artdeco-button--icon-right.artdeco-button--3.artdeco-button--primary.ember-view')
    except NoSuchElementException:
        return False
    return True
def check_easy_apply():
    try:
        driver.find_element(By.XPATH,"//span[text()='Easy Apply']")
    except NoSuchElementException:
        return False
    return True
def check_discard():
    try:
        driver.find_element(By.XPATH,"//span[text()='Discard']")
    except NoSuchElementException:
        return False
    return True
def submit_app():
    try:
        driver.find_element(By.XPATH,"//span[text()='Submit application']")
    except NoSuchElementException:
        return False
    return True

def check_if_job_available():
    try:
        driver.find_element(By.CSS_SELECTOR,
                            '.disabled.ember-view.job-card-container__link.job-card-list__title')
    except NoSuchElementException:
        return False
    return True

def check_job_name():
    try:
        driver.find_element(By.CSS_SELECTOR,'.t-24.t-bold.jobs-unified-top-card__job-title')
    except NoSuchElementException:
        return False
    return True

def check_black_list_companies(com):
    for c in black_list:
        if c == com:
            return True
            break
        else:
            False

def check_compnay_name():
    try:
        driver.find_element(By.CSS_SELECTOR,'.ember-view.t-black.t-normal')
    except NoSuchElementException:
        return False
    return True

def check_close_after_submit():
    try:
        driver.find_element(By.CSS_SELECTOR,'.artdeco-modal__dismiss.artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--2.artdeco-button--tertiary.ember-view')
    except NoSuchElementException:
        return False
    return True

def load_jobs_side():
     listul = driver.find_element(By.CSS_SELECTOR,'.jobs-search-results__list.list-style-none')
     ite = listul.find_elements(By.TAG_NAME,"li")
     results = driver.find_elements(By.CSS_SELECTOR,
                                    '.job-card-list__entity-lockup.artdeco-entity-lockup.artdeco-entity-lockup--size-4.ember-view')
     links.clear()
     for r in ite:
         if r.get_attribute("class").__contains__("ember-view   jobs-search-results__list-item occludable-update p0 relative"):
             r.click()

def click_jobs():
    main_page = driver.current_url
    counter=0
    skipped = 0
    applied = 0
    while True:
        load_jobs_side()
        jobs = driver.find_elements(By.CSS_SELECTOR,
                                    '.disabled.ember-view.job-card-container__link.job-card-list__title')
        if check_if_job_available():
            for j in jobs:
                try:
                    j.click()
                    time.sleep(7)
                    if check_job_name():
                        job_name = driver.find_element(By.CSS_SELECTOR,'.t-24.t-bold.jobs-unified-top-card__job-title').text
                    else:
                        job_name="None"
                    if check_compnay_name():
                        compnay_name = driver.find_element(By.CSS_SELECTOR, '.ember-view.t-black.t-normal').text

                    else:
                        compnay_name = "None"
                    date_apply = date.today()
                    joblink = driver.current_url
                    if check_black_list_companies(compnay_name):
                        print("Black Listed Company")
                        saveto_excel(job_name, compnay_name, date_apply,"Skipped",joblink,fullname)
                        skipped = skipped + 1
                    else:
                        if check_linkout():
                            saveto_excel(job_name, compnay_name, date_apply,"Skipped",joblink,fullname)
                            skipped = skipped + 1
                        else:
                            print("This part will be for simple apply")
                            if check_easy_apply():
                                driver.find_element(By.XPATH, "//span[text()='Easy Apply']").click()
                                time.sleep(1)
                                if driver.find_element(By.CSS_SELECTOR,'.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view').text.__contains__("Next"):
                                    time.sleep(1)
                                    driver.find_element(By.CSS_SELECTOR,'.artdeco-modal__dismiss.artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--2.artdeco-button--tertiary.ember-view').click()
                                    if check_discard():
                                        driver.find_element(By.XPATH,"//span[text()='Discard']").click()
                                    saveto_excel(job_name, compnay_name, date_apply, "Skipped", joblink,fullname)
                                    skipped = skipped + 1
                                    time.sleep(1)
                                else:
                                    print("this will be for easy submit")
                                    if submit_app():
                                        driver.find_element(By.XPATH, "//span[text()='Submit application']").click()
                                        applied = applied + 1
                                        time.sleep(3)
                                        if check_close_after_submit():
                                            driver.find_element(By.CSS_SELECTOR,'.artdeco-modal__dismiss.artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--2.artdeco-button--tertiary.ember-view').click()
                                            time.sleep(2)
                                        saveto_excel(job_name, compnay_name, date_apply, "Applied", joblink,fullname)
                                        time.sleep(5)
                            else:
                                print("Already applied")
                                saveto_excel(job_name, compnay_name, date_apply, "Already Applied or Contains Questions", joblink,fullname)
                                skipped = skipped + 1
                except Exception as e:
                    with open('Data\Counter.txt', 'w') as f:
                        f.write("Applied Job : "+ str(applied)+ "\nSkipped Jobs : "+ str(skipped))
                    with open("Logs\logs.txt", "a") as g:
                        g.write(str(e) + "\n")
                    with open("Logs\logsDetails.txt", "a") as g:
                        g.write(repr(e) + "\n")

            counter = counter+25
            next_page = main_page+"&start="+str(counter)
            driver.get(next_page)
            time.sleep(10)
        else:
            print("Done")
            return False

click_jobs()
for l in links:
    print(l)
