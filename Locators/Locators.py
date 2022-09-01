from selenium.webdriver.common.by import By


class ViberLocators():
    messageIcon = (By.ID, 'com.viber.voip:id/fab_container')
    searchIcon = (By.ID, 'com.viber.voip:id/menu_search')
    typeNumberTextBox = (By.ID, 'com.viber.voip:id/search_src_text')
    expectedProfile = (By.ID, 'com.viber.voip:id/new_num_layout')

    typeMessageTextbox = (By.ID, 'com.viber.voip:id/send_text')
    sendButton = (By.ID, 'com.viber.voip:id/btn_send')
    messageBackArrowIcon = (By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')

    popUpOkButton = (By.ID, 'android:id/button1')
    numberBackArrowIcon = (By.XPATH, '//android.widget.ImageButton[@content-desc="Collapse"]')
