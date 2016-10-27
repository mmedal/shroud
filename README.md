# Shroud

**Easy encryption for deployed secrets.**

[![travis-image]][travis]
[![pypi-image]][pypi]

## Requirements

* Python 2.7.x, 3.4.x, 3.5.x
* MacOS or Linux
* Valid keyring software if using keyring storage for private key passphrases.
  If you are using MacOS, you're all set (MacOS has a Keychain)!
  For Linux, see [details](http://pythonhosted.org/keyring/#linux).
  For installing SecretStorage on Ubuntu 16.04 and headless Linux, see
  [setup instructions](http://pythonhosted.org/keyring/#using-keyring-on-ubuntu-16-04).

## Installation

Install using pip:

    $ pip install shroud


## Usage

    $ shroud generate_keypair -l
    $ shroud encrypt MYSECRETVAR=supersecret123
    $ shroud decrypt -l


[travis-image]: https://secure.travis-ci.org/mmedal/shroud.svg?branch=master
[travis]: http://travis-ci.org/mmedal/shroud?branch=master
[pypi-image]: https://img.shields.io/pypi/v/shroud.svg
[pypi]: https://pypi.python.org/pypi/shroud
