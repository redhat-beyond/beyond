#!/usr/bin/env python3

import pytest


def test_title(selenium):
    selenium.get('http://localhost:5000')
    assert selenium.title == 'Baboon'
