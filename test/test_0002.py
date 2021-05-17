
import sys
sys.path.append("../")

from pywebland import Milt

def test_administrative_districtes():
	
	jp_milt = Milt('English') # English or Japanese

	hokkaido = jp_milt.geography().hokkaido()
	assert hokkaido['hokkaido'] == '01'

	tohoku = jp_milt.geography().tohoku()
	assert tohoku['akita']		== '05'
	assert tohoku['aomori']		== '02'
	assert tohoku['iwate']		== '03'
	assert tohoku['yamagata']	== '06'
	assert tohoku['miyagi']		== '04'
	assert tohoku['fukushima']	== '07'

	kanto = jp_milt.geography().kanto()
	assert kanto['kanagawa']	== '14'
	assert kanto['saitama']		== '11'
	assert kanto['gumma']		== '10'
	assert kanto['chiba']		== '12'
	assert kanto['toyko']		== '13'
	assert kanto['ibaraki']		== '08'
	assert kanto['tochigi']		== '09'

	chubu = jp_milt.geography().chubu()
	assert chubu['yamanashi']	== '19'
	assert chubu['toyama']		== '16'
	assert chubu['aichi']		== '23'
	assert chubu['nagano']		== '20'
	assert chubu['ishikawa']	== '17'
	assert chubu['nigata']		== '15'
	assert chubu['mie']			== '24'
	assert chubu['fukui']		== '18'
	assert chubu['gifu']		== '21'
	assert chubu['shizuoka']	== '22'

	kansai = jp_milt.geography().kansai()
	assert kansai['shiga']		== '25'
	assert kansai['nara']		== '29'
	assert kansai['hyogo']		== '28'
	assert kansai['osaka']		== '27'
	assert kansai['kyoto']		== '26'
	assert kansai['wakayama']	== '30'


	chugoku = jp_milt.geography().chugoku()
	assert chugoku['okayama']	== '33'
	assert chugoku['hiroshima']	== '34'
	assert chugoku['yamaguchi']	== '35'
	assert chugoku['tottori']	== '31'
	assert chugoku['shimane']	== '32'

	shikoku = jp_milt.geography().shikoku()
	assert shikoku['ehime']		== '38'
	assert shikoku['kochi']		== '39'
	assert shikoku['tokushima']	== '36'
	assert shikoku['kagawa']	== '37'

	kyushu = jp_milt.geography().kyushu()
	assert kyushu['kumamoto']	== '43'
	assert kyushu['kagoshima']	== '46'
	assert kyushu['saga']		== '41'
	assert kyushu['miyazaki']	== '45'
	assert kyushu['fukuoka']	== '40'
	assert kyushu['nagasaki']	== '42'
	assert kyushu['oita']		== '44'

	okinawa = jp_milt.geography().okinawa()
	assert okinawa['okinawa']	== '47'
