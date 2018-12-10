
import sys

class MiltError:

	def __init__(self):
		self._prefix = '[pymilt] Error: '

	def lang_unknown(self):
		sys.stderr.write(self._prefix + 'unknown language option. Available options {English | Japanese}.\n')
		sys.exit(-1)	

	def exceeded_code(self):
		sys.stderr.write(self._prefix + 'area code exceeded. {1 < code < 48}\n')
		sys.exit(-1)	
		
		
