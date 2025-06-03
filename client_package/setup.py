import setuptools
from setuptools import setup


setup(name="client_package_library",
      version="0.7",
      author="william",
      author_email="william.ambrosetti@supis.ch",
      description="a client library for a web package",
      package_dir={"": "."},
      packages=setuptools.find_packages(where="."),
      python_requires=">=3.6",
      )
