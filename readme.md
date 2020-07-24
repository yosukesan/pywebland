
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

## Prefectural Code (area)

Table 1: Prefectural Code. Table taken from [1]

| Prefectural Code | JP | EN |
|:---:|:---:|:---:|
|01 | 北海道 |Hokkaido |
|02 | 青森県 |Aomori Prefecture |
|03 | 岩手県 |Iwate Prefecture |
|04 | 宮城県 |Miyagi Prefecture |
|05 | 秋田県 |Akita Prefecture |
|06 | 山形県 |Yamagata Prefecture |
|07 | 福島県 |Fukushima Prefecture |
|08 | 茨城県 |Ibaraki Prefecture |
|09 | 栃木県 |Tochigi Prefecture |
|10 | 群馬県 |Gunma Prefecture |
|11 | 埼玉県 |Saitama Prefectur |
|12 | 千葉県 |Chiba Prefecture |
|13 | 東京都 |Tokyo	|
|14 | 神奈川県|Kanagawa Prefecture |
|15 | 新潟県 |Niigata Prefecture |
|16 | 富山県 |Toyama Prefecture	|
|17 | 石川県 |Ishikawa Prefecture |
|18 | 福井県 |Fukui Prefecture |
|19 | 山梨県 |Yamanashi Prefecture |
|20 | 長野県 |Nagano Prefecture	|
|21 | 岐阜県 |Gifu Prefecture |
|22 | 静岡県 |Shizuoka Prefecture |
|23 | 愛知県 |Aichi Prefecture |
|24 | 三重県 |Mie Prefecture |
|25 | 滋賀県 |Shiga Prefecture |
|26 | 京都府 |Kyoto Prefecture |
|27 | 大阪府 |Osaka Prefecture |
|28 | 兵庫県 |Hyogo Prefecture |
|29 | 奈良県 |Nara Prefecture |
|30 | 和歌山県 |Wakayama Prefecture |
|31 | 鳥取県 |Tottori Prefecture |
|32 | 島根県 |Shimane Prefecture |
|33 | 岡山県 |Okayama Prefecture |
|34 | 広島県 |Hiroshima Prefecture |
|35 | 山口県 |Yamaguchi Prefecture |
|36 | 徳島県 |Tokushima Prefecture |
|37 | 香川県 |Kagawa Prefecture |
|38 | 愛媛県 |Ehime Prefecture |
|39 | 高知県 |Kochi Prefecture |
|40 | 福岡県 |Fukuoka Prefecture |
|41 | 佐賀県 |Saga Prefecture |
|42 | 長崎県 |Nagasaki Prefecture |
|43 | 熊本県 |Kumamoto Prefecture |
|44 | 大分県 |Oita Prefecture |
|45 | 宮崎県 |Miyazaki Prefecture |
|46 | 鹿児島県 |Kagoshima Prefecture |
|47 | 沖縄県 |Okinawa Prefecture |

## Reference
[1] https://www.land.mlit.go.jp/webland/api.html (accessed 2020/07/24)
