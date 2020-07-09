#!/usr/bin/env python3

import pytest


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.headless = True
    return firefox_options
