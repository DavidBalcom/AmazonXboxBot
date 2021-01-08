

import os
import time
import datetime
import pickle
from contextlib import suppress

import psutil
from selenium import webdriver



target_url = 'https://www.amazon.ca/Microsoft-RRT-00001-Xbox-Series-X/dp/B08H75RTZ8/'  # Xbox Series X... could be used for PS5 too



class XboxPurchasingAgent:

	def __init__(self):
		pass

	def create_driver(self):
		self.driver = webdriver.Chrome('./chromedriver')
		self.driver.get("http://www.amazon.ca")

		# https://stackoverflow.com/questions/15058462/how-to-save-and-load-cookies-using-python-selenium-webdriver
		if not os.path.exists("cookies.pkl"):
			input("\n\n\nLogin to Amazon and then press Enter to continue...\n\n\n")
			pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))

		cookies = pickle.load(open("cookies.pkl", "rb"))
		for cookie in cookies:
			self.driver.add_cookie(cookie)

		self.driver.get(target_url)


	def refresh_and_try_buying(self):
		wait_value = 20  # wait 20 seconds between checking the page

		while True:
			try:
				# add to cart button
				self.driver.find_element_by_xpath('//*[@id="add-to-cart-button"]').click()
				print(datetime.datetime.now().strftime('%m-%d %H:%M:%S'), 'clicked add to cart')
				time.sleep(2)

				# proceed to checkout
				wait_value = 3
				self.driver.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]').click()
				print(datetime.datetime.now().strftime('%m-%d %H:%M:%S'), 'clicked proceed to checkout')
				time.sleep(2)

				# place order
				self.driver.find_element_by_xpath('//*[@id="placeYourOrder"]/span/input').click()
				print(datetime.datetime.now().strftime('%m-%d %H:%M:%S'), 'clicked place order')

				# stop
				break
			
			except:
				time.sleep(wait_value)
				print(datetime.datetime.now().strftime('%m-%d %H:%M:%S'), 'refreshing')
				self.driver.get(target_url)
				time.sleep(2)


	def kill_driver_processes(self):
		for process in psutil.process_iter():
			if process.name() == 'chrome.exe' and '--test-type=webdriver' in process.cmdline():
				with suppress(psutil.NoSuchProcess):
					psutil.Process(process.pid).kill()


	def run(self):

		self.create_driver()

		while True:
			try:
				try:
					self.refresh_and_try_buying()
				except Exception as e:
					# self.driver becomes disconnected from chrome window sometimes - kill old window and start new driver
					print(e)
					self.kill_driver_processes()

					self.run()
			except Exception as e:
				import pdb; pdb.set_trace()



if __name__ == '__main__':
	xboxPurchasingAgent = XboxPurchasingAgent()
	xboxPurchasingAgent.run()

