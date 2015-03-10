#import requests
import urlparse

# r = requests.get("http://example.com/foo/bar")

# print r.status_code
# print r.headers
# print r.content

url = 'http://cbt.com/?number=255715123123&keyword=Custom'
par = urlparse.parse_qs(urlparse.urlparse(url).query)

print par['number'], par['keyword']