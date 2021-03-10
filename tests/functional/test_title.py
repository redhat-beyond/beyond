#!/usr/bin/env python3

def test_title(selenium):
    selenium.get('http://localhost:5000')
    assert selenium.title == 'Beyond'


def test_contact_page(selenium):
    selenium.get('http://localhost:5000')
    selenium.find_element_by_xpath("//body//a[text()='Contacts']").click()
    body_text = selenium.find_element_by_tag_name("body").text
    assert "CONTACT" in body_text, "'CONTACT' string wasn't found in body text"


def test_cycles_page(selenium):
    selenium.get('http://localhost:5000')
    search_str = 'List of upcoming cycles'
    expected_cycles_url = 'http://localhost:5000/cycles'
    selenium.find_element_by_xpath("//body//a[text()='Cycles']").click()
    body_text = selenium.find_element_by_tag_name("body").text
    assert search_str in body_text, f"'{search_str}' string wasn't found in body text of the 'cycles' page"
    assert selenium.current_url == expected_cycles_url, (
        f"'Cycles' page URL doesn't match expected. Expected: {expected_cycles_url} Actual: {selenium.current_url}"
    )
