from setuptools import setup

setup(name='tap-airtable',
      version='0.0.2',
      description='Singer.io tap for extracting data from the Airtable API',
      author='AIME Mentorinng',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_airtable'],
      install_requires=[
          'backoff==1.8.0',
          'certifi==2018.11.29',
          'chardet==3.0.4',
          'idna==2.7',
          'jsonschema==2.6.0',
          'pendulum==1.2.0',
          'python-dateutil==2.7.5',
          'pytz==2018.4',
          'pytzdata==2018.7',
          'requests==2.20.1',
          'simplejson==3.11.1',
          'singer-python==5.12.1',
          'six==1.11.0',
          'tzlocal==1.5.1',
          'urllib3==1.24.2'
      ],
      entry_points='''
          [console_scripts]
          tap-airtable=tap_airtable:main
      ''',
      packages=['tap_airtable, tap_airtable.airtable'],
      include_package_data=True,
      )
