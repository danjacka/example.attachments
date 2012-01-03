from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='example.attachments',
      version=version,
      description="Display page attachments in Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Dan Jacka',
      author_email='danjacka@gmail.com',
      url='https://github.com/danjacka/example.attachments',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['example'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
      ],
      extras_require={
          'test': [ 'plone.app.testing',],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
