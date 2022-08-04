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
name="Ariana Red"
phone="081234567890"

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
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[3]/a[1]").click() #select sub menu
        time.sleep(2)

    def test_A_MyInfo_EmergencyContact_Add_Check_Mandatory (self):
        driver = self.driver
        driver.find_element(By.ID,"btnAddContact").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnSaveEContact").click()
        time.sleep(3)
        
        response_name = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/span[1]").text
        response_relationship = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[2]/form[1]/fieldset[1]/ol[1]/li[2]/span[1]").text
        response_phone = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[2]/form[1]/fieldset[1]/ol[1]/li[3]/span[1]").text

        self.assertEqual(response_name,'Required')
        self.assertEqual(response_relationship,'Required')
        self.assertEqual(response_phone,'At least one phone number is required')

    def test_B_MyInfo_EmergencyContact_Add_Success (self):
        driver = self.driver
        driver.find_element(By.ID,"btnAddContact").click()
        time.sleep(2)
        driver.find_element(By.ID,"emgcontacts_name").send_keys(name)
        time.sleep(1)
        driver.find_element(By.ID,"emgcontacts_relationship").send_keys("Sister")
        time.sleep(1)
        driver.find_element(By.ID,"emgcontacts_mobilePhone").send_keys(phone)
        time.sleep(1)
        driver.find_element(By.ID,"btnSaveEContact").click()
        time.sleep(3)
        
        response_title = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[3]/div[2]/form[1]/table[1]/tbody[1]/tr[1]").text
        
        self.assertNotEqual(response_title,'No Records Found')

    def test_C_MyInfo_EmergencyContact_Delete_Success (self):
        driver = self.driver
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[3]/div[2]/form[1]/table[1]/thead[1]/tr[1]/th[1]/input[1]").click()
        time.sleep(2)
        driver.find_element(By.ID,"delContactsBtn").click()
        time.sleep(3)
        
        response_title = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[3]/div[2]/form[1]/table[1]/tbody[1]/tr[1]").text
        
        self.assertEqual(response_title,'No Records Found')


    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()