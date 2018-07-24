from distutils.core import setup

setup(
	name="oxd-rp-certification-python",
	version="0.0.2",
	author="Brandon Hammond",
	author_email="brandon@gluu.org",
	packages=["oxd-rp-certification-python"],
	scripts=[],
	url="https://oxd.gluu.org",
	license="LICENSE",
	description="A tool to allow OpenID RP Certification testing with oxd server and the OpenID Test Suite",
	long_description=open('README.md').read(),
	install_requires=[
		"configparser >= 3.0.0",
		"flask >= 1.0.0",
		"oxdpython >= 3.1.3",
	],
)
