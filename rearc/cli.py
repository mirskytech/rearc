# -*- coding: utf-8 -*-

"""Console script for rearc."""

import click

from rearc.parser import GCodeParser


@click.command()
def main(args=None):
    """Console script for rearc."""
    click.echo("Replace this message by putting your code into "
               "rearc.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")

    parser = GCodeParser()
    examples = [
        'G123 X1 X1'
        ]
    for example in examples:
        result = parser.parse(example)

if __name__ == "__main__":
    main()
