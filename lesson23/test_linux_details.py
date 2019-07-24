import lesson23.app as functions


def test_ip_addr(current_ip):
    ip_address = functions.get_ip_addr()
    assert ip_address == current_ip


def test_default_route(default_route):
    current_route = functions.get_default_route()
    assert current_route == default_route


def test_cpu_name(cpu_name):
    current_cpu_name = functions.get_cpu_name()
    assert current_cpu_name == cpu_name


def test_process_list():
    process_list = functions.get_process_list()
    assert len(process_list) > 0


def test_network_status():
    total_value = functions.get_network_status()
    assert total_value > 0.0


def test_running_service(service_name):
    status = functions.get_service_status(service_name)
    assert "(running)" in status


def test_tcp_port(port_info):
    port_number = port_info[0]
    port_type = port_info[1]
    current_port_type = functions.get_port_info(port_number)
    assert current_port_type == port_type


def test_package_version(package_info):
    package_name = package_info[0]
    package_version = package_info[1]
    current_package_version = functions.get_package_version(package_name)
    assert current_package_version == package_version


def test_file_list(dir_info):
    dir_path = dir_info[0]
    file_count = int(dir_info[1])
    file_list = functions.get_file_list(dir_path)
    assert len(file_list) == file_count


def test_core_version(core_version):
    current_core_version = functions.get_core_version()
    assert core_version in current_core_version


def test_current_directory(current_dir):
    current_directory = functions.get_current_directory()
    assert current_directory == current_dir


def test_os_version(os_version):
    current_os = functions.get_os_version()
    assert os_version in current_os
