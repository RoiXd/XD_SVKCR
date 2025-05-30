from setuptools import setup, find_packages

setup(
    name="XD_SVKCR",
    version="0.1.0",
    author="Roixd",
    author_email="chibouni562@gmail.com",
    description="A library that contains (well literally) random stuff",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_library",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License ::  2.0",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        # List dependencies here
    ],
)