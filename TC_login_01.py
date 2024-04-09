#import pytest, data and locators
import pytest
from Data import data
from Locators import locator
#common imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Test:
    @pytest.fixture
    def boot(self):
        """ Fixture to set up and quitting the WebDriver instance."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.quit()

    @pytest.mark.html
    def testLogin(self,boot):
        """Test case to verify login functionality using the locators available in the locators file,
            credentials available in the data file and print the result of the test """
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().correctPassword)
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
        assert self.driver.current_url == data.WebData().dashboardURL
        print(f"Successfully logged in with credentials:{data.WebData().username}, {data.WebData().correctPassword}")


if __name__ == "__main__":
    pytest.main()