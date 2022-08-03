import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#variable
url="https://opensource-demo.orangehrmlive.com/index.php/leave/viewLeaveList" #URL langsung ke menu
username="Admin" # username admin
password="admin123" # password admin

class Test_Leave(unittest.TestCase): 

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

    def test_A_Assign_Leave_Field_Mandatory (self):
        driver = self.driver
        driver.find_element(By.ID,"menu_leave_assignLeave").click()
        time.sleep(3)
        driver.find_element(By.ID,"assignBtn").click()
        time.sleep(3)
                    
        response_name = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/span[1]").text
        response_type = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[2]/span[1]").text
        response_from = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[4]/span[1]").text
        response_to = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[5]/span[1]").text

        self.assertEqual(response_name, 'Invalid')
        self.assertEqual(response_type, 'Required')
        self.assertEqual(response_from, 'Should be a valid date in yyyy-mm-dd format')
        self.assertEqual(response_to, 'Should be a valid date in yyyy-mm-dd format')
    
    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()