import click, json
#from .azure import deploy_to_azure
#from .__init__ import __version__
#from . import constant

def validate_config(config):
    # TODO validate JSON schema
    return (True,"")

def read_config():
    #default_conf = json.load(open(constant.DEFAULT_CONFIGURATION))
    default_conf = json.load(open("conf/default_configuration.json"))
    return default_conf

def echo_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('0.0.1-beta') #TODO use __version__ defined in __init__.py
    ctx.exit()

@click.group()
@click.option(
    '--version',
    is_flag=True,
    callback=echo_version,
    expose_value=False,
    is_eager=True
)
def deploud():
    pass

@click.command(short_help='Bring up a cluster.')
@click.option("--admin_user",prompt="MarkLgoc admin user name",help="MarkLgoc admin user name (prompt)")
@click.password_option("--admin_password", prompt="MarkLgoic admin password", help="MarkLgoc admin password (prompt)")
def lauch(admin_user, admin_password):
    """
    Bring up a cluster.
    """
    conf = read_config()
    (successful, reason) = validate_config(conf)
    if not successful:
        click.echo("something")
        return
    platform = conf.platform
    pass


@click.command(short_help='Blow away a cluster.')
def blow_away():
    pass

deploud.add_command(bring_up)
deploud.add_command(blow_away)

if __name__ == "__main__":
    deploud()