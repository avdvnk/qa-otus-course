from collections import Counter
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.tags = Counter()
        self.text = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        self.tags[tag] += 1
        for attr in attrs:
            if attr[0] == "href":
                self.links.append(attr[1])
            if tag == "img" and attr[0] == "src":
                self.links.append(attr[1])

    def handle_data(self, data):
        strip_data = data.strip()
        if strip_data != "":
            self.text.append(strip_data)

    def get_text(self):
        return self.text

    def get_tags(self):
        return self.tags

    def get_links(self):
        return self.links
