
class LoginPage:
    textbox_username_id= "Email"
    textbox_password_id= "Password"
    button_login_xpath= "//input[@class='button-1 login-button']"
    link_logout_linktext = "/html/body/div[3]/div[1]/div/div/ul/li[3]/a"

    def __init__(self,driver):
        self.driver=driver


    # actions methods
    def setUserName(self,username):
            self.driver.find_element_by_id(self.textbox_username_id).clear()
            self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
            self.driver.find_element_by_id(self.textbox_password_id).clear()
            self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
            self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
            self.driver.find_element_by_xpath(self.link_logout_linktext).click()