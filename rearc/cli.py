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
    problems = [
            ('2+3*4-4', 10),
            ('-4', -4),
            ('-4 * 2', -8),
            ('-2 * - (1 + 3)', 4),
            ('6 / 2 * 4 - 8 * 1', 4),
        ]
    for problem, answer in problems:
        result = parser.parse(problem)
        print(problem, '=', result, ';', result == answer)


if __name__ == "__main__":
    main()
