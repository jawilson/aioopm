from setuptools import setup, find_packages


long_description = open('README.md').read()

setup(
    name='aioopm',
    version='0.0.0',
    license='Apache License 2.0',
    url='https://github.com/jawilson/aioopm',
    author='Jeffery Wilson',
    author_email='jeff@jeffalwilson.com',
    description='Python module to fetch data from OPM.',
    packages=['aioopm'],
    zip_safe=True,
    platforms='any',
    install_requires=list(val.strip() for val in open('requirements.txt')),
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
