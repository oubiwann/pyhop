from setuptools import setup, find_packages

from pyhop import meta


setup(name=meta.display_name,
      version=meta.version,
      description=meta.description,
      author=meta.author,
      author_email=meta.author_email,
      url=meta.url,
      license=meta.license,
      packages=find_packages(),
      long_description=meta.long_description,
      install_requires=meta.requires)
