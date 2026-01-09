from automation.utils.driver_setup import get_driver
from automation.pages.home_page import HomePage
from automation.pages.result_page import ResultPage
import pytest

@pytest.mark.xfail(reason="UI elements are assumed as per assignment")
def test_valid_string_output():
    driver = get_driver()
    driver.get("file:///Users/your_path/problem2/automation/demo_app/index.html")

    home = HomePage(driver)
    home.enter_text("abcabcbb")
    home.click_submit()

    result = ResultPage(driver)
    assert result.get_result_text() == "The length of the longest substring without repeating characters is 3"

    driver.quit()