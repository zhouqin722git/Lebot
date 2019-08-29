#-*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')              #允许root权限执行
chrome_options.add_argument('--disable-dev-shm-usage')   #
#chrome_options.add_argument('--headless')                #不用打开图形界面
browser = webdriver.Chrome(chrome_options=chrome_options)

host = "https://172.16.100.161"
username = "admin"
password = "S3cur!ty"

def test_env():
    browser.get("https://www.baidu.com")
    print browser.title

    elem = browser.find_element_by_id("kw")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in browser.page_source
    browser.close()

#test_env()

def login():
    browser.get(host)

    #login
    locator = (By.ID, 'username')
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located(locator))
    browser.find_element_by_id("username").send_keys(username)
    browser.find_element_by_xpath("//input[@type='password']").send_keys(password)
    browser.find_element_by_xpath("//input[@ng-model='$ctrl.captcha.value']").send_keys("bypass")
    browser.find_element_by_xpath("//hs-button[@text='global.login']").click()
    time.sleep(3)

    #security_info
    browser.find_element_by_xpath("//hs-i18n[@t='security.menu.securityInf']").click()
    time.sleep(3)

    #whitelist_management
    global_locator = (By.XPATH, "//hs-i18n[@t='security.menu.whitelist']")
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located, global_locator)
    browser.find_element_by_xpath("//hs-i18n[@t='security.menu.whitelist']").click()

    #add_ip_value
    browser.find_element_by_xpath("//global-whitelist//hs-i18n[@t='global.common.add']").click()
    time.sleep(3)
    ip_value = browser.find_element_by_xpath("/html/body/div[3]/div[2]/form/div[3]/div/input")
    ip_value.send_keys("1.2.3.4")
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div[3]/div[3]/div/hs-button[1]").click()
    time.sleep(3)
    #edit_ip_value
    # generated_ip_locator = (By.XPATH, "//global-whitelist//*[@id='row_0']/td[3]/hs-table-td/div")
    # WebDriverWait(browser, 10).until(EC.visibility_of_element_located, generated_ip_locator)
    browser.find_element_by_xpath("//*[@id='row_0']/td[7]/hs-table-td/div/a[1]/hs-icon").click()
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/form/div[3]/div/input").clear()
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/form/div[3]/div/input").send_keys('1.2.3.44')
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div[3]/div[3]/div/hs-button[1]").click()
    time.sleep(2)

    #delete_batch
    browser.find_element_by_xpath("//security-inf-whitelist//global-whitelist//th[1]/hs-checkbox/div").click()
    time.sleep(3)
    browser.find_element_by_xpath("//security-inf-whitelist//global-whitelist/div/div[1]/div[1]/hs-button[3]/div/hs-i18n").click()
    time.sleep(3)

    #delete_second_confirm
    delete_confirm_locator = (By.XPATH, "/html/body/div[3]/div[1]")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located, delete_confirm_locator)

    #delete_confirm
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/hs-button[1]/div/hs-i18n").click()
    time.sleep(3)

    #分页
    #browser.find_element_by_xpath("/html/body/div[3]/div[1]").click()
    '''
    #delete_batch
    browser.find_element_by_xpath("//security-inf-whitelist//global-whitelist//th[1]/hs-checkbox/div").click()
    time.sleep(3)
    browser.find_element_by_xpath("//security-inf-whitelist//global-whitelist/div/div[1]/div[1]/hs-button[3]/div/hs-i18n").click()
    time.sleep(3)

    #delete_second_confirm
    delete_confirm_locator = (By.XPATH, "/html/body/div[3]/div[1]")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located, delete_confirm_locator)

    # delete_cancel
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/hs-button[2]").click()
    time.sleep(3)
    '''
    browser.close()

login()
