#!/usr/bin/env python3

def test_title(selenium):
    selenium.get('http://localhost:5000')
    assert selenium.title == 'Beyond'


def test_contact_page(selenium):
    selenium.get('http://localhost:5000')
    selenium.find_element_by_xpath("//body//a[text()='Contacts']").click()
    body_text = selenium.find_element_by_tag_name("body").text
    assert "CONTACT" in body_text, "'CONTACT' string wasn't found in body text"
