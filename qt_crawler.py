# -*- coding: utf-8 -*-
"""
PyQT5教學
https://shareboxnow.com/pyqt5/#%E5%A6%82%E4%BD%95%E8%AE%93Qt5_Button%E6%9C%89%E4%BD%9C%E7%94%A8%E5%91%A2%EF%BC%9F
""" 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from qui import Ui_Dialog

class AppWindow(QDialog):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton.clicked.connect(self.send_info)
    def send_info(self):
        webdriver.ChromeOptions().add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
        # options.add_argument('--headless')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) 
        driver.get('https://sys.ndhu.edu.tw/AA/CLASS/SubjEvaluate/eval-login.aspx')
        account = driver.find_element_by_css_selector('#ContentPlaceHolder1_acc')
        password = driver.find_element_by_css_selector('#ContentPlaceHolder1_pass') 
        save_btn = driver.find_element_by_css_selector('#ContentPlaceHolder1_btn_login')
        account_qt = self.ui.lineEdit.text()
        psw_qt = self.ui.lineEdit_2.text()
        account.send_keys(account_qt)
        password.send_keys(psw_qt)
        save_btn.click()
        driver.refresh()
        self.ui.listWidget.addItem("已登入您個人頁面")
        time.sleep(2)
        sp = BeautifulSoup(driver.page_source,'lxml')
        count = len(sp.select("tbody > tr")) - 1
        student_info = sp.select("#ContentPlaceHolder1_Label1")[0].text
        self.ui.listWidget.addItem(f"{student_info}\n本學期共修{count}個科目")
        for i in range(int(count)):
            time.sleep(1)
            try:
                trs = WebDriverWait(driver, 10).until(lambda d: d.find_elements(By.XPATH, "//tbody/tr"))
                del trs[0]
                course_code = WebDriverWait(driver, 10).until(lambda d: trs[i].find_elements_by_tag_name("td")[0]).text
                course_name = WebDriverWait(driver, 10).until(lambda d: trs[i].find_elements_by_tag_name("td")[1]).text
                course_status = WebDriverWait(driver, 10).until(lambda d: trs[i].find_elements_by_tag_name("td")[3]).text
                url = WebDriverWait(driver, 10).until(lambda d: trs[i].find_elements_by_tag_name("td")[4].find_element_by_tag_name("a"))
                course_url = url.get_attribute("href")
                info = f'---------\n課程代碼/課程名稱： {course_code}/{course_name} \n填寫狀態： {course_status}\n填寫網址： {course_url}'
                self.ui.listWidget.addItem(info)
                url.click()
                btns = WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_css_selector('input[value="5"]'))
                btns.size()>0
            except Exception as e:
                    print(f"1: {e}")
                    pass
            self.ui.listWidget.addItem(f"填寫第{i+1}份，科目： {course_name}")
            for k in range(len(btns)):
                try:
                    btns[k].click()
                except Exception as e:
                    print(f"2: {e}")
                    pass
            WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_css_selector('input[value="1"]')[12]).click()
            WebDriverWait(driver, 10).until(lambda d: d.find_elements_by_css_selector('input[value="資料存檔"]')[0]).click()
            driver.switch_to.alert.accept()
            self.ui.listWidget.addItem(f"科目： {course_name} 填寫完畢\n進入下一個科目.....")

        driver.quit()
        self.ui.listWidget.addItem("Done!")
        self.ui.listWidget.scrollToBottom()  # 這行很重要，如果你沒加這行，如果超過self.displayListWidget範圍的話，他是不會往下執行的
        
app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
