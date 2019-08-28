from setuptools import setup

setup(
    name='libinstall',
    version='0.1',
    py_modules=['libinstall'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': ['libinstall=lib.script:cli'],
    },
    )
