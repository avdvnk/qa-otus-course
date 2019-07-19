from lesson22.client import MyHttpClient

if __name__ == '__main__':
    req_method = "GET"
    req_host = "demo23.opencart.pro"
    req_port = 80
    req_url = "/admin/"
    req_headers = {"Host": "demo23.opencart.pro"}
    client = MyHttpClient()
    client.send_request(req_method, req_host, req_port, req_url, req_headers)
    print("Start line: {}".format(client.get_start_line()))
    print("Headers: {}".format(client.get_headers()))
    print("Body: {}".format(client.get_body()))
    print("Part2:")
    print("Tag list: {}".format(client.get_tag_list()))
    print("Page text: {}".format(client.get_text()))
    print("Most frequent tag: {}".format(client.get_most_frequent_tag()))
    print("Page links: {}".format(client.get_links()))
