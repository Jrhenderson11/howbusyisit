import re
import sys
import optparse
import urllib2
import datetime
from email import Encoders
from bs4 import BeautifulSoup
from datetime import timedelta

#tower of London
#https://www.google.co.uk/maps/place/Tower+of+London/@51.5080618,-0.075971,170m/data=!3m1!1e3!4m5!3m4!1s0x48760349331f38dd:0xa8bf49dde1d56467!8m2!3d51.5081123!4d-0.0759494

bookmarks = {}

def get_data(url):
	
	page = BeautifulSoup(urllib2.urlopen(url), 'html.parser')

	#class results
	#id dayOfWeek
	day =  page.find("span", {"id":"dayOfWeek"})
	return

#bookmarks

def show_bookmarks():
	for place in bookmarks:
		print place[1]
	return

def add_to_bookmarks_interactive():
	print "enter bookmark name:"
	name = raw_input()
	#check not already exists
	while (name in bookmarks):
	 	print name + "already in bookmarks\nenter bookmark name:"
		name = raw_input()
	print "enter url:"
	url = raw_input()
	add_to_bookmarks(name, url)

def add_to_bookmarks(name, url):
	if (name in bookmarks):
		print (name + " already in bookmarks")
		return false

	bookmarks[name] = url
	print name + " successfully added to bookmarks"
	return true

#file handling
def load_places(fname):
	file = open(fname)
	#file.write(bookmarks)
	file.close()
	return

def save_places():
	fname = "bookmarks.txt"
	print "enter file to save bookmarks to: (default bookmarks.txt)"
	intext = raw_input()
	if (intext!=""):
		fname = intext
	file = open(fname)
	file.write(bookmarks)
	file.close()

	return


