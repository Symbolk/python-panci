import os
import sys
from setuptools import setup, find_packages

install_requires = ['PyYAML']

version = sys.version_info[:2]

if version < (2,7) or (3,0) <= version <= (3,1):
    install_requires += ['argparse']

this_dir = os.path.dirname(__file__)
long_description = "\n" + open(os.path.join(this_dir, 'README.rst')).read()

setup(
    name='panci',
    version='0.0.0',
    description=('Convert between Travis-CI `.travis.yml` files and Tox `tox.ini` files'),
    long_description=long_description,
    keywords='tox, travis, continuous integration, CI',
    author='Marc Abramowitz',
    author_email='marc@marc-abramowitz.com',
    url='https://github.com/msabramo/panci',
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    test_suite='tests',
    entry_points = """\
      [console_scripts]
      travis2tox = panci.travis2tox:main
      tox2travis = panci.tox2travis:main
    """,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Testing',
        'Natural Language :: English',
        'Intended Audience :: Developers',
    ],
)