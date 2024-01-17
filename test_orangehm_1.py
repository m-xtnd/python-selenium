# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

opts = ChromeOptions()
opts.add_argument("--window-size=2560,1440")

class test_orangehm_1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_failedlogin_retrieve(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").click()
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("ad")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/div/div/div[2]/div[2]/form/div[4]/p").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
        driver.find_element(By.NAME, "username").click()
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset")
    
    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").click()
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    
    def test_manage_employee(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").click()
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/aside/nav/div[2]/ul/li/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[2]/div").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div/button").click()
        # driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[7]/div/div[6]/div/button[2]").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser/120")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").send_keys("Ethan Hunt")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[4]/div/div[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[4]/div/div[2]/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[4]/div/div[2]/input").send_keys("Ethan124")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").send_keys("Ethan James Hunt")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser")
        # driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div/div/div[2]/div/div/div").click()
        # driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[3]").click()
        # driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[3]/div/div[2]/div/div/div").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").click()
        #ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input | ]]
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").send_keys("Hint Coold")
        # driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[4]").click()
        # driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/div/div[2]/div/div/input").send_keys("sandhya  biradar")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[4]/div/div[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[4]/div/div[2]/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[4]/div/div[2]/input").send_keys("sasada")
        driver.find_element(By.XPATH, "//input[@type='password']").click()
        driver.find_element(By.XPATH, "//input[@type='password']").clear()
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("pawwsordy")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("passwordy")
        driver.find_element(By.XPATH, "//input[@type='password']").click()
        driver.find_element(By.XPATH, "//input[@type='password']").clear()
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("pawwsordy1")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").click()
        # driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("")
        driver.find_element(By.XPATH, "//input[@type='password']").click()
        driver.find_element(By.XPATH, "//input[@type='password']").clear()
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("x1")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("x1")
        driver.find_element(By.XPATH, "//input[@type='password']").click()
        driver.find_element(By.XPATH, "//input[@type='password']").clear()
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("x1000000")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("x1000000")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    
    def test_addnationality(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").click()
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/aside/nav/div[2]/ul/li/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/nationality")
        driver.find_element(By.XPATH, "//a[@href = '#' and (text() = 'Nationalities' or . = 'Nationalities')]").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/header/div[2]/nav/ul/li[5]/a").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/nationality")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div/button/i").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveNationality")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div/div[2]/input").send_keys("Eorzean")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/nationality")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
