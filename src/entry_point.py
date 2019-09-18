import click
import pkg_resources

from lib.global_cli.global_cli import cli_global_class
from .sample import commands as sample


@click.group()
@click.pass_context
def entry_point(ctx):
    """This is the entry point function"""
    ctx.ensure_object(dict)
    ctx.obj['cgc'] = cli_global_class('my_param')

entry_point.add_command(sample.sample)
