## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['biotac_log_parser'],
    package_dir={'': 'src'},
    requires=['rospy'],
    scripts=['scripts/parse_log_hdf5.py', 'scripts/parse_log_json.py', 'scripts/parse_log_pytable.py']
)

setup(**setup_args)
