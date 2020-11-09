#!/usr/bin/env python3


def test_title(selenium):
    selenium.get('http://localhost:80')
    assert selenium.title == 'Beyond'
