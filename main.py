import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

in_usr = ""
pas_d = ""
acc_nm = "deliciae_bakes"

chr_drvr = "D:\Softwares\chromedriver_win32\chromedriver.exe"
drvr = webdriver.Chrome(executable_path=chr_drvr)

drvr.get(url="https://www.instagram.com")
time.sleep(5)
iusr = drvr.find_element_by_name("username")
ipasd = drvr.find_element_by_name("password")
iusr.send_keys(in_usr)
ipasd.send_keys(pas_d)
ipasd.send_keys(Keys.ENTER)
time.sleep(5)
inotf = drvr.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
inotf.send_keys(Keys.ENTER)
time.sleep(2)
drvr.get(url=f"https://www.instagram.com/{acc_nm}")
time.sleep(5)
iflw = drvr.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
iflw.click()
time.sleep(2)

for k in range(3):
    iflbtn = drvr.find_elements_by_css_selector("li button")
    for i in range(5):
        try:
            time.sleep(2)
            iflbtn[i].click()
        except ElementClickInterceptedException:
            icanc = drvr.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
            icanc.click()
    iscrn = drvr.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
    for j in range(2):
        drvr.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", iscrn)
        time.sleep(2)