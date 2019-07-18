import socket

from lesson22.MyHTMLParser import MyHTMLParser


def send_request(method, host, port, url, headers, body=""):
    request = "{} {} HTTP/1.1\r\n".format(method, url)
    for key, value in headers.items():
        request += "{}: {}\r\n".format(key, value)
    request += "\r\n"
    request += body

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.send(request.encode())
    return sock


def get_response(my_socket):
    result = b""
    buffer = my_socket.recv(4096)
    while len(buffer) > 0:
        result += buffer
        buffer = my_socket.recv(4096)
    return result.decode()


def get_full_info(input_data):
    parser = MyHTMLParser()
    parser.feed(input_data)
    print(parser.get_most_frequent_tag())


if __name__ == '__main__':
    req_method = "GET"
    req_host = "demo23.opencart.pro"
    req_port = 80
    req_url = "/admin/"
    req_headers = {"Host": "demo23.opencart.pro"}
    s = send_request(req_method, req_host, req_port, req_url, req_headers)
    result = get_response(s)
    get_full_info(result)
