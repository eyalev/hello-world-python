# -*- coding: utf-8 -*-

"""Console script for hello_world_python."""

import click

from hello_world_python.main import print_hello_world


@click.command()
def main(args=None):
    """Console script for hello_world_python."""

    print_hello_world()

if __name__ == "__main__":
    main()
