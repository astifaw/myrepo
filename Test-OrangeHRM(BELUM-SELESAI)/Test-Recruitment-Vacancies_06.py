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


class Test_Recruitment_Vacancies(unittest.TestCase): 

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
        driver.find_element(By.ID,"menu_recruitment_viewJobVacancy").click()
        time.sleep(2)

    def test_A_Recruitment_Vacancy_Add_Check_Mandatory_Field (self):
        driver = self.driver
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(3)
        
        response_title = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/span[1]").text
        response_vacancy = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[2]/span[1]").text
        response_manager = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[3]/span[1]").text

        self.assertEqual(response_title,'Required')
        self.assertEqual(response_vacancy,'Required')
        self.assertEqual(response_manager,'Invalid')

    def test_B_Recruitment_Vacancy_Add_Success (self):
        driver = self.driver
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        driver.find_element(By.ID,"addJobVacancy_jobTitle").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/select[1]/option[21]").click()
        time.sleep(1)
        driver.find_element(By.ID,"addJobVacancy_name").send_keys("Software Engineer Recruitment")
        time.sleep(1)
        driver.find_element(By.ID,"addJobVacancy_hiringManager").send_keys("Lisa")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[4]/ul[1]/li[1]").click()
        time.sleep(1)
        driver.find_element(By.ID,"addJobVacancy_noOfPositions").send_keys("3")
        time.sleep(1)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(3)
        
        response_title = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/h1[1]").text
        
        self.assertEqual(response_title,'Edit Job Vacancy')

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()