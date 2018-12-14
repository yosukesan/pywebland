
from .milt_concrete_geography import ConcreteGeography

class DecoratorGeography:

	def __init__(self, root):

		self._concrete_geography = ConcreteGeography(root)

	def city(self, code_area):
		"""
		Description
			returns set of city name and city code in the specified areal code
		"""

		return self._concrete_geography.city(code_area)	

	def area(self):
		return self._concrete_geography.area()

	def hokkaido(self):
		return self._concrete_geography.hokkaido()

	def tohoku(self):
		return self._concrete_geography.tohoku()

	def kanto(self):
		return self._concrete_geography.kanto()

	def chubu(self):
		return self._concrete_geography.chubu()

	def kansai(self):
		return self._concrete_geography.kansai()

	def chugoku(self):
		return self._concrete_geography.chugoku()

	def shikoku(self):
		return self._concrete_geography.shikoku()

	def kyushu(self):
		return self._concrete_geography.kyushu()

	def okinawa(self):
		return self._concrete_geography.okinawa()
