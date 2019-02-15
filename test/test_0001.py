
import sys
sys.path.append("../")

from pywebland import Milt

def test_lang():

	en_milt = Milt('English')
	jp_milt = Milt('Japanese')

	assert en_milt.url() == 'http://www.land.mlit.go.jp/webland_english/api/'
	assert jp_milt.url() == 'http://www.land.mlit.go.jp/webland/api/'
