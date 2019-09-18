import click
from lib.sample.sample import my_sample

@click.group()
@click.option('--var-name', envvar='SAMPLE_VAR_NAME', default='my_var')
@click.pass_context
def sample(ctx, var_name):
    """Sample Click command

    """
    ctx.obj['sample_obj'] = my_sample(var_name)

@sample.command('print')
@click.pass_obj
def print_var(ctx):
    """Print the var value for the sample class. """
    ctx['sample_obj'].print_var()

@sample.command('test')
@click.pass_obj
def test_sample(ctx):
    """Print the var value for the sample class. """
    ctx['cgc'].print_global()