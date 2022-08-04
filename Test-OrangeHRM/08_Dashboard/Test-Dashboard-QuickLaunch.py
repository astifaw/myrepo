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
url="https://opensource-demo.orangehrmlive.com/index.php/dashboard" #URL langsung ke menu
username="Admin" # username admin
password="admin123" # password admin

class Test_Dashboard_QuickLaunch(unittest.TestCase): 

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

    def test_A_Dashboard_Quicklaunch_AssignLeave (self):
        driver = self.driver
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/a[1]/img[1]").click()
        time.sleep(3)
                
    expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/leave/assignLeave"
    
    def test_A_Dashboard_Quicklaunch_LeaveList (self):
        driver = self.driver
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/a[1]/img[1]").click()
        time.sleep(3)
                
    expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/leave/viewLeaveList"

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()