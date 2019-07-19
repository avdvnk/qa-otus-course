import socket

from lesson22.MyHTMLParser import MyHTMLParser


class MyHttpClient:

    def __init__(self):
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.body = None
        self.headers = None
        self.start_line = None

    def send_request(self, method, host, port, url, headers, body=""):
        request = "{} {} HTTP/1.1\r\n".format(method, url)
        for key, value in headers.items():
            request += "{}: {}\r\n".format(key, value)
        request += "\r\n"
        request += body
        self.my_socket.connect((host, port))
        self.my_socket.send(request.encode())
        self.__get_response()

    def __get_response(self):
        result = b""
        buffer = self.my_socket.recv(4096)
        while len(buffer) > 0:
            result += buffer
            buffer = self.my_socket.recv(4096)
        normalize_form = result.decode()
        normalize_form = "".join((line + "\n") for line in normalize_form.splitlines())
        response_head, response_body = normalize_form.split("\n\n", 1)
        response_head = response_head.splitlines()
        self.start_line = response_head[0]
        self.headers = dict(head.split(":", 1) for head in response_head[1:])
        self.body = response_body

    def get_tag_list(self):
        parser = MyHTMLParser()
        parser.feed(self.body)
        result = []
        for tag in parser.get_tags():
            result.append(tag)
        return result

    def get_text(self):
        parser = MyHTMLParser()
        parser.feed(self.body)
        return parser.get_text()

    def get_most_frequent_tag(self):
        parser = MyHTMLParser()
        parser.feed(self.body)
        return parser.get_tags().most_common(1)[0]

    def get_links(self):
        parser = MyHTMLParser()
        parser.feed(self.body)
        return parser.get_links()

    def get_start_line(self):
        return self.start_line

    def get_headers(self):
        return self.headers

    def get_body(self):
        return self.body
