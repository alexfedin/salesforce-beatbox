from setuptools import setup

setup(name='gs-beatbox',
      version='32.1.3',  # be sure to update the version in _beatbox.py too
      package_dir={'': 'src'},
      packages=['beatbox'],
      author="Alex Fedin",
      author_email='alex@getstocks.com',
      description="A Fork of the original beatbox by Simon Fell et al (https://pypi.python.org/pypi/beatbox/32.1)",
      long_description=open('README.txt').read() + "\n" + open('CHANGES.txt').read(),
      license="GNU GENERAL PUBLIC LICENSE Version 2",
      keywords="python salesforce salesforce.com",
      url="http://code.google.com/p/salesforce-beatbox/",
      classifiers=["Development Status :: 5 - Production/Stable"]
      )
