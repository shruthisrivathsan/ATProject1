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
    def testLoginIncorrectCred(self,boot):
        """Test case to verify login functionality. """
        self.driver.get(data.WebData().url)
        self.driver.maximize_window()
        locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().incorrectPassword)
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
        assert "dashboard" not in self.driver.current_url
        print(f"Incorrect credentials:{data.WebData().username}, {data.WebData().incorrectPassword}")


if __name__ == "__main__":
    pytest.main()