from setuptools import setup
import sys

depends = ['requests']
if sys.version[0] == '2':
    depends.append('oursql')

setup(
    name='wmflabs',
    version='2.1',
    packages=['wmflabs'],
    url='https://wikitech.wikimedia.org/wiki/User:Legoktm/wmflib',
    license='Public domain',
    author='Kunal Mehta',
    author_email='legoktm@gmail.com',
    description='Small library for common tasks on Wikimedia Labs',
    install_requires=depends,
    test_suite="tests",
)
