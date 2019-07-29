import json
import os
import re
from collections import Counter


class MyParser:

    @staticmethod
    def get_total_requests(file_path, output_file):
        log_files = MyParser._get_files(file_path)
        data = MyParser._get_all_data(log_files).splitlines()
        MyParser._write_to_json([("total_requests", len(data))], output_file)

    @staticmethod
    def get_top_ip(file_path, output_file):
        log_files = MyParser._get_files(file_path)
        data = MyParser._get_all_data(log_files)
        ip_list = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} ", data)
        result = Counter(ip_list)
        MyParser._write_to_json(result.most_common(10), output_file)

    @staticmethod
    def get_requests(request_type, file_path, output_file):
        log_files = MyParser._get_files(file_path)
        data = MyParser._get_all_data(log_files)
        requests = re.findall(r" \"\w+ ".format(request_type), data)
        requests = [item.replace("\"", " ").strip() for item in requests]
        result = Counter(requests)
        MyParser._write_to_json([(request_type, result[request_type])], output_file)

    @staticmethod
    def get_long_requests(file_path, output_file):
        log_files = MyParser._get_files(file_path)
        data = MyParser._get_all_data(log_files)
        expression = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} [- \w\d\[\]/:+\".?=_&]+ \d{3} \d+"
        requests = re.findall(expression, data)
        time_dict = {}
        for request in requests:
            key, value = request.rsplit(" ", 1)
            time_dict[key] = int(value)
        result = sorted(time_dict.items(), key=lambda x: x[1], reverse=True)
        MyParser._write_to_json(result[:10], output_file)

    @staticmethod
    def get_client_error(file_path, output_file):
        log_files = MyParser._get_files(file_path)
        data = MyParser._get_all_data(log_files)
        expression = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} [- \w\d\[\]/:+\".?=_&]+\" 4\d{2}"
        requests = re.findall(expression, data)
        requests = [re.sub(r"\[[\d\w\s/:+\]]+", "", line) for line in requests]
        result = Counter(requests)
        MyParser._write_to_json(result.most_common(10), output_file)

    @staticmethod
    def get_server_error(file_path, output_file):
        log_files = MyParser._get_files(file_path)
        data = MyParser._get_all_data(log_files)
        expression = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} [- \w\d\[\]/:+\".?=_&]+\" 5\d{2}"
        requests = re.findall(expression, data)
        requests = [re.sub(r"\[[\d\w\s/:+\]]+", "", line) for line in requests]
        result = Counter(requests)
        MyParser._write_to_json(result.most_common(10), output_file)

    @staticmethod
    def _get_files(file_path):
        files = os.listdir(file_path)
        result = []
        for file in files:
            if file.split(".")[-1] == "log":
                result.append(file)
        return result

    @staticmethod
    def _get_all_data(files):
        data = ""
        for file in files:
            with open(file, "r") as log:
                data += log.read()
        return data

    @staticmethod
    def _write_to_json(data, output_file):
        with open(output_file, "w") as file:
            json_data = json.dumps(dict(data))
            file.write(json_data)
