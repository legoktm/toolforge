from setuptools import setup

setup(
    name='toolforge',
    version='4.4.0',
    packages=['toolforge'],
    package_data={'toolforge': ['py.typed']},
    url='https://wikitech.wikimedia.org/wiki/User:Legoktm/toolforge_library',
    license='GPL-3.0+',
    author='Kunal Mehta',
    author_email='legoktm@member.fsf.org',
    description='Small library for common tasks on Wikimedia Toolforge',
    long_description=open('README.rst').read(),
    install_requires=[
        'requests',
        'pymysql<0.10;python_version<"3.5"',
        'pymysql;python_version>="3.5"',
        'typing;python_version<"3.5"'
    ],
    python_requires='>=3.4',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite="tests",
)
