import codecs
import os.path
import re


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return codecs.open(fpath(fname), encoding='utf-8').read()


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


file_text = read(fpath('vvvv/__init__.py'))

setup(
    name='vvvv',
    version=grep('__version__'),
    description='vvvv Python OSC client',
    long_description=read(fpath('README.md')),
    url='https://github.com/Djiit/vvvv',
    author='Julien Tanay',
    author_email="julien.tanay@gmail.com",
    license='Apache 2.0',
    packages=['vvvv'],
    zip_safe=True,
    install_requires=[
        'python-osc==1.5'
    ],
    test_suite="tests",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
