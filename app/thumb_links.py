import sys
import requests
from bs4 import BeautifulSoup
import urllib2
import re
import json


def get_thumb_links(ig_user):
	profile = "https://www.instagram.com/" + ig_user

	html_page = urllib2.urlopen(profile)
	soup = BeautifulSoup(html_page, "html5lib")

	# get useful json info as a string, remove other javascript stuff like trailing semicolon and variable
	# then convert string to json dictionary
	string_json = soup.body.script.string.split("window._sharedData = ",1)[1][:-1]
	my_json = json.loads(string_json)
	link_num =  len(my_json["entry_data"]["ProfilePage"][0]["user"]["media"]["nodes"])

	thumb_links = []
	for num in range(0, link_num):
	    ig_link = my_json["entry_data"]["ProfilePage"][0]["user"]["media"]["nodes"][num]["thumbnail_src"]
	    thumb_links.append(ig_link)
	return thumb_links

