
import sys
sys.path.append("../../")

from pymilt import Milt

if __name__ == "__main__":

	jp_milt = Milt('Japanese') # English or Japanese

	jp_milt.real_estate().interval('20181', '20182')
	areas = jp_milt.geography().kansai()

	print (areas)

	for a in areas.values(): # for all prefectures
		print(a)
		for cities in jp_milt.geography().city(a)['data']: # for all cities
			print(cities['id'], cities['name'])
			for real_estate in jp_milt.real_estate().city(cities['id'])['data']: # for all real estate
				print(real_estate)
