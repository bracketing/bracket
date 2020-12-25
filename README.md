## 🎊 Bracket is with Jinja

![PyPI](https://img.shields.io/pypi/v/bracket) ![PyPI - Downloads](https://img.shields.io/pypi/dm/bracket)

**Bracket** is an Elegant static site generator. It encapsulates **[Jinja2](https://github.com/pallets/jinja)**. Its biggest highlight is to render the static pages in the form of **view function**, and support real-time **debugging**. It can also support **CSS framework**, **international routing** and more functions through ecological extension.

### Install 

``` bash
$ pip install bracket
```

### Example

``` python
from bracket import WebSite

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

They render:

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

#### License

**MIT** 