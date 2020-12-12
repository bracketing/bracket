import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bracket",
    version="0.0.1",
    author="Ceorleorn",
    author_email="snbck@qq.com",
    description="Bracket is an elegant web user interface rendering tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bracketing/bracket",
    packages=setuptools.find_packages(),
    install_requires=['click'],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'bracket=bracket:cli',
        ], },
    zip_safe=False,
    include_package_data=True

)
