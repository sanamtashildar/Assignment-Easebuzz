from pages.locators import PracticePageLocators as loc


class PracticePage:

    def __init__(self, page):
        self.page = page

    def select_radio(self):
        self.page.locator(loc.RADIO_BTN).click()

    def check_checkbox(self):
        self.page.locator(loc.CHECKBOX_OPTION1).check()

    def select_dropdown(self, value):
        self.page.select_option(loc.DROPDOWN, value)

    def trigger_alert(self, name):
        self.page.fill(loc.NAME_INPUT, name)
        self.page.click(loc.ALERT_BTN)

    def select_autocomplete(self, country):
        self.page.fill(loc.AUTOCOMPLETE, country[:3])
        self.page.wait_for_selector(loc.AUTOCOMPLETE_OPTIONS)

        options = self.page.locator(loc.AUTOCOMPLETE_OPTIONS)
        for i in range(options.count()):
            if options.nth(i).inner_text() == country:
                options.nth(i).click()
                break

    def hover_and_click(self):
        self.page.hover(loc.MOUSE_HOVER)
        self.page.click(loc.HOVER_TOP)

    def get_table_row_count(self):
        return self.page.locator(loc.TABLE_ROWS).count()

    def is_radio_selected(self):
        return self.page.locator(loc.RADIO_BTN).is_checked()

    def is_checkbox_checked(self):
        return self.page.locator(loc.CHECKBOX_OPTION1).is_checked()

    def get_dropdown_value(self):
        return self.page.locator(loc.DROPDOWN).input_value()

    def get_autocomplete_value(self):
        return self.page.locator(loc.AUTOCOMPLETE).input_value()