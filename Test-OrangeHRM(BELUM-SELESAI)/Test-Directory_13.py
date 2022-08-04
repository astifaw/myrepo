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
url="https://opensource-demo.orangehrmlive.com/index.php/directory/viewDirectory/" #URL langsung ke menu
username="Admin" # username admin
password="admin123" # password admin
name="Lisa Andrews"

class Test_Directory_Search(unittest.TestCase): 

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

    def test_A_Search_Existing_Employee (self):
        driver = self.driver
        driver.find_element(By.ID,"searchDirectory_emp_name_empName").send_keys(name)
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[4]").click()
        time.sleep(1)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(3)
        
        response_name = driver.find_element(By.XPATH,"//b[contains(text(),'Lisa Andrews')]").text
        
        self.assertEqual(response_name,'Lisa Andrews')
    
    def test_B_Search_NotExisting_Employee (self):
        driver = self.driver
        driver.find_element(By.ID,"searchDirectory_emp_name_empName").send_keys(name,"xx")
        time.sleep(1)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(3)
        
        response_name = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[2]").text
        
        self.assertEqual(response_name,'No Records Found')
    
    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()