import pathlib


import setuptools


setuptools.setup(
    name="internet-archive-uploader",
    version="1.2",
    description="A wrapper around the internetarchive package for uploading files and directorys",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/jgore077/Internet-Archive-Uploader/blob/master/README.md",
    author="James Gore",
    author_email="jgore077@gmail.com",
    license='MIT',
    project_urls={
        
    },
    python_requires=">=3.6,<3.12",
    install_requires=[
        'internetarchive>=3.6.0'
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    
)