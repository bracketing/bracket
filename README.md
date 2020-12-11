# Bracket

<img align="right" src=artwork/20201210_224523_0000.png height="150px">

**Bracket** is an elegant web user interface rendering tool

### Features

- Single page server rendering can be embedded in various web server frameworks.
- Use in large multi page projects.
- Real time rendering while developing mode.
- Use the command line to package the CI&CD as a static file.

### Getting Started

Install from **Python Package Index**

``` bash
$ pip install bracket
```

Create a template project by **CLI**

``` bash
$ bracket create --name example
Create ...

Your Project was created ...

> cd ./example
> python serve.py
```

A template project:

``` bash
├─components
├─pages
└─public
    ├─fonts
    ├─javascript
    └─stylesheet
└─__init__.py   
└─.editorconfig
└─.eslintignore
└─.gitattributes
└─.gitignore
└─serve.py
└─site.py
```