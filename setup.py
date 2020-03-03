## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    package_xml_path='./package.xml',
    packages=['rospy_message_converter'],
    package_dir={'' : 'src'},
)

setup(**d)
