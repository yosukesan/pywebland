
from .milt_error import MiltError

class MiltConcrete:

	def __init__(self, lang):

		err = MiltError()

		if lang == 'English':
			sub_dir = 'webland_english'
		elif lang == 'Japanese':
			sub_dir = 'webland'
		else:
			err.lang_unknown()

		self._root_url = 'https://www.land.mlit.go.jp/' \
					   + sub_dir \
					   + '/api/'

	def url(self):
		return self._root_url
