from setuptools import find_packages, setup

setup(
    name='jts',
    version='1.0.0',
    install_requires=[
        'flask'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'jts = jts:run'
        ]
    }
)
