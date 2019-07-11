import os

import pytest
from pip._internal.utils.misc import get_installed_distributions


@pytest.mark.usefixtures("installed packages")
@pytest.fixture(scope="session", autouse=True)
def add_package_list_to_report(request):
    packages = ""
    for package in get_installed_distributions(local_only=True):
        str_variable = package.key + ":" + package.version + "\n"
        packages += str_variable
    request.config._metadata.update(
        {"packages": packages}
    )
    yield


@pytest.mark.usefixtures("environment info")
@pytest.fixture(scope="session", autouse=True)
def add_env_variables_to_report(request):
    variables = os.environ["PATH"]
    request.config._metadata.update(
        {"variables": variables}
    )
