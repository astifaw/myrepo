import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#variable
url="https://opensource-demo.orangehrmlive.com/index.php/pim/viewEmployeeList/" #URL langsung ke menu
username="Admin" # username admin
password="admin123" # password admin
firstname= "John"
lastname="Snow"
user_name="JSnow"
user_password="User123?"

class Test_PIM_EmpList(unittest.TestCase): 

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
        time.sleep(2)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(2)
                    
        response_data = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/ol[1]/li[1]/span[1]").text
        
        self.assertEqual(response_data, 'Required')
        
    def test_B_Add_New_Employee (self):
        driver = self.driver
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(3)
        #existing username
        driver.find_element(By.ID,"firstName").send_keys(firstname)
        time.sleep(1)
        driver.find_element(By.ID,"lastName").send_keys(lastname)
        time.sleep(1)
        driver.find_element(By.ID,"chkLogin").click()
        time.sleep(3)
        driver.find_element(By.ID,"user_name").send_keys(username) #existing username
        time.sleep(1)
        driver.find_element(By.ID,"user_password").send_keys(user_password)
        time.sleep(1)
        driver.find_element(By.ID,"re_password").send_keys(user_password)
        time.sleep(1)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(2)

        #not existing username 
        driver.find_element(By.ID,"firstName").send_keys(firstname)
        time.sleep(1)
        driver.find_element(By.ID,"lastName").send_keys(lastname)
        time.sleep(1)
        driver.find_element(By.ID,"user_name").send_keys(user_name) #not existing username
        time.sleep(1)
        driver.find_element(By.ID,"user_password").send_keys(user_password)
        time.sleep(1)
        driver.find_element(By.ID,"re_password").send_keys(user_password)
        time.sleep(1)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(2)

        response_data = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/h1[1]").text
        
        self.assertEqual(response_data, 'Personal Details')

    def test_C_Search_and_Delete_Employee (self):
        driver = self.driver
        #search existing employee
        driver.find_element(By.ID,"empsearch_employee_name_empName").send_keys(firstname," ",lastname)
        time.sleep(1)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(2)
        #delete employee
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/form[1]/div[4]/table[1]/tbody[1]/tr[1]/td[1]").click()
        time.sleep(1)
        driver.find_element(By.ID,"btnDelete").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[3]/div[3]/input[1]").click()
        time.sleep(2)
        #search not existing employee
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(2)

        response_data = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/form[1]/div[4]/table[1]/tbody[1]/tr[1]/td[1]").text
        
        self.assertEqual(response_data, 'No Records Found')

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()