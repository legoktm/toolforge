from setuptools import setup

setup(
    name='wmflabs',
    version='3.1.0',
    packages=['wmflabs'],
    url='https://wikitech.wikimedia.org/wiki/User:Legoktm/wmflib',
    license='GPL-3.0+',
    author='Kunal Mehta',
    author_email='legoktm@member.fsf.org',
    description='Small library for common tasks on Wikimedia Labs',
    install_requires=['requests', 'pymysql'],
    test_suite="tests",
)
