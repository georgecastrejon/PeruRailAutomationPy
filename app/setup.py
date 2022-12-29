import cli

from pip._internal.req import parse_requirements
from setuptools import setup, find_packages

long_description = "TsoftTest:cli"
requirements = parse_requirements('requirements.txt', session=False)
install_requires = [str(r.req) for r in requirements]

setup(
    name                    = 'test:cli',
    description             = 'test:cli-peruRail',
    packages                = find_packages(),
    author                  = 'tsoft',
    author_email            = 'angelo.abregu@tsoftglobal.com',
    scripts                 = ['bin/cli'],
    version                 = cli.__version__,
    url                     = 'https://',
    license                 = 'MIT',
    zip_safe                = False,
    keywords                = 'cli,task',
    long_description        = long_description,
    classifiers             = ['Development Status :: 4 - Beta',
                               'Intended Audience :: Developers',
                               'License :: OSI Approved :: MIT License',
                               'Topic :: Software Development :: Build Tools',
                               'Topic :: Software Development :: Libraries',
                               'Topic :: Software Development :: Testing',
                               'Topic :: Utilities',
                               'Operating System :: MacOS :: MacOS X',
                               'Operating System :: Microsoft :: Windows',
                               'Operating System :: POSIX',
                               'Programming Language :: Python :: 3.6',
                               'Programming Language :: Python :: 2.7',]

)