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
url="https://opensource-demo.orangehrmlive.com/index.php/buzz/viewBuzz" #URL langsung ke menu
username="Admin" # username admin
password="admin123" # password admin

class Test_Buzz(unittest.TestCase): 

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

    def test_A_Buzz_Post_Status (self):
        driver = self.driver
        driver.find_element(By.ID,"createPost_content").send_keys("Have a good day everyone....!!!")
        time.sleep(1)
        driver.find_element(By.ID,"postSubmitBtn").click()
        time.sleep(3)
        
        response_name = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[6]/ul[1]/li[1]/div[1]/div[5]/div[1]").text

        self.assertEqual(response_name,'Have a good day everyone....!!!')

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()