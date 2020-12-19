# Bracket

**Bracket** is an Elegant static site generator.

## Example

``` python
from jinja2 import Template
import bracket

website = bracket.Website(__name__)

@website.pages("/")
def handlefunction(context):
    return context({
        "title":"Welcome to Bracket",
        "content":Template('''
            <h1>{{ messages }}</h1>
            <img src="{{ bracket.res('/logo.png')">
        '''),
        "resources":{
            "messages":"Welcome to Bracket"
        }
    })

@website.resources()
def logo(static):
    return static([
        {
            "name":"logo.png",
            "code":bracket.find("./logo.png",in_public=True)
        },
        {
            "name":"face.png",
            "code":bracket.find("./face.png",in_public=True)
        }
    ])


website.pack()

# Output:

# /static/images/1bb87d41d15fe27b500a4bfcde01bb0e/logo.png
# /static/images/5a0b58b269313dea9b6de3ae68307bd7/face.png
# /static/bracket/0716eca5edcaf8702d79bad6f82496c8.css
# /index.html
# /_/meta.html

# /index.html

"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Bracket</title>
    <link href="/static/bracket/0716eca5edcaf8702d79bad6f82496c8.css" rel="stylesheet">
</head>
<body>
    <div class="bracket-app">
        <h1>
            <div>Welcome to Bracket</div>
        </h1>
        <img src="/static/images/1bb87d41d15fe27b500a4bfcde01bb0e/logo.png">
    </div>
</body>
</html>
"""

```


### Getting Started

Install from **Python Package Index**

``` bash
$ pip install bracket
```

