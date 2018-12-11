
import requests
import json

class ConcreteRealEstate:

	def __init__(self):
		pass

	def interval(self):
		pass

	def city(self, url):

		print(url)
		r = requests.get(url)
		return json.loads(r.text)

	def area(self, code):
		pass

