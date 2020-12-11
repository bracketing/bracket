# Command

import click
import shutil
import os

resources = {
    "example": "resources/example"
}

def nowpath(path):
    return os.path.join(os.path.dirname(__file__), path) + "/"

@click.group()
def cg():
    """
    ## Bracket

    **Bracket** is an elegant web user interface rendering tool

    ### Features

    - Single page server rendering can be embedded in various web server frameworks.
    - Use in large multi page projects.
    - Real time rendering while developing mode.
    - Use the command line to package the CI&CD as a static file.
    """

@click.command("create", short_help="Create a template project.")
@click.option('--name', prompt='Your Project Name',
              help='Give me a great name.')
def create(name):
    click.echo("Create ...")
    shutil.copytree(nowpath(resources["example"]), "./" + name + "/")
    click.echo("")
    click.echo("Your Project was created ...")
    click.echo("")
    click.echo("> cd ./" + name)
    click.echo("> python serve.py")
    click.echo("")

cg.add_command(create)

if __name__ == "__main__":
    cg()
