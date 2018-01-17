import requests


my_referer = "http://www.sebnorris.com/"
s = requests.Session()
s.headers.update({'referer': my_referer})
s.get("https://igapi.ga/peachy.bunnies/media")

print s
