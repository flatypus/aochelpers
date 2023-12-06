from setuptools import setup, find_packages

DESCRIPTION = "My personal Advent of Code helper functions"

VERSION = '0.0.1'

setup(
    name="flatypus-aochelpers",
    version=VERSION,
    author="Hinson Chan",
    author_email="<yhc3141@gmail.com>",
    maintainer="Hinson Chan",
    maintainer_email="<yhc3141@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    license='MIT'
)