from setuptools import setup

setup(
    name='toolforge',
    version='4.2.0',
    packages=['toolforge'],
    url='https://wikitech.wikimedia.org/wiki/User:Legoktm/toolforge_library',
    license='GPL-3.0+',
    author='Kunal Mehta',
    author_email='legoktm@member.fsf.org',
    description='Small library for common tasks on Wikimedia Toolforge',
    install_requires=[
        'requests',
        'pymysql',
        'typing;python_version<"3.5"'
    ],
    test_suite="tests",
)
