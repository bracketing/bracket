import setuptools
import re

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("bracket/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setuptools.setup(
    name="bracket",
    version=version,
    packages=setuptools.find_packages(),
    author="Ceorleorn",
    author_email="snbck@qq.com",
    description="Bracket is an Elegant static site generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bracketing/bracket/",
    install_requires=[
        "Jinja2>=2.10.1"
    ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

)
