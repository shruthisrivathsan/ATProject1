class WebData:
    def __init__(self):
        """this method is used to contain url of the website and the dashboard url to test successful log in """
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.dashboardURL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        self.username = "Admin"
        self.correctPassword = "admin123"
        self.incorrectPassword = "invalid password"
        self.employeeFirstName = "Kate"
        self.employeeLastName = "Philip"
        self.middleName ="Alex"