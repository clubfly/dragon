#!/usr/bin/env python
import sys
from distutils.core import setup
from oplinkdragon import __version__
 
if sys.version_info < (2, 7):
    error = "ERROR: sheep requires Python Version 2.7 ...exiting."
    print >> sys.stderr, error
    sys.exit(1)

def setup_package():
    setup(
        name='oplink-dragon',
        version='0.0.1',
        description='webstore',
        author = "Henry Wang",
        author_email = "henrywang@oplink.com.tw",
        packages=['oplinkdragon',
                  'oplinkdragon.method',
                  'oplinkdragon.model',
                  'oplinkdragon.lib'],
        data_files=[('/etc/init', ['init/oplinkdragon.conf']),
                    ('/etc/oplink/dragon', ['conf/DatabaseList.conf',
                                            'conf/default.conf',
                                            'conf/MethodList.conf'])],
        scripts=['scripts/oplinkdragon', 'scripts/oplinkconfigcheck'],
        install_requires=[
          'MySQL-python',
          'bottle',
          'simplejson',
          'pylibmc',
          'pycurl'
        ]
    )

if __name__ == '__main__':
    setup_package()
