from setuptools import setup, find_packages

setup(
    name="autogen",
    version="0.1",
    packages=find_packages(include=["python", "python.*"]),
    install_requires=[],
    extras_require={
        "dev": [],
        "tools": [],
    },
)

