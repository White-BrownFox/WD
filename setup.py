
from setuptools import setup

setup(name='wdpassport_utils',
      version='0.2',
      description='WD My Passport Drive Hardware Encryption Utility for Linux',
      url='https://github.com/0-duke/wdpassport-utils',
      author='0-duke, crypto-universe, JoshData',
      license='GPLv2',
      install_requires=[
        'pyudev',
      ],
      scripts=['wdpassport-utils.py'],
      )
