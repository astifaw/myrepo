import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variable
url="https://opensource-demo.orangehrmlive.com/index.php/leave/viewLeaveList/"
username="Admin" # username admin
password="admin123" # password admin

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_login(self):
        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(3)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

    def test_search_leave(self):
        driver = self.driver
        self.test_login()
        time.sleep(3)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[3]/div[1]/label[1]").click()
        time.sleep(3)
        
        #response_data = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[4]/table[1]/tbody[1]").text
        
        #elf.assertEqual(response_data, 'Job Title 5')
    
    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()