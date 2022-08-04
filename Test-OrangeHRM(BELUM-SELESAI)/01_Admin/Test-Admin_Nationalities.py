import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#variable
url="https://opensource-demo.orangehrmlive.com/index.php/admin/nationality" #URL langsung ke menu
username="Admin" # username admin
password="admin123" # password admin
nationality= "Indonesia"

class Test_Admin_Nationalities(unittest.TestCase): 

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

    def test_A_Add_Check_Field_Mandatory (self):
        driver = self.driver
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(3)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(3)
                    
        response_data = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/span[1]").text
        
        self.assertEqual(response_data, 'Required')
        
    def test_B_Add_New_Nationality (self):
        driver = self.driver
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(3)
        driver.find_element(By.ID,"nationality_name").send_keys(nationality)
        time.sleep(3)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(3)

    def test_C_Add_Existing_Nationality (self):
        driver = self.driver
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID,"nationality_name").send_keys(nationality)
        time.sleep(3)

        response_data = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/span[1]").text
        
        self.assertEqual(response_data, 'Already exists')

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()