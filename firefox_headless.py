#! /usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class firefox_headless():
	
	def __init__(self):

		self.FirefoxBinary = ''
		self.url = ''
		self.status = ''
		self.firefox_path = ''
		return

	def set_options(self, **kwargs):
		return

	def get_headless_url(self, url):

		options = Options()
		options.set_headless(headless=True)
		self.options = options

		if self.firefox_path == '':
			self.firefox_path = '/opt/firefox/firefox'

		self.url = url
		self.binary = FirefoxBinary(self.firefox_path)

		try:
			session = webdriver.Firefox(firefox_options=self.options,firefox_binary=self.binary)
			self.session.get(self.url)
			self.status = True
		 
		except:
			self.status = False
		
		return 

	# def start_session(self, options, firefox_path):
	# 	self.driver = webdriver.Firefox(firefox_options=options,firefox_binary=firefox_path)
	# 	return self.driver

if __name__ == '__main__':

	#run stuff
