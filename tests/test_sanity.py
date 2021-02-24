import docker
import requests
from pystemd.systemd1 import Unit

CONTAINER_NAMES = ['beyond', 'mariadb']


def test_webserver_response_code():
    response = requests.get("http://localhost:5000")
    assert response.status_code == 200


def test_docker_deamon_is_running():
    unit = Unit(b'docker.service')
    unit.load()
    assert unit.Unit.ActiveState == b'active', "Docker deamon is not running"


def test_docker_container_is_running():
    """
    Check that a given container names are running.
    client.containers.list() is similar to 'docker ps'. it returns only running containers by default.
    """
    client = docker.from_env()
    running_containers = [con.name for con in client.containers.list()]
    assert set(CONTAINER_NAMES).issubset(running_containers), (
        f"Container/s {list(set(CONTAINER_NAMES).difference(running_containers))} is/are not running."
    )
