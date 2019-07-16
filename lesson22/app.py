import socket


def send_request(method, host, port, url, headers, body=""):
    request = "{} {}/{} HTTP/1.1\n".format(method, host, url)
    for key, value in headers.items():
        request += "{}: {}\n".format(key, value)
    request += "\n{}".format(body)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.send(request.encode())
    return sock


def get_response(my_socket):
    result = ""
    part = my_socket.recv(4096)
    while len(part) > 0:
        result += part
        part = my_socket.recv(4096)
    return result


if __name__ == '__main__':
    req_method = "GET"
    req_host = "demo23.opencart.pro"
    req_port = 80
    req_url = "admin/"
    req_headers = {"Host": "demo23.opencart.pro",
                   "Connection": "keep-alive"}
    s = send_request(req_method, req_host, req_port, req_url, req_headers)
    print(get_response(s))
