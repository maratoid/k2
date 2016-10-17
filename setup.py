from setuptools import setup

setup(
  name='k2cli',
  version='1.0',
  description='k2 command line interface',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: Apache 2 Licence',
    'Programming Language :: Python :: 2.7',
    'Topic :: Cloud computing :: Kubernetes',
  ],
  packages=['k2cli'],
  install_requires=[
    'click',
    'ansible',
    'boto',
    'netaddr'
  ],
  entry_points={
    'console_scripts': ['k2cli=k2cli.k2cli:cli'],
  },
  include_package_data=True,
  zip_safe=False
)