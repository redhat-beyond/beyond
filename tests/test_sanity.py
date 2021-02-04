import docker
import requests
from pystemd.systemd1 import Unit

WEB_APP_CONTAINER_NAME = 'beyond'


def test_webserver_response_code():
    response = requests.get("http://localhost:5000")
    assert response.status_code == 200


def test_docker_deamon_is_running():
    unit = Unit(b'docker.service')
    unit.load()
    assert unit.Unit.ActiveState == b'active', "Docker deamon is not running"


def test_docker_container_is_running():
    """
    Check that a given container name is running.
    client.containers.list() is similar to 'docker ps'. it returns only running containers by default.
    """
    client = docker.from_env()
    assert WEB_APP_CONTAINER_NAME in [con.name for con in client.containers.list()], (
        f"Container {WEB_APP_CONTAINER_NAME} is not running."
    )
