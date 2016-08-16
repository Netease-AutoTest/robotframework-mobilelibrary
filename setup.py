#!/usr/bin/env python

import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), 'src'))
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup

setup(setup_requires=['pbr'], pbr=True, package_dir={'': 'src'}, package=["AppiumLibrary"])

execfile(join(dirname(__file__), 'src', 'AppiumLibrary', 'version.py'))

setup(name         = 'robotframework-mobilelibrary',
      version      = VERSION,
      description  = 'app testing library for Robot Framework Extended with AppiumLibrary',
      long_description = open(join(dirname(__file__), 'README.rst')).read(),
      author       = 'Subscription QA',
      author_email = '<longmazhanfeng@gmail.com>',
      url          = 'https://g.hz.netease.com/yixinplusQA/RFUI_Framework/tree/master/Third-Party-Module/MobileLibrary',
      license      = 'Apache License 2.0',
      keywords     = 'robotframework testing testautomation mobile appium webdriver app',
      platforms    = 'any',
      classifiers  = [
                        "Development Status :: 5 - Production/Stable",
                        "License :: OSI Approved :: Apache Software License",
                        "Operating System :: OS Independent",
                        "Programming Language :: Python",
                        "Topic :: Software Development :: Testing"
                     ],
      install_requires = [
                            'images2gif-Pillow >= 0.0.2',
                            'decorator >= 3.3.2',
                            'robotframework >= 2.9.1, <=2.9.2',
                            'docutils >= 0.8.1',
                            'Appium-Python-Client >= 0.5',
                            'selenium >= 2.47.1',
                            'mock >= 1.0.1, <=1.3.0',
                            'sauceclient >= 0.1.0',
                            'pytest-cov >= 1.8.1',
                            'pytest-xdist >= 1.11',
                            'pytest-pythonpath >= 0.4',
                            'aircv >= 1.4.4',
                         ],
      py_modules=['ez_setup'],
      package_dir  = {'' : 'src'},
      packages     = ['AppiumLibrary','AppiumLibrary.keywords','AppiumLibrary.locators',
                      'AppiumLibrary.utils','AppiumLibrary.utils.events'],
      include_package_data = True,
      )
