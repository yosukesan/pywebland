
import setuptools

with open ("readme.md", "r") as fh:
	long_description = fh.read()

setuptools.setup (
	name = 'pywebland',
	version = '0.1',
	author = 'Yosuke OTSUKI',
	author_email = 'y.otsuki30@gmail.com',
	decription = 'The API client for webland ,real estate database, \
					by Ministry of Land, Infrastructure and Transport of Japan',
	long_description = long_description, 
	long_description_content_typ = "text/markdown",
	url = 'https://github.com/yosukesan/pywebland',
	license = 'python-2.0',
	packages = setuptools.find_packages(exclude=('test')),
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI APPROVED :: Python 2.0 License",
		"Operating System :: OS Independent",
	],
)
