from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    input_field = (By.ID, "inputText")
    submit_button = (By.ID, "submitBtn")

    def enter_text(self, text):
        self.driver.find_element(*self.input_field).send_keys(text)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()