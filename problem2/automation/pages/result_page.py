from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    result_text = (By.ID, "resultText")

    def get_result_text(self):
        return self.driver.find_element(*self.result_text).text