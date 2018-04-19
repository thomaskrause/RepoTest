# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SearchIndexAllCorpora(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.laudatio-repository.org"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_search_index_all_corpora(self):
        driver = self.driver
        driver.get(self.base_url + "/repository/")
        driver.find_element_by_link_text("Search").click()
        driver.find_element_by_css_selector("a.facetview_filtershow").click()
        for i in range(60):
            try:
                if self.is_element_present(By.LINK_TEXT, "more"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_link_text("more").click()
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Deutsch Diachron Digital - Referenzkorpus Altdeutsch Version 1.0 (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Deutsche Diachrone Baumbank (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Fuerstinnenkorrespondenz 1.1 (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "GerManC (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "HIPKON: Historisches Predigtenkorpus zum Nachfeld (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Historische Syntax des Jiddischen (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Kasseler Junktionskorpus (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Mannheimer Korpus Historischer Zeitungen und Zeitschriften (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Mercurius-Baumbank (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Märchenkorpus Version 1.0 (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "RIDGES Herbology Version 8.0 (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Shenoute A 22 (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Tatian Corpus of Deviating Examples 2.1 (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Der Nachlass des Vereins für musikalische Privataufführungen - digitale Edition. Vorversion (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Heliand (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Ludolf (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Muspilli (1)"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Sächsiche Weltchronik (1)"))
    
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
