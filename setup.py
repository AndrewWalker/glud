from setuptools import setup
import os


def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    contents = open(path).read()
    return contents


setup(
    name         = "glud",
    version      = "0.0.1",
    description  = "TBD",
    long_description = read('README.rst'),
    author       = "Andrew Walker",
    author_email = "walker.ab@gmail.com",
    url          = "http://github.com/AndrewWalker/glud",
    license      = "MIT",
    zip_safe     = False,
    packages     = ['glud'],
    package_dir  = { 'glud' : 'glud' },
    package_data = {
        'glud' : ['templates/*.tpl']
    },
    entry_points = {
        'console_scripts' : [
            'glud = glud:main'
        ]
    },
    classifiers  = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Code Generators',
    ],
)

