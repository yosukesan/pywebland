
import sys
sys.path.append("../../")

from pymilt import Milt

if __name__ == "__main__":

	jp_milt = Milt('Japanese') # English or Japanese
	cities = jp_milt.geography().area()
	print(cities)

