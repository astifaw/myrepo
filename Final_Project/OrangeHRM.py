import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variable
url="http://barru.pythonanywhere.com/daftar"
email_new="tes_002@mailinator.com" # email belum terdaftar
name_new="tes 002" # nama belum terdaftar
email_reg="tes_001@mailinator.com" #email sudah terdaftar
passw="testerjago"

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_A_REG_1_failed_register_with_empty_field(self):
        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"signUp").click()
        time.sleep(3)
        driver.find_element(By.ID,"signup_register").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data, 'Email/Username/Password tidak boleh kosong')
        self.assertEqual(response_message, 'Gagal Registrasi')

    def test_A_REG_2_failed_register_with_registered_email(self):
        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"signUp").click()
        time.sleep(3)
        driver.find_element(By.ID,"name_register").send_keys("tes") # isi nama
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys(email_reg) # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys(passw) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data, 'Email sudah terdaftar, gunakan Email lain')
        self.assertEqual(response_message, 'Gagal Registrasi')

    def test_A_REG_3_success_register(self):
        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"signUp").click()
        time.sleep(3)
        driver.find_element(By.ID,"name_register").send_keys(name_new) # isi nama
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys(email_new) # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys(passw) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data, 'berhasil')
        self.assertEqual(response_message, 'created user!')

    def test_B_LOGIN_1_failed_login_with_empty_email(self):
        
        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys(passw) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data, 'Email tidak valid')
        self.assertEqual(response_message, 'Cek kembali email anda')

    def test_B_LOGIN_2_failed_login_with_empty_password(self):
        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys(email_reg) # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data, "User's not found")
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_B_LOGIN_3_failed_login_with_wrong_password(self):
        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys(email_reg) # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("xxxxxx") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data, "User's not found")
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_B_LOGIN_4_success_login(self): 

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys(email_reg) # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys(passw) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data, 'Welcome tester jago')
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()