# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BrowseAllCorpora(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.laudatio-repository.org/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_browse_all_corpora(self):
        driver = self.driver
        driver.get(self.base_url + "/repository/")
        driver.find_element_by_link_text("Browse").click()
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "T-Codex"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "ShenouteA22"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "DDB"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "GerManC"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "KAJUK"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Fuerstinnenkorrespondenz"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "ddd-ad"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "HIPKON"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "HSJ"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "MaKoHiZZ"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Maerchenkorpus"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Mercurius"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "RIDGES-Herbology"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "VereinSchoenfeld"))
    
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
