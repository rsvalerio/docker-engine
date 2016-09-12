# running the tests: testinfra --connection=ssh --ssh-config=./ssh_config --hosts=localhost

import pytest


@pytest.mark.parametrize("pkg", ["docker-engine"])
def test_packages(Package, pkg):
    assert Package(pkg).is_installed
    # assert Package(name).version.startswith(version)

def test_docker_running_and_enabled(Service):
    docker = Service("docker")
    assert docker.is_running
    assert docker.is_enabled