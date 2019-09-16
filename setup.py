from setuptools import setup, find_packages
# Usage: [sudo] pip install --process-dependency-links .
setup(name='jiralib',
      version='0.0.2',
      packages=find_packages(),
      install_requires=['requests'],
      zip_safe=False)

