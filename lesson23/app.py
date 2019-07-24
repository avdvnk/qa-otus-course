import os
import re
import subprocess

SUDO_PASS = "sudopassword"


def get_ip_addr():
    interface = subprocess.getoutput("ifconfig -a | grep 'inet addr'").strip().splitlines()[0]
    dict_interface = dict(item.split(":") for item in interface.split("  "))
    return dict_interface.get("inet addr", None)


def get_default_route():
    return subprocess.getoutput("ip r | grep default").split()[2]


def get_cpu_name():
    output = subprocess.getoutput("lscpu").splitlines()
    normal_form = []
    for item in output:
        normal_form.append("{}:{}".format(item.split(":")[0], item.split(":")[1].strip()))
    cpu_info = dict(item.split(":") for item in normal_form)
    return cpu_info.get("Model name")


def get_process_list():
    return subprocess.getoutput("ps a").splitlines()[1:]


def get_network_status():
    command = "sudo -S iftop -t -s 1"
    password = subprocess.Popen(["echo", SUDO_PASS], stdout=subprocess.PIPE)
    total_line = ""
    iftop = subprocess.Popen(command.split(), stdin=password.stdout, stdout=subprocess.PIPE)
    output = iftop.stdout.read().decode().splitlines()
    for line in output:
        if "Cumulative" in line:
            total_line = line
    total_value = total_line.split()[-1]
    total_value = re.findall("\d+\,\d+", total_value)[0].replace(",", ".")
    return float(total_value)


def get_service_status(service_name):
    output = subprocess.Popen("service {} status".format(service_name), shell=True, stdout=subprocess.PIPE)
    output = output.stdout.read().decode().splitlines()
    for line in output:
        if "Active" in line:
            return line.strip()


def get_port_info(port_number):
    output = subprocess.Popen("netstat -tulpn | grep LISTEN", shell=True, stdout=subprocess.PIPE)
    output_lines = output.stdout.read().decode().splitlines()
    for line in output_lines:
        port = line.split()[3].strip().split(":")[1]
        if port == port_number:
            return line.split()[0].strip()


def get_package_version(package_name):
    output = subprocess.Popen("apt-cache policy {}".format(package_name), shell=True, stdout=subprocess.PIPE)
    output_result = output.stdout.read().decode().splitlines()
    for line in output_result:
        if "Установлен" in line:
            version = line.split(":")[1].strip()
            return version


def get_file_list(dir_path):
    output = subprocess.Popen("ls {}".format(dir_path), shell=True, stdout=subprocess.PIPE)
    file_list = output.stdout.read().decode().splitlines()
    return file_list


def get_current_directory():
    return os.getcwd()


def get_core_version():
    return subprocess.Popen("cat /proc/version", shell=True, stdout=subprocess.PIPE).stdout.read().decode()


def get_os_version():
    return subprocess.Popen("cat /etc/issue", shell=True, stdout=subprocess.PIPE).stdout.read().decode()
