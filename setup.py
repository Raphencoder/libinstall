from setuptools import setup, find_packages

setup(
    name='libinstall',
    version='0.1',
    packages=find_packages(),
    author="Raphael Krief",
    author_email="raphaelkriefbm@gmail.com",
    description="Installe les librairies python necessaire d'un projet",
    long_description=open('README.md').read(),
    url="https://github.com/Raphencoder/libinstall",
    classifiers=[
    "Programming Language :: Python",
    "Development Status :: 1 - Planning",
    "License :: OSI Approved",
    "Natural Language :: French",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.7",
    "Topic :: Installation",
],
    py_modules=['libinstall'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': ['libinstall=lib.script:cli'],
    },
    license="BSD 3-Clause License"
    )