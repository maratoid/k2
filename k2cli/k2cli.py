import click
import pkg_resources
from ansible_utils import *


resource_package = __name__ 
up_playbook = '/'.join('ansible').join('up.yaml')
down_playbook = '/'.join('ansible').join('down.yaml')
inventory = '/'.join('ansible').join('inventory').join('localhost')

@click.group()
def cli():
  pass

@click.command()
def down():
  runner = Runner(
    playbook=pkg_resources.resource_string(resource_package, down_playbook),
    hosts=pkg_resources.resource_string(resource_package, inventory),
    display=display,
    options={
        'subset': '~^local',
        # 'become': True,
        # 'become_method': 'sudo',
        # 'become_user': 'root',
        # 'private_key_file': '/path/to/the/id_rsa',
        'tags': 'all',
        # 'skip_tags': 'debug',
        'verbosity': 0,
    },
    # passwords={
    #     'become_pass': 'sudo_password',
    #     'conn_pass': 'ssh_password',
    # },
    # vault_pass='vault_password',
  )

  stats = runner.run()

@click.command()
def up():
  runner = Runner(
    playbook=pkg_resources.resource_string(resource_package, up_playbook),
    hosts=pkg_resources.resource_string(resource_package, inventory),
    display=display,
    options={
        'subset': '~^local',
        # 'become': True,
        # 'become_method': 'sudo',
        # 'become_user': 'root',
        # 'private_key_file': '/path/to/the/id_rsa',
        'tags': 'all',
        # 'skip_tags': 'debug',
        'verbosity': 0,
    },
    # passwords={
    #     'become_pass': 'sudo_password',
    #     'conn_pass': 'ssh_password',
    # },
    # vault_pass='vault_password',
  )
  stats = runner.run()

cli.add_command(up)
cli.add_command(down)