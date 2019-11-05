import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='aisastack',
    version='1.0.1',
    scripts=['aisvue'] ,
    author="Aisahana",
    author_email="aisahana.business@gmail.com",
    description="Command Line Tools for creating skeleton project in FrontEnd (django rest)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aisahana/aisastack",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'python-cli-ui',
        'pyfiglet==0.7',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)