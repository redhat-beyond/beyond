import os

import requests


def test_webserver_response_code():
    response = requests.get("http://localhost:80")
    assert response.status_code == 200


def test_mysql_server_is_running():
    stream = os.popen("mysqladmin status -u root -proot")
    output = stream.read().lower()
    assert ('uptime' in output)
