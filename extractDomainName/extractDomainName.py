# importing `urlparse` from `urllib.parse` module
# Its used to parse the given url
from urllib.parse import urlparse

def domain_name(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split('.')[-2] 
    return domain

print(domain_name('http://github.com/carbonfive/raygun')) # github
