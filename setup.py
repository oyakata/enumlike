import os

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    ]

tests_require = [
    ]

entry_points = """
"""

setup(name='enumlike',
      version='0.2',
      description='An enum like object for using django-form-choces.',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "License :: OSI Approved :: MIT License",
      ],
      keywords='',
      author="imagawa_yakata(oyakata)",
      author_email="imagawa.hougikumaru@gmail.com",
      url="https://github.com/oyakata/enumlike",
      license="MIT",
      py_modules=["enumlike"],
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      install_requires=requires,
      test_suite="enumlike",
      entry_points=entry_points,
      )
