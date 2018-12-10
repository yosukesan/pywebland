
from .milt_concrete_geography import ConcreteGeography

class DecoratorGeography:

	def __init__(self, root):

		self._concrete_geography = ConcreteGeography(root)

	def city(self, code_area):

		return self._concrete_geography.city(code_area)	
