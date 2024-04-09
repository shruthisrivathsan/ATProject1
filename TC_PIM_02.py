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
    def testeditEmployeePim(self, boot):
        """Test case to set up to log into the website using the username and password, edit an employee's name,
        save it and print the successful edit in the PIM module """
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().correctPassword)
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
        assert self.driver.current_url == data.WebData().dashboardURL
        print("Successfully logged in")
        try:
            locator.WebLocators().selectPim(self.driver, locator.WebLocators().pimLocator) # select PIM module
            locator.WebLocators().employeeList(self.driver, locator.WebLocators().employeeListLocator) #select employeelist
            locator.WebLocators().editEmployee(self.driver, locator.WebLocators().employeeLocator) #select the employee to edit
            locator.WebLocators().addMiddleName(self.driver, locator.WebLocators().middleNameLocator, data.WebData().middleName) #enter middle name
            locator.WebLocators().saveChanges(self.driver, locator.WebLocators().saveEditButtonLocator) # click on save button
            print("Changes to Employee successfully saved in PIM!")
        except NoSuchElementException as e:
            print(f"Error!{e}")

if __name__ == "__main__":
    pytest.main()