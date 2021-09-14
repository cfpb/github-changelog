from setuptools import find_packages, setup


with open("README.md") as f:
    long_description = f.read()


setup(
    name="github-changelog",
    url="https://github.com/cfpb/github-changelog",
    author="CFPB",
    license="CC0",
    version="1.4.0",
    description="GitHub Pull Request changelog generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "requests>=2.13",
    ],
    extras_require={
        "testing": [
            "mock>=2.0.0",
            "coverage>=3.7.0",
            "flake8>=2.2.0",
        ],
    },
    test_suite="changelog.tests",
    entry_points={
        "console_scripts": [
            "changelog = changelog:main",
        ]
    },
)
