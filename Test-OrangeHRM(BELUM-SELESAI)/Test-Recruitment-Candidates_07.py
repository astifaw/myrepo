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
url="https://opensource-demo.orangehrmlive.com/index.php/recruitment/viewCandidates" #URL langsung ke menu
username="Admin" # username admin
password="admin123" # password admin
email="ronaldo5@mailinator.com"

class Test_Recruitment_Candidates(unittest.TestCase): 

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

    def test_A_Recruitment_Candidates_Add_Check_Mandatory (self):
        driver = self.driver
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(5)
        
        response_firstname = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/ol[1]/li[1]/span[1]").text
        response_lastname = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/ol[1]/li[3]/span[1]").text
        response_email = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[2]/span[1]").text

        self.assertEqual(response_firstname,'Required')
        self.assertEqual(response_lastname,'Required')
        self.assertEqual(response_email,'Required')

    def test_B_Recruitment_Candidates_Add_Success (self):
        driver = self.driver
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID,"addCandidate_firstName").send_keys("Ronaldo")
        time.sleep(1)
        driver.find_element(By.ID,"addCandidate_lastName").send_keys("Arman")
        time.sleep(1)
        driver.find_element(By.ID,"addCandidate_email").send_keys(email)
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[2]/li[1]/select[1]").click()
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[2]/li[1]/select[1]/option[3]").click()

        driver.find_element(By.ID,"btnSave").click()
        time.sleep(3)
        
        response_email = driver.find_element(By.ID,"addCandidateHeading").text
        
        self.assertEqual(response_email,'Candidate')
        
    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()