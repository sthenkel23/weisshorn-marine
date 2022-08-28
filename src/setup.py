import setuptools
import os

setuptools.setup(
    name=os.environ["LIB_NAME"],
    version="0.0.0.1",
    author="<author>",
    author_email="coder.henkelmann@gmail.com",
    description="A boilerplate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)