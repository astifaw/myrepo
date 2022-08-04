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
url="https://opensource-demo.orangehrmlive.com/index.php/pim/viewMyDetails" #URL langsung ke menu
username="Admin" # username admin
password="admin123" # password admin
number="121-039-31030"

class Test_MyInfo_EmergencyContact(unittest.TestCase): 

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
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[5]/a[1]").click() #select sub menu
        time.sleep(2)

    def test_A_MyInfo_Immigration_Add_Check_Mandatory (self):
        driver = self.driver
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(3)
        
        response_number = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[2]/form[1]/fieldset[1]/ol[1]/li[2]/span[1]").text

        self.assertEqual(response_number,'Required')
        
    def test_B_MyInfo_Immigration_Add_Success (self):
        driver = self.driver
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID,"immigration_number").send_keys(number)
        time.sleep(1)
        driver.find_element(By.ID,"immigration_passport_issue_date").click()
        time.sleep(1)
        driver.find_element(By.ID,"immigration_passport_issue_date").send_keys("2022-01-07")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[2]/form[1]/fieldset[1]/ol[1]/li[3]/img[1]").click()
        time.sleep(1)
        driver.find_element(By.ID,"immigration_passport_expire_date").click()
        time.sleep(1)
        driver.find_element(By.ID,"immigration_passport_expire_date").send_keys("2027-01-07")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[2]/form[1]/fieldset[1]/ol[1]/li[4]/img[1]").click()
        time.sleep(1)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(3)
        
        response_title = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[3]/div[2]/form[1]/table[1]/tbody[1]/tr[1]").text
        
        self.assertNotEqual(response_title,'No Records Found')

    def test_C_MyInfo_EmergencyContact_Delete_Success (self):
        driver = self.driver
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[3]/div[2]/form[1]/table[1]/thead[1]/tr[1]/th[1]/input[1]").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnDelete").click()
        time.sleep(3)
        
        response_title = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[3]/div[2]/form[1]/table[1]/tbody[1]/tr[1]").text
        
        self.assertEqual(response_title,'No Records Found')


    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()