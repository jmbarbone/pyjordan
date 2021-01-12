from setuptools import find_packages, setup
# from package import Package

setup(
    name="pyjordan",
    version="0.1.0",
    description="Personal function keeping for Jordan",
    url="https://github.com/jmbarbone/pyjordan",
    author="Jordan Mark Barbone",
    author_email="jmbarbone@gmail.com",
    license="MIT",
    packages=find_packages(exclude=("tests")),
    include_package_data=True
)
