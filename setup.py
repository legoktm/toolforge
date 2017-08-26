from setuptools import setup

setup(
    name='wmflabs',
    version='3.3.0',
    packages=['wmflabs'],
    url='https://wikitech.wikimedia.org/wiki/User:Legoktm/wmflib',
    license='GPL-3.0+',
    author='Kunal Mehta',
    author_email='legoktm@member.fsf.org',
    description='DEPRECATED: Use "toolforge" package instead',
    install_requires=['toolforge'],
    test_suite="tests",
)
