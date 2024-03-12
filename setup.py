import pathlib


import setuptools


setuptools.setup(
    name="internet-archive-uploader",
    version="1.0",
    description="A wrapper around the internetarchive package for uploading files and directorys",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_contenttype="text/markdown",
    url="Link to github",
    author="James Gore",
    author_email="jgore077@gmail.com",
    license='MIT',
    project_urls={
        
    },
    python_requires=">=3.6,<3.12",
    install_requires=[
        'internetarchive'
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    
)