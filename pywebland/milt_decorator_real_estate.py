
from .milt_error import MiltError
from .milt_concrete_real_estate import ConcreteRealEstate

class DecoratorRealEstate:

	def __init__(self, root):

		self._err = MiltError()
		self._real_estate = ConcreteRealEstate()
		self._root = root
		self._from = ''
		self._to = ''

	def interval(self, _from, to):		

		self._from = _from
		self._to = to

	def base(self):
		"""
		Description:
			generate base url
		"""

		url = self._root \
			+ 'TradeListSearch?from=' \
			+ self._from + '&to='\
			+ self._to + '&'

		return url	

	def city(self, code):
		"""
		Description:
			returns real estate transaction information in the specified city code.
		"""

		return self._real_estate.city(self.base() + 'city=' + str(code))

	def prefecture(self, code):
		"""
		Description:
			returns real estate transaction information in the specified area code.
		"""

		if code < 1 and code > 47:
			self._err.exceeded_code()

		return self._real_estate.area(self.base() + 'area=' + str(code))

	def all(self):
		"""
		Description:
			returns real estate transacation information in Japan
		"""
		print("Unavailable")

	def hokkaido(self):
		print("Unavailable")

	def tohoku(self):
		print("Unavailable")

	def kanto(self):
		print("Unavailable")

	def hokuriku(self):
		print("Unavailable")

	def chukyo(self):
		print("Unavailable")

	def kansai(self):
		print("Unavailable")

	def shikoku(self):
		print("Unavailable")

	def kyushu(self):
		print("Unavailable")
