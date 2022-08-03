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
url="https://opensource-demo.orangehrmlive.com/index.php/time/viewEmployeeTimesheet" #URL langsung ke menu
username="Admin" # username admin
password="admin123" # password admin
date_today="2022-07-12" #today
date_future="2022-09-03" #future date
date_yesterday="2022-06-30" #punch in date has passed
time_punchin='08:00' #punch in time
time_punchout='16:00' #punch out time

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
        driver.find_element(By.ID,"menu_attendance_Attendance").click()
        time.sleep(1)

    def test_A_Attendance_Punch_In_Success (self):
        driver = self.driver
        driver.find_element(By.ID,"menu_attendance_punchIn").click()
        time.sleep(2)
        driver.find_element(By.ID,"attendance_date").clear()
        time.sleep(1)
        driver.find_element(By.ID,"attendance_date").send_keys(date_today)
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[2]/form[1]/fieldset[1]/ol[1]/li[2]/label[1]/label[1]").click()
        time.sleep(2)
        driver.find_element(By.ID,"attendance_time").clear()
        time.sleep(2)
        driver.find_element(By.ID,"attendance_time").send_keys(time_punchin)
        time.sleep(2)
        driver.find_element(By.ID,"attendance_note").click()
        time.sleep(2)
        driver.find_element(By.ID,"btnPunch").click()
        time.sleep(3)

        response_title = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/h1[1]").text
        
        self.assertEqual(response_title,'Punch Out')

    def test_B_Attendance_Punch_Out_Date_Before_PunchIn (self):
        driver = self.driver
        driver.find_element(By.ID,"menu_attendance_punchIn").click()
        time.sleep(2)
        driver.find_element(By.ID,"attendance_date").clear()
        time.sleep(1)
        driver.find_element(By.ID,"attendance_date").send_keys(date_yesterday)
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[2]/form[1]/fieldset[1]/ol[1]/li[2]/label[1]/label[1]").click()
        time.sleep(2)
        driver.find_element(By.ID,"attendance_time").clear()
        time.sleep(1)
        driver.find_element(By.ID,"attendance_time").send_keys(time_punchout)
        time.sleep(2)
        driver.find_element(By.ID,"attendance_note").send_keys("")
        time.sleep(2)
        driver.find_element(By.ID,"btnPunch").click()
        time.sleep(3)

        response_title = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[2]/form[1]/fieldset[1]/ol[1]/li[3]/span[2]").text
        
        self.assertEqual(response_title,'Punch out Time Should Be Higher Than Punch in Time')

    def test_C_Attendance_Punch_Out_Success (self):
        driver = self.driver
        driver.find_element(By.ID,"menu_attendance_punchIn").click()
        time.sleep(2)
        driver.find_element(By.ID,"attendance_date").clear()
        time.sleep(1)
        driver.find_element(By.ID,"attendance_date").send_keys(date_today)
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[2]/form[1]/fieldset[1]/ol[1]/li[2]/label[1]/label[1]").click()
        time.sleep(2)
        driver.find_element(By.ID,"attendance_time").clear()
        time.sleep(1)
        driver.find_element(By.ID,"attendance_time").send_keys(time_punchout)
        time.sleep(2)
        driver.find_element(By.ID,"attendance_note").send_keys("")
        time.sleep(2)
        driver.find_element(By.ID,"btnPunch").click()
        time.sleep(3)

        response_title = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/h1[1]").text
        
        self.assertEqual(response_title,'Punch In')
    
    def test_D_Attendance_MyRecords_Found (self):
        driver = self.driver
        driver.find_element(By.ID,"menu_attendance_viewMyAttendanceRecord").click()
        time.sleep(2)
        driver.find_element(By.ID,"attendance_date").clear()
        time.sleep(1)
        driver.find_element(By.ID,"attendance_date").send_keys(date_today)
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/label[1]").click()
        time.sleep(3)
        
        response_title = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]").text
        
        self.assertNotEqual(response_title,'No attendance records to display')

    def test_E_Attendance_MyRecords_NotFound (self):
        driver = self.driver
        driver.find_element(By.ID,"menu_attendance_viewMyAttendanceRecord").click()
        time.sleep(2)
        driver.find_element(By.ID,"attendance_date").clear()
        time.sleep(1)
        driver.find_element(By.ID,"attendance_date").send_keys(date_future)
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[1]/label[1]").click()
        time.sleep(3)
        
        response_title = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[2]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]").text
        
        self.assertEqual(response_title,'No attendance records to display')

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()