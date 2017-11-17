from __future__ import print_function
from setuptools import setup, find_packages
import io

import deploud

def read(*filenames, **kwargs):
    """Read and merge content of several files"""
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as infile:
            buf.append(infile.read())
    return sep.join(buf)

setup(
    name='ml_deploud',
    version=deploud.__version__,
    url='https://github.com/mattsunsjf/ml-deploud/',
    license='Apache Software License',
    author='Matt Sun',
    author_email='sjf.matt@gmail.com',
    description='ML Deploud',
    long_description=read('README.md'),
    packages=find_packages(),
    install_requires=[
        'requests>=2.8.0',
        'click'
    ],
    include_package_data=True,
    platforms='any',
    setup_requires=['pytest-runner'],
    #tests_require=['pytest'],
    classifiers=['Programming Language :: Python', \
        'Development Status :: 1 - Alpha', \
        'Natural Language :: English', \
        'Environment :: Console', \
        'Intended Audience :: Developers', \
        'License :: OSI Approved :: Apache Software License', \
        'Operating System :: OS Independent', \
        'Topic :: Software Development :: Libraries :: Python Modules' \
        ],
)
