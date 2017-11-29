from setuptools import setup, find_packages

# files = ["src"]
# package_data={'templates':['*'],'static':['*'],'docs':['*'],},
setup(
  name = 'mathviz_hopper',
  packages = ['mathviz_hopper'], # this must be the same as the name above
  package_data = {'mathviz_hopper' : ["src/*", "src/*/*", "src/*/*/*", "src/*/*/*/*", "src/*/*/*/*/*"] },
  version = '0.1',
  description = 'A word vector visualization library',
  author = 'Samuel Helms',
  author_email = 'samuel.helms@yale.edu',
  url = 'https://github.com/samghelms/mathviz', # use the URL to the github repo
  download_url = 'https://github.com/samghelms/mathviz/archive/0.2.tar.gz', # I'll explain this in a second
  # keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)

# from setuptools import setup

# setup(name='funniest',
#       version='0.1',
#       description='The funniest joke in the world',
#       url='http://github.com/storborg/funniest',
#       author='Flying Circus',
#       author_email='flyingcircus@example.com',
#       license='MIT',
#       packages=['funniest'],
#       zip_safe=False)