
import requests
import json

class ConcreteGeography:

	def __init__(self, root):
		self._root = root

	def city(self, code_area):
		"""
		Description:
			Retruns the cities under the specified area
		"""

		url = self._root + 'CitySearch?area=' + str(code_area)
		r = requests.get(url)
		return json.loads(r.text)
	
