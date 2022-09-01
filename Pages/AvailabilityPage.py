import time
from Locators.Locators import ViberLocators
from Pages.HomePage import HomePage


class AvailabilityPage(HomePage):

    def __init__(self, driver: object) -> object:
        self.locator = ViberLocators
        self.driver = driver
        super(AvailabilityPage, self).__init__(driver)


    def click_message_icon(self):
        self.find_element(*self.locator.messageIcon).click()
        time.sleep(2)


    def click_search_icon(self):
        self.find_element(*self.locator.searchIcon).click()
        time.sleep(2)
        self.find_element(*self.locator.typeNumberTextBox).click()

    def type_phone_number(self, number):
        self.find_element(*self.locator.typeNumberTextBox).send_keys(number)
        time.sleep(2)

    def click_expected_profile(self):
        self.find_element(*self.locator.expectedProfile).click()
        time.sleep(2)

    def is_Displayed(self):
        return self.find_element(*self.locator.typeMessageTextbox).is_displayed()

    def is_Displayed_ok(self):
        return self.find_element(*self.locator.popUpOkButton).is_displayed()

    def get_text_rowStatus(self):
        text = self.find_element(*self.locator.popUpOkButton).text
        return text

    def type_message(self, message):
        self.find_element(*self.locator.typeMessageTextbox).send_keys(message)
        time.sleep(2)

    def click_send_button(self):
        self.find_element(*self.locator.sendButton).click()
        time.sleep(2)

    def click_message_back_button(self):
        self.find_element(*self.locator.messageBackArrowIcon).click()
        time.sleep(2)

    def click_number_back_button(self):
        self.find_element(*self.locator.numberBackArrowIcon).click()
        time.sleep(2)

    def click_popup_ok_button(self):
        self.find_element(*self.locator.popUpOkButton).click()
        time.sleep(2)


