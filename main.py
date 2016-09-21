import os
import sys

_packages_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'site-packages'))


def add_py_packages(package_names):
    for item in package_names:
        sys.path.append(os.path.join(_packages_dir, item))

_packages = (
    'markupsafe-0.23-py2.7.egg',
    'werkzeug-0.11.11-py2.7.egg',
    'jinja2-2.8-py2.7.egg',
    'itsdangerous-0.24-py2.7.egg',
    'click-6.6-py2.7.egg',
    'docopt-0.6.2-py2.7.egg',
    'flask-0.11.1-py2.7.egg',
    'markdown-2.6.6-py2.7.egg',
    'path_and_address-2.0.1-py2.7.egg',
    'pygments-2.1.3-py2.7.egg',
    'requests-2.11.1-py2.7.egg'
    )

add_py_packages(_packages)

# Disable SSL warnings
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import grip.command


__author__ = 'hfannar'

grip.command.main(sys.argv[1:])
