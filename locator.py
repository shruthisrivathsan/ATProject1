from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebLocators:
    def __init__(self):
        """this method created to locate the different elements using name, ID, tag name, xpath and CSS-selector inorder to test OrangeHRM
        """
        self.usernameLocator = "username"
        self.passwordLocator = "password"
        self.buttonLocator = "button"
        self.pimLocator = "PIM"
        self.addButtonLocator = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
        self.firstNameLocator = "firstName"
        self.lastNameLocator = "lastName"
        self.saveButtonLocator = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
        self.employeeListLocator = "Employee List"
        self.employeeLocator = "(//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable'])[1]"
        self.middleNameLocator = "middleName"
        self.saveEditButtonLocator = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button"
        self.deleteButtonLocator = "//button[@class='oxd-icon-button oxd-table-cell-action-space'][1]"

    def enterText(self, driver, locator, textValue):
        """ this method is to locate the element using NAME, wait until it is located and enter the username and password"""
        WebDriverWait(driver, 10). until(EC.presence_of_element_located((By.NAME, locator)))
        element = driver.find_element(by=By.NAME, value=locator)
        element.clear()
        element.send_keys(textValue)

    def clickButton(self, driver, locator):
        """ this method is to locate the element using TAG NAME, wait until its located and enter the text """
        driver.find_element(by=By.TAG_NAME, value=locator).click()

    def selectPim(self, driver, locator):
        """ this method is to locate the element using ID, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).click()

    def addEmployeePim(self, driver, locator):
        """ this method is to locate the element using XPATH, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).click()

    def enterEmployeeDetails(self, driver, locator, textValue):
        """ this method is to locate the element using NAME, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, locator)))
        driver.find_element(by=By.NAME, value=locator).send_keys(textValue)

    def saveEmployeeDetails(self, driver, locator):
        """ this method is to locate the element using XPATH, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).click()

    def employeeList(self, driver, locator):
        """ this method is to locate the element using LINKTEXT, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        driver.find_element(by=By.LINK_TEXT, value=locator).click()

    def editEmployee(self, driver, locator):
        """ this method is to locate the element using XPATH, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).click()

    def addMiddleName(self, driver, locator, textValue):
        """ this method is to locate the element using NAME, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, locator)))
        element = driver.find_element(by=By.NAME, value=locator)
        element.clear()
        element.send_keys(textValue)

    def saveChanges(self, driver, locator):
        """ this method is to locate the element using XPATH, wait until its located and enter the text """
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,locator)))
        driver.find_element(by=By.XPATH, value=locator).click()

    def deleteEmployee(self, driver, locator):
        """ this method is to locate the element using XPATH, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).click()

    def comfirmDelete(self, driver, locator):
        """ this method is to locate the element using XPATH, wait until its located and enter the text """
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        driver.find_element(by=By.XPATH, value=locator).click()

    @staticmethod
    def confirmDeleteAlert(driver):
        """ this method is to locate the element using CLASSNAME, wait until its located,
        Find the "Yes, Delete" button using XPATH and return the button element """
        try:
            alert_popup = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-dialog-sheet--gutters")))
            yes_delete_button = WebDriverWait(alert_popup, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[3]/div/div/div/div[3]/button[2]" )))
            return yes_delete_button
        except Exception as e:
            print(f"Error: {e}")
            return None





