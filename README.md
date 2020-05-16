# feedly-to-sqlite

[![PyPI](https://img.shields.io/pypi/v/feedly-to-sqlite.svg)](https://pypi.org/project/feedly-to-sqlite/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/bcongdon/feedly-to-sqlite/blob/master/LICENSE)

Save data from [feedly](https://www.feedly.com/) to a SQLite database. Supports
saving subscription and collection data.

## How to install

    $ pip install feedly-to-sqlite

## Authentication

Obtain a personal developer token [here](https://feedly.com/v3/auth/dev). Run
the following command and enter your Feedly developer auth token :

    $ feedly-to-sqlite auth

This will create a file called `auth.json` in your current directory containing
the required value. To save the file at a different path or filename, use the
`--auth=myauth.json` option.

## Usage

After you've setup your authentication, you can use the following commend to
download and save your feedly data:

    $ feedly-to-sqlite subscriptions feedly.db

More detailed help can be found by running the command with `--help`

    $ feedly-to-sqlite --help

## Attribution

This package is heavily inspired by
[goodreads-to-sqlite](https://github.com/rixx/goodreads-to-sqlite/) by
[Tobias Kunze ](https://github.com/rixx) and
[github-to-sqlite](https://github.com/dogsheep/github-to-sqlite/) by
[Simon Willison](https://simonwillison.net/2019/Oct/7/dogsheep/).

This package was designed to fit nicely in the
[dogsheep](https://dogsheep.github.io/) /
[datasette](https://github.com/simonw/datasette) ecosystems.
