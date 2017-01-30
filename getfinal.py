from selenium import webdriver
from time import sleep
import random

def voting():
	url = 'referral goes here' # PUT YOUR REFERRAL LINK HERE
	email_prefix = 'tester'
	for i in range(1,1000):
		browser = webdriver.PhantomJS()
		email = '{}+{}@gmail.com'.format(email_prefix, random.randint(500, 1000000))
		browser.get(url)
		try:
			browser.find_element_by_xpath('//*[@id="email"]').send_keys(email)
			browser.find_element_by_xpath('//*[@id="signup-form"]/fieldset/div/button').click()
			print('Registered an account.')
		except:
			print('Closing and trying again.')
		browser.close()

if __name__ == '__main__':
	voting()
