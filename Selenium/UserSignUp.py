import time
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestSignUp:
    test_ua = ('Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 '
               'Safari/537.36')

    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument(f'--user-agent={test_ua}')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")

    # test_driver = webdriver.Chrome(options=options)
    # solver = RecaptchaSolver(driver=test_driver)

    def setup_method(self, method):
        self.test_driver = webdriver.Chrome()
        self.solver = RecaptchaSolver(driver=self.test_driver)
        self.vars = {}

    def teardown_method(self, method):
        self.test_driver.quit()

    def test_sign(self):
        self.test_driver.get("https://phptravels.net/signup")
        time.sleep(2)
        self.test_driver.set_window_size(1920, 1080)
        time.sleep(2)
        self.test_driver.find_element(By.ID, "firstname").click()
        self.test_driver.find_element(By.ID, "firstname").send_keys("Test")
        time.sleep(1)
        self.test_driver.find_element(By.ID, "last_name").click()
        self.test_driver.find_element(By.ID, "last_name").send_keys("User")
        time.sleep(1)
        self.test_driver.find_element(By.ID, "phone").click()
        self.test_driver.find_element(By.ID, "phone").send_keys("+90 555 4444333")
        time.sleep(1)
        self.test_driver.find_element(By.ID, "user_email").click()
        self.test_driver.find_element(By.ID, "user_email").send_keys("signup5-user@phptravels.com")
        time.sleep(1)
        self.test_driver.find_element(By.ID, "password").click()
        self.test_driver.find_element(By.ID, "password").send_keys("signupuser123")
        time.sleep(1)
        self.test_driver.find_element(By.CSS_SELECTOR, ".filter-option-inner-inner").click()
        time.sleep(1)
        self.test_driver.find_element(By.CSS_SELECTOR, ".bs-searchbox > .form-control").send_keys("Turkey +90")
        time.sleep(1)
        self.test_driver.find_element(By.CSS_SELECTOR, "#bs-select-1-218 strong").click()
        time.sleep(1)
        recaptcha_iframe = self.test_driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
        time.sleep(2)
        self.solver.click_recaptcha_v2(iframe=recaptcha_iframe)
        time.sleep(2)
        self.test_driver.find_element(By.XPATH, '//*[@id="signup"]/div/div/div/div[7]/div/div/div[1]').click()
        time.sleep(2)

if __name__ == "__main__":
    test = TestSignUp()
    test.setup_method(None)
    try:
        test.test_sign()
    finally:
        test.teardown_method(None)