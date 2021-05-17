
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

	def area(self):
		"""
		Description
			returns area code from 1 to 47
		"""

		areas = {}

		areas.update(self.hokkaido())
		areas.update(self.tohoku())
		areas.update(self.kanto())
		areas.update(self.chubu())
		areas.update(self.kansai())
		areas.update(self.chugoku())
		areas.update(self.shikoku())
		areas.update(self.kyushu())
		areas.update(self.okinawa())

		return areas

	def hokkaido(self):
		"""
		Description
			returns area code in hokkaido
		"""

		areas = {	'hokkaido'	: '01'}

		return areas

	def tohoku(self):
		"""
		Description
			returns area code in tohoku
		"""
		 
		areas = {	 'aomori'	: '02',	
				 	'iwate'		: '03',
				 	'miyagi'	: '04',
				 	'akita'		: '05',
				 	'yamagata'	: '06',
				 	'fukushima'	: '07'}
		return areas

	def kanto(self):
		"""
		Description
			returns area code in kando
		"""

		areas = {	'ibaraki'	: '08',  
				 	'tochigi'	: '09',	
				 	'gumma'		: '10',	
				 	'saitama'	: '11',
				 	'chiba'		: '12',
				 	'toyko'		: '13',
				 	'kanagawa'	: '14'}

		return areas

	def chubu(self):
		"""
		Description
			returns area code in chubu
		"""

		areas = {	'nigata'	: '15',  
					'toyama'	: '16',  
					'ishikawa'	: '17',  
					'fukui'		: '18',
					'yamanashi'	: '19',
					'nagano'	: '20',
					'gifu'		: '21',
					'shizuoka'	: '22',
					'aichi'		: '23',
					'mie'		: '24'}

		return areas

	def kansai(self):
		"""
		Description
			returns area code in kansai
		"""

		areas = {	'shiga'		: '25',  
					'kyoto'		: '26',  
					'osaka'		: '27',  
					'hyogo'		: '28',  
					'nara'		: '29',  
					'wakayama'	: '30'}  
		return areas

	def chugoku(self):
		"""
		Description
			returns area code in chugoku
		"""

		areas = {	'tottori'	: '31',  
					'shimane'	: '32',  
					'okayama'	: '33',  
					'hiroshima'	: '34',  
					'yamaguchi'	: '35'}

		return areas

	def shikoku(self):
		"""
		Description
			returns area code in shikoku
		"""

		areas = {	'tokushima'	: '36',  
					'kagawa'	: '37',  
					'ehime'		: '38',  
					'kochi'		: '39'} 

		return areas

	def kyushu(self):
		"""
		Description
			returns area code in kyushu
		"""

		areas = {	'fukuoka'	: '40',  
					'saga'		: '41',  
					'nagasaki'	: '42',  
					'kumamoto'	: '43',  
					'oita'		: '44',  
					'miyazaki'	: '45',  
					'kagoshima'	: '46'} 
		return areas

	def okinawa(self):
		"""
		Description
			returns area code in okinawa
		"""

		areas = {	'okinawa'	: '47'}

		return areas
