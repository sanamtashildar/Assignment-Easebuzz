from pages.practice_page import PracticePage


def test_radio_button(page):
    practice = PracticePage(page)
    practice.select_radio()
    assert practice.is_radio_selected()


def test_checkbox(page):
    practice = PracticePage(page)
    practice.check_checkbox()
    assert practice.is_checkbox_checked()


def test_dropdown(page):
    practice = PracticePage(page)
    practice.select_dropdown("option2")
    assert practice.get_dropdown_value() == "option2"


def test_alert(page):
    practice = PracticePage(page)

    page.on("dialog", lambda dialog: dialog.accept())
    practice.trigger_alert("Sanam")


def test_autocomplete(page):
    practice = PracticePage(page)
    practice.select_autocomplete("India")

    assert "India" in practice.get_autocomplete_value()


def test_mouse_hover(page):
    practice = PracticePage(page)
    practice.hover_and_click()


def test_table(page):
    practice = PracticePage(page)
    assert practice.get_table_row_count() > 1