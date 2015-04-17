#import requests
import urlparse

# r = requests.get("http://example.com/foo/bar")

# print r.status_code
# print r.headers
# print r.content
str = "Customs wanatucharge bei kubwa, tunaumia sana."
key,desc = str.split(' ', 1 );

url = 'http://cbt.com/?number=255715123123&keyword='+key+'&description='+desc
par = urlparse.parse_qs(urlparse.urlparse(url).query)

print par['number'], par['keyword'], par['description']