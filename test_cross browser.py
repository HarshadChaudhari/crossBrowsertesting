from selenium.webdriver.common.by import By

class Test_Credence_002:

    def test_CredKart_Login_008(self, setup):
        driver = setup
        # Go to Url
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credencetest@test.com")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@1234")
        # password
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login TestCase is Passed")
            driver.close()
            assert True
        except:
            print("Login TestCase is Failed")
            driver.close()
            assert False