"""
# Bracket

**Bracket** is an elegant web user interface rendering tool

### Features

- Single page server rendering can be embedded in various web server frameworks.
- Use in large multi page projects.
- Real time rendering while developing mode.
- Use the command line to package the CI&CD as a static file.

"""

from .app import Bracket
from .document import Document
from .router import Router
from .router import route
from .cli import cg as cli