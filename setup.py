from distutils.core import setup

setup(name='tinyfeedback',
      version='0.3.0',
      author='Zach Steindler',
      author_email='steiza@gmail.com',
      url='https://github.com/steiza/tinyfeedback',
      description="A simple graphing web-based dashboard",
      long_description="""\
tinyfeedback is a ridiculously simple way for you to see trends in whatever you are monitoring. You do an HTTP POST to put data in, and you point and click in the web interface to make some graphs. Yay!""",
      keywords='dashboard, web, graph, metrics',
      classifiers=['Programming Language :: Python', 'License :: OSI Approved :: MIT License'], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      license='MIT',
      packages=['tinyfeedback'],
      scripts=['bin/tinyfeedback', 'bin/tinyfeedback-ctl'],
      package_data={'tinyfeedback': ['static/*/*', 'templates/*']},
      install_requires=['twisted', 'txroutes', 'txredisapi', 'mako', 'simplejson',]
      )
