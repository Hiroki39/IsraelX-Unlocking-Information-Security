from urllib.parse import urlparse


def parse_url(url):
    parsed = urlparse(url)
    return parsed.scheme, parsed.netloc, parsed.path


print(parse_url("http://www.google.com/search"))
