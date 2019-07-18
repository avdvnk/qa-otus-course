from collections import Counter
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.tags = Counter()

    def handle_starttag(self, tag, attrs):
        self.tags[tag] += 1
        print("Tag: {}".format(tag))

        for attr in attrs:
            if attr[0] == "href":
                print("\tSource: {}".format(attr))
            if tag == "img" and attr[0] == "src":
                print("\tSource: {}".format(attr))

    def handle_data(self, data):
        print("\tData: {}".format(data))

    def get_most_frequent_tag(self):
        return self.tags.most_common(1)
