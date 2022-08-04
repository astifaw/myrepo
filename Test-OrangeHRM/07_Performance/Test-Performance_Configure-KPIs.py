import numbers
import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#variable
url="https://opensource-demo.orangehrmlive.com/index.php/performance/searchKpi" #URL langsung ke menu
username="Admin" # username admin
password="admin123" # password admin
KPI="Responsibility"

class Test_Performance_Configure_KPIs(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(3)

    def test_A_Performance_Configure_KPIs_Add_Check_Mandatory (self):
        driver = self.driver
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID,"saveBtn").click()
        time.sleep(3)
        
        response_jobtitle = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/span[1]").text
        response_KPI = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[2]/form[1]/fieldset[1]/ol[1]/li[2]/span[1]").text

        self.assertEqual(response_jobtitle,'Required')
        self.assertEqual(response_KPI,'Required')

    def test_B_Performance_Configure_KPIs_Add_Success (self):
        driver = self.driver
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/select[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//option[contains(text(),'Software Engineer')]").click()
        time.sleep(1)
        driver.find_element(By.ID,"defineKpi360_keyPerformanceIndicators").send_keys(KPI)
        time.sleep(1)
        driver.find_element(By.ID,"saveBtn").click()
        time.sleep(3)
        
    expected_current_url = url

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()