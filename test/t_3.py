import urllib 
import urllib2 
url = 'http://hardware-104.view.sitestar.cn/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
  
values = {'name' : 'Michael Foord', 
          'location' : 'pythontab', 
          'language' : 'Python' } 
headers = { 'User-Agent' : user_agent } 
data = urllib.urlencode(values) 
req = urllib2.Request(url, data, headers) 
response = urllib2.urlopen(req) 
the_page = response.read()
print(the_page)