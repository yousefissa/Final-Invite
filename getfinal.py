from selenium import webdriver
from time import sleep
from random import randint

def voting():
	url = 'referral goes here' # PUT YOUR REFERRAL LINK HERE
	email_prefix = 'tester{}'.format(randint(1,10)) # more unique email prefix
	for i in range(1,1000):
		browser = webdriver.PhantomJS()
		email = '{}+{}@gmail.com'.format(email_prefix, randint(500, 1000000))
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
