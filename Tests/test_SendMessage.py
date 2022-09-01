

from Pages.BasePage import BasePage
from Pages.SendMessagePage import SendMessagePage
 

class SendMessageTest(BasePage):

    def test_SendMessage(self):
        send = SendMessagePage(self.driver)
        send.click_message_icon()
        send.click_search_icon()
        send.type_phone_number("01885931983")
        send.click_expected_profile()
        send.type_message("Hi, Welcome To You From QUPS")
        send.click_send_button()
        send.click_message_back_button()

