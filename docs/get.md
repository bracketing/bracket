# Bracket

> *This is a short quick start*

## Install

``` bash
$ pip install bracket
```

## A Simple Example

``` python
from bracket import WebSite
from jinja2 import Template

app = WebSite(__name__)

@app.pages("/")
def helloworld(context):
    return context({
    "title":"Welcome to Bracket",
    "content":Template('''
        <h1>{{ messages }}</h1>
        <img src="{{ bracket.res('/logo.png')}}">
    '''),
    "resources":{
        "messages":"Welcome to Bracket"
    }
})

app.dispatch("/")
```

* `#4` Creating `app` through `WebSite(__name__)`
* `#6` Create `helloworld` interface through `app.pages()`
* `#8` Send `jinja2` content with rendering through `context` object
    * `title` Title of HTML
    * `context` `jinja2.Template`
    * `resources` Template parameters passed
* `#19` Rendering interface

``` html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="generator" content="Bracket & Jinja2 ">
    
    <title>Welcome to Bracket</title>
</head>
<body>
    <div id="bracketapp">
    
        <h1>Welcome to Bracket</h1>
        <img src="/static/logo.png">
        
    </div>
</body>
</html>
```

## Serve

``` bash
$ pip install flask
```

``` python
app.serve(serveconfigs={
    "host":"localhost",
    "port":5000,
    "debug":False
})
```

> *The function is still being improved*

## Build

``` python
app.build()
```
