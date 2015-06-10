# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ExampleDocEntry(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.laudatio-repository.org/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_example_doc_entry(self):
        driver = self.driver
        driver.get(self.base_url + "/repository/")
        driver.find_element_by_link_text("Browse").click()
        driver.find_element_by_link_text("Fuerstinnenkorrespondenz").click()
        driver.find_element_by_css_selector(u"b[title=\"Contains classical metadata for the object ‘document’\"]").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "#ex2-node-2-0 > td"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("#ex2-node-2-0 > td").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "#ex2-node-2-0-1 > td"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("#ex2-node-2-0-1 > td").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "#ex2-node-2-0-1-1 > td"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertEqual("AD_JE2_1677_08_14", driver.find_element_by_css_selector("#ex2-node-2-0-1-1 > td").text)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
