from setuptools import find_packages, setup

setup(
    name='github-changelog',
    url='https://github.com/cfpb/github-changelog',
    author='CFPB',
    license='CC0',
    version='1.0.0',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'requests>=2.13',
    ],
    extras_require={
        'testing': [
            'mock>=2.0.0',
            'coverage>=3.7.0',
            'flake8>=2.2.0',
        ],
    },
    test_suite="changelog.tests",
    entry_points={
        'console_scripts': ['changelog = changelog:main', ]
    }
)
