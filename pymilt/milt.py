
from .milt_decorator_geography import DecoratorGeography
from .milt_decorator_real_estate import DecoratorRealEstate
from .milt_concrete import MiltConcrete

class Milt:

	def __init__(self, lang):

		self._milt_concrete = MiltConcrete(lang)
		self._geography = DecoratorGeography(self._milt_concrete.url())
		self._real_estate = DecoratorRealEstate(self._milt_concrete.url())

	def geography(self):
		return self._geography

	def real_estate(self):
		return self._real_estate
		
