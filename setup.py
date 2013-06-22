from setuptools import setup
import sys

if sys.version[0] == '2':
    depends = ['oursql']
else:
    depends = []


setup(
    name='wmflabs',
    version='1.0',
    packages=['wmflabs'],
    url='https://github.com/legoktm/wmflabs-lib',
    license='Public domain',
    author='Kunal Mehta',
    author_email='legoktm@gmail.com',
    description='Small library for common tasks on Wikimedia Labs',
    install_requires=depends,
    test_suite="tests",
)
