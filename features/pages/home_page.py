from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(Browser):
    # Locators
    LOGIN_BTN = "//*[@id='about_8tracks_splash']/div[1]/div/div[2]/div[1]/a[1]"
    USERNAME_FIELD = "//*[@id='login']"
    PASSWD_FIELD = "//*[@id='password']"
    SUBMIT_BUTTON = "//*[@id='login_form']/div/div[4]/input"
    SUCCESSFULL_MSG = "//li[contains(text(), 'Login was unsuccessful')]"

    def fill(self, text, *locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, *locator)))
        element.send_keys(text)

    def click_element(self, *locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, *locator)))
        element.click()

    def navigate(self, url):
        self.driver.get(url)

    def assert_elementText(self, msg, *locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, *locator)))
        assert element.text, msg
