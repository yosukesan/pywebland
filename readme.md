
--------------------------------------------------------------------------------------
pywebland: The API client for Ministry of Land, Infrastructure and Transport of Japan
--------------------------------------------------------------------------------------

# Summary

This is a python3 client implementation for land and estate transation API 
for Minisitry of Land, Infrastructure and Transport of Japan.

The API is available both in English and Japanese

# Usage

## Obtain City Code

* obtain city code in the prefecture.

- following code returns city code in Tokyo in json format.

```
from pywebland import Milt

if __name__ == "__main__":

	jp_milt = Milt('Japanese') # English or Japanese
	cities = jp_milt.geography().city(13)

	for c in cities['data']:
		print(c['id'], c['name'])
```

## Estate Transation Record

* obtain city code in the prefecture.

- following code returns real estate transation record from 2018 Q1 to 2018 Q2 in the specified city (13102)

```
if __name__ == "__main__":

	jp_milt = Milt('Japanese') # English or Japanese
	jp_milt.real_estate().interval('20181', '20182')
	cities = jp_milt.real_estate().city(13102)
	print(cities)
```
