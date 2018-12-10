
import sys
sys.path.append("../../")

from pymilt import Milt

if __name__ == "__main__":

	jp_milt = Milt('Japanese') # English or Japanese
	jp_milt.real_estate().interval('20181', '20182')
	cities = jp_milt.real_estate().city(13102)
	print(cities)

