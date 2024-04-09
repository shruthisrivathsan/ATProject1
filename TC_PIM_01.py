#import pytest, data and locators
import pytest
from Data import data
from Locators import locator
#common imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

class Test:
    @pytest.fixture
    def boot(self):
        """ Fixture to set up and quitting the WebDriver instance."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.quit()

    @pytest.mark.html
    def testLogin(self,boot):
        """Set up to log into the website using the username and password"""
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().correctPassword)
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
        assert self.driver.current_url == data.WebData().dashboardURL
        print("Successfully logged in")
        try:
            locator.WebLocators().selectPim(self.driver, locator.WebLocators().pimLocator) # select PIM module
            locator.WebLocators().addEmployeePim(self.driver,locator.WebLocators().addButtonLocator) # click on ADD button
            locator.WebLocators().enterEmployeeDetails(self.driver, locator.WebLocators().firstNameLocator, data.WebData().employeeFirstName) # enter first name
            locator.WebLocators().enterEmployeeDetails(self.driver, locator.WebLocators().lastNameLocator, data.WebData().employeeLastName) # enter last name
            locator.WebLocators().saveEmployeeDetails(self.driver, locator.WebLocators().saveButtonLocator) #click save to save the details
            print(f"New employee {data.WebData().employeeFirstName} {data.WebData().employeeLastName} successfully added!")
        except NoSuchElementException as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    pytest.main()