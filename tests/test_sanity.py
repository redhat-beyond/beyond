import os

import requests
from pystemd.systemd1 import Unit


def test_webserver_response_code():
    response = requests.get("http://localhost:5000")
    assert response.status_code == 200


def test_mysql_server_is_running():
    stream = os.popen("mysqladmin status -u root -proot")
    output = stream.read().lower()
    assert ('uptime' in output)


def test_docker_deamon_is_running():
    unit = Unit(b'docker.service')
    unit.load()
    assert unit.Unit.ActiveState == b'active', "Docker deamon is not running"
