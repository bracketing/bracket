import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bracket",
    version="0.0.1",
    author="Ceorleorn",
    author_email="snbck@qq.com",
    description="Bracket is an Elegant static site generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bracketing/bracket",
    packages=setuptools.find_packages(),
    install_requires=[],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'

)
