from os.path import expanduser, isfile

import click

from shroud import encryption


@click.group()
def cli():
    pass


@click.command()
@click.option('--name', '-n',
              prompt="Name for keypair", default='shroud')
@click.option('--keydir', '-d',
              prompt="Directory to place keys in",
              type=click.Path(exists=True, file_okay=False, writable=True),
              default=expanduser('~') + '/.ssh')
@click.option('--passphrase', '-p',
              prompt="Passphrase for private key", default='',
              hide_input=True, confirmation_prompt=True)
@click.option('--forcewrite', '-f',
              is_flag=True, default=False)
def generate_keypair(name, keydir, passphrase, forcewrite):
    if passphrase == '':
        passphrase = None

    pub_filename = '{}/{}.pub'.format(keydir, name)
    priv_filename = '{}/{}'.format(keydir, name)
    if isfile(pub_filename) and not forcewrite:
        click.confirm("{} already exists. Would you like to write over it?"
                      .format(pub_filename), abort=True, default=True)
    if isfile(priv_filename) and not forcewrite:
        click.confirm("{} already exists. Would you like to write over it?"
                      .format(priv_filename), abort=True, default=True)

    click.echo("Generating keypair ...")
    pub, priv = encryption.generate_rsa_key_pair(passphrase=passphrase)

    click.echo("Storing public key in {} ...".format(pub_filename))
    with click.open_file(pub_filename, 'wb') as f:
        f.write(pub)
    click.echo("Storing private key in {} ...".format(priv_filename))
    with click.open_file(priv_filename, 'wb') as f:
        f.write(priv)


@click.command()
@click.argument('secret')
@click.option('--pubkey', '-k',
              type=click.Path(exists=True), default='~/.ssh/shroud.pub')
def encrypt(secret, pubkey):
    print('Hello world!')


cli.add_command(generate_keypair)
cli.add_command(encrypt)
