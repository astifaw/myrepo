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
url="https://opensource-demo.orangehrmlive.com/index.php/leave/viewLeaveList" #URL langsung ke menu
username="Admin" # username admin
password="admin123" # password admin
keyword="Lisa" #employee's first name
datefrom="2022-08-15" #Leave start date
dateto="2022-08-15" #Leave end date

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

    def test_A_Entitlements_Add_Success (self):
        driver = self.driver
        driver.find_element(By.ID,"menu_leave_Entitlements").click()
        time.sleep(1)
        driver.find_element(By.ID,"menu_leave_addLeaveEntitlement").click()
        time.sleep(2)
        driver.find_element(By.ID,"entitlements_employee_empName").send_keys(keyword) #employee name
        time.sleep(2)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[4]/ul[1]/li[1]").click() #select employee
        time.sleep(1)
        driver.find_element(By.ID,"entitlements_leave_type").click() #select leave type
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[3]/select[1]/option[4]").click()
        time.sleep(1)
        driver.find_element(By.ID,"entitlements_entitlement").send_keys("12") #input entitlements
        time.sleep(1)
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(3)

    def test_B_Assign_Leave_Field_Mandatory (self):
        driver = self.driver
        driver.find_element(By.ID,"menu_leave_assignLeave").click()
        time.sleep(3)
        driver.find_element(By.ID,"assignBtn").click() #cek mandatory field
        time.sleep(3)
                    
        response_name = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/span[1]").text
        response_type = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[2]/span[1]").text
        response_from = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[4]/span[1]").text
        response_to = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[5]/span[1]").text

        self.assertEqual(response_name, 'Invalid')
        self.assertEqual(response_type, 'Required')
        self.assertEqual(response_from, 'Should be a valid date in yyyy-mm-dd format')
        self.assertEqual(response_to, 'Should be a valid date in yyyy-mm-dd format')
    
    def test_C_Assign_Leave_and_Search (self):
        driver = self.driver
        driver.find_element(By.ID,"menu_leave_assignLeave").click()
        time.sleep(3)
        driver.find_element(By.ID,"assignleave_txtEmployee_empName").send_keys(keyword)
        time.sleep(2)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[6]/ul[1]/li[1]").click()
        time.sleep(1)
        driver.find_element(By.ID,"assignleave_txtLeaveType").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[2]/select[1]/option[5]").click()
        time.sleep(3)
        driver.find_element(By.ID,"assignleave_txtFromDate").clear()
        time.sleep(1)
        driver.find_element(By.ID,"assignleave_txtFromDate").send_keys(datefrom)
        time.sleep(1)
        driver.find_element(By.ID,"assignleave_txtToDate").clear()
        time.sleep(1)
        driver.find_element(By.ID,"assignleave_txtToDate").send_keys(dateto)
        time.sleep(1)
        driver.find_element(By.ID,"assignleave_txtComment").send_keys("Mudik")
        time.sleep(1)
        driver.find_element(By.ID,"assignBtn").click()
        time.sleep(3)
        driver.find_element(By.ID,"menu_leave_viewLeaveList").click() #cek data leave assignment di Leave List
        time.sleep(3)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[3]/div[1]/label[1]").click() #cek data leave assignment
        time.sleep(3)
        driver.find_element(By.ID,"leaveList_txtEmployee_empName").send_keys(keyword)
        time.sleep(2)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[5]/ul[1]/li[1]").click()
        time.sleep(1)
        driver.find_element(By.ID,"btnSearch").click()

        response_result = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/form[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]")

        self.assertNotEqual(response_result, 'No Records Found')
    
    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()