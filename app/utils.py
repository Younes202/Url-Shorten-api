import base64
import re


class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten_url(self, original_url, domain, custom_name=None):
        unique_id = hash(original_url)
        if custom_name:
            encoded_id = f"{custom_name}_{base64.urlsafe_b64encode(str(unique_id).encode()).decode()[:6]}"
        else:
            encoded_id = base64.urlsafe_b64encode(str(unique_id).encode()).decode()[:6]
        short_url = f"http://{domain}/{encoded_id}"
        self.url_map[short_url] = original_url
        return short_url


def route_url(url, shortener):
    http_pattern = re.compile(r'^https?://')
    if http_pattern.match(url):
        domain_match = re.match(r'^https?://(?:www\.)?(.*?)\..*', url)
        if domain_match:
            domain = domain_match.group(1)
            return shortener.shorten_url(url, domain)
    return None
