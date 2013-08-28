from distutils.core import setup

long_description = open('README.md').read()

setup(name="python-angellist",
      version="1.0.0",
      py_modules=["angellist"],
      description="Libraries for interacting with the Angellist API",
      author="Kevin Marshall and Zach Goldberg",
      author_email="zach@zachgoldberg.com, info@falicon.com",
      license="WTFPL",
      url="http://github.com/zachgoldberg/AngelList",
      long_description=long_description,
      platforms=["any"],
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development" +
                   " :: Libraries :: Python Modules",
                   ],
      )
