import time

from Pages.BasePage import BasePage
from Pages.SendMessageWithExcelPage import SendMessageWithExcelPage
from utils.ExcelHandling import *
import os.path


class SendMessageTest(BasePage):
    def test_SendMessage(self):
        available = SendMessageWithExcelPage(self.driver)
        excel = os.path.abspath('..\TestData\Contract_Number_List.xlsx')
        number = open_and_read_excel_file(excel, "Sheet1", 3)
        for i in range(len(number)):
            available.click_message_icon()
            available.click_search_icon()
            available.type_phone_number(number[i])
            available.click_expected_profile()
            time.sleep(5)

            try:
                if available.is_Displayed():
                    available.type_message("Hi")
                    available.click_send_button()
                    available.click_message_back_button()

            except:
                available.click_popup_ok_button()
                available.click_number_back_button()
