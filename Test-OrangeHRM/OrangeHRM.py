import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variable
url="https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
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
        time.sleep(1)

    def test_search(self):
        driver = self.driver
        self.test_login()
        time.sleep(3)
        driver.find_element(By.ID,"searchSystemUser_userName").send_keys("linda")
        time.sleep(3)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/form[1]/div[4]/table[1]/tbody[1]/tr[1]/td[1]/input[1]").click()
        time.sleep(3)
        
        response_data = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td[2]/a").text
        
        self.assertEqual(response_data, 'linda')
    
    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()