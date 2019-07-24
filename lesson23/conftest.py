import pytest


def pytest_addoption(parser):
    parser.addoption("--current_ip", action="store", default="192.168.100.5", help="Current IP address")
    parser.addoption("--default_route", action="store", default="192.168.0.254", help="Default route")
    parser.addoption("--cpu_name", action="store", default="Intel(R) Core(TM) i3-4170 CPU @ 3.70GHz",
                     help="Default CPU name")
    parser.addoption("--service_name", action="store", default="ssh", help="Service name")
    parser.addoption("--port_value", action="store", default="22", help="Port value")
    parser.addoption("--port_type", action="store", default="tcp", help="Expected port value")
    parser.addoption("--package_name", action="store", default="iftop", help="Package name")
    parser.addoption("--package_version", action="store", default="1.0~pre4-3", help="Expected package version")
    parser.addoption("--file_list", action="store", default="/home", help="Directory file list")
    parser.addoption("--file_count", action="store", default="2", help="Expected file list value")
    parser.addoption("--core_version", action="store", default="4.15.0-54-generic", help="Expected core version")
    parser.addoption("--current_dir", action="store", default="/qa-otus-course/lesson23",
                     help="Expected current directory")
    parser.addoption("--os_version", action="store", default="16.04", help="Expected OS version")


@pytest.fixture(scope="session")
def current_ip(request):
    return request.config.getoption("current_ip")


@pytest.fixture(scope="session")
def default_route(request):
    return request.config.getoption("default_route")


@pytest.fixture(scope="session")
def cpu_name(request):
    return request.config.getoption("cpu_name")


@pytest.fixture(scope="session")
def service_name(request):
    return request.config.getoption("service_name")


@pytest.fixture(scope="session")
def port_info(request):
    return request.config.getoption("port_value"), request.config.getoption("port_type")


@pytest.fixture(scope="session")
def package_info(request):
    return request.config.getoption("package_name"), request.config.getoption("package_version")


@pytest.fixture(scope="session")
def dir_info(request):
    return request.config.getoption("file_list"), request.config.getoption("file_count")


@pytest.fixture(scope="session")
def core_version(request):
    return request.config.getoption("core_version")


@pytest.fixture(scope="session")
def current_dir(request):
    return request.config.getoption("current_dir")


@pytest.fixture(scope="session")
def os_version(request):
    return request.config.getoption("os_version")
