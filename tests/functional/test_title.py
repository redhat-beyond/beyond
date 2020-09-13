#!/usr/bin/env python3


def test_title(selenium):
    selenium.get('http://localhost:5000')
    assert selenium.title == 'Beyond'
