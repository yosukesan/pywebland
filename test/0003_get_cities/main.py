
import sys
sys.path.append("../../")

from pymilt import Milt

if __name__ == "__main__":

	jp_milt = Milt('Japanese') # English or Japanese
	cities = jp_milt.geography().city(33)

	for c in cities['data']:
		print(c['id'], c['name'])
