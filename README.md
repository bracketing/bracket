# Bracket

**Bracket** is an Elegant static site generator. It encapsulates **[Jinja2](https://github.com/pallets/jinja)**. Its biggest highlight is to render the static pages in the form of **view function**, and support real-time **debugging**. It can also support **CSS framework**, **international routing** and more functions through ecological extension.

## Installing

Install and update using [pip](pypi.org):

``` bash
$ pip install bracket
```

## A Simple Example

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

## Contributing

How to contribute to this project, report problems, and build a development environment, please refer to the [contribution guide]()

## Links

* Website: https://bracket.ink
* Documentation: https://bracket.ink/docs/
* Releases: https://pypi.org/project/bracket/
* Code: https://github.com/bracketing/bracket
* Issue tracker: https://github.com/bracketing/bracket/issues

## License

The project is open source under MIT license in [GitHub Community](https://github.com). No one is allowed to infringe the copyright. Please follow `LICENSE`
