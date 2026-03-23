from pages.locators import PracticePageLocators


class PracticePage:

    def __init__(self, page):
        self.page = page

    def select_radio(self):
        self.page.locator(PracticePageLocators.RADIO_BTN).click()

    def check_checkbox(self):
        self.page.locator(PracticePageLocators.CHECKBOX_OPTION1).check()

    def select_dropdown(self, value):
        self.page.select_option(PracticePageLocators.DROPDOWN, value)

    def trigger_alert(self, name):
        self.page.fill(PracticePageLocators.NAME_INPUT, name)
        self.page.click(PracticePageLocators.ALERT_BTN)

    def hover_and_click(self):
        self.page.hover(PracticePageLocators.MOUSE_HOVER)
        self.page.click(PracticePageLocators.HOVER_TOP)

    def is_radio_selected(self):
        return self.page.locator(PracticePageLocators.RADIO_BTN).is_checked()

    def is_checkbox_checked(self):
        return self.page.locator(PracticePageLocators.CHECKBOX_OPTION1).is_checked()

    def get_dropdown_value(self):
        return self.page.locator(PracticePageLocators.DROPDOWN).input_value()
