# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
options = webdriver.ChromeOptions() 
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://sys.ndhu.edu.tw/AA/CLASS/SubjEvaluate/eval-login.aspx')

account = driver.find_element_by_css_selector('#ContentPlaceHolder1_acc')   
account.send_keys(str(input("輸入你的帳號： "))) 
password = driver.find_element_by_css_selector('#ContentPlaceHolder1_pass') 
password.send_keys(str(input("輸入你的密碼： ")))
driver.find_element_by_css_selector('#ContentPlaceHolder1_btn_login').click() 
driver.refresh()
print("已登入您個人頁面")
time.sleep(2)
sp = BeautifulSoup(driver.page_source,'lxml')
count = len(sp.select("tbody > tr")) - 1
student_info = sp.select("#ContentPlaceHolder1_Label1")[0].text
print(f"{student_info}\n本學期共修{count}個科目")
for i in range(int(count)):
    time.sleep(2)
    try:
        trs = WebDriverWait(driver, 10).until(lambda d: d.find_elements(By.XPATH, "//tbody/tr"))
        del trs[0]
        course_code = WebDriverWait(driver, 10).until(lambda d: trs[i].find_elements_by_tag_name("td")[0]).text
        course_name = WebDriverWait(driver, 10).until(lambda d: trs[i].find_elements_by_tag_name("td")[1]).text
        course_status = WebDriverWait(driver, 10).until(lambda d: trs[i].find_elements_by_tag_name("td")[3]).text
        url = WebDriverWait(driver, 10).until(lambda d: trs[i].find_elements_by_tag_name("td")[4].find_element_by_tag_name("a"))
        course_url = url.get_attribute("href")
        info = f'---------\n課程代碼/課程名稱： {course_code}/{course_name} \n填寫狀態： {course_status}\n填寫網址： {course_url}'
        print(info)
        url.click()
        btns = WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_css_selector('input[value="5"]'))
    except Exception as e:
        print(f"1: {e}")
        pass
    print(f"填寫第{i+1}份，科目： {course_name}")
    for btn in btns:
        try:
            btn.click()
        except Exception as e:
            print(f"2: {e}")
            pass
    WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_css_selector('input[value="1"]')[12]).click()
    WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_css_selector('input[value="資料存檔"]')[0]).click()
    driver.switch_to.alert.accept()
    print(f"科目： {course_name} 填寫完畢\n進入下一個科目.....")

print("Done!")
driver.quit()
