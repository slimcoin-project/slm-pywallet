# slm-pywallet
Pywallet script for Slimcoin and helper script to check addresses in a block explorer.
## pywallet

Requires Python 2.

Uses the following version: https://github.com/joric/pywallet/blob/master/pywallet.py

Licenses: See pywallet.py. Pywallet code was released into the public domain.

**Usage**

```python2 pywallet.py [options]

Options:
  --version            show program's version number and exit
  -h, --help           show this help message and exit
  --dumpwallet         dump wallet in json format
  --importprivkey=KEY  import private key from vanitygen
  --datadir=DATADIR    wallet directory (defaults to bitcoin default)
  --testnet            use testnet subdirectory and address type
  --password=PASSWORD  password for the encrypted wallet

Dependencies:
  bsddb (python 2.7.2 msi includes bsddb by default)

Links:
  http://www.python.org/ftp/python/2.7.2/python-2.7.2.msi
```

## cryptoidlookup.py

Allows to look up addresses at the Cryptoid explorer. Prints out addresses for which transactions are found.

Uses some code snippets from pypeerassets. License: BSD 3-clause (see LICENSE file)
Requires Python3.

Usage:

```
python3 cryptoidlookup.py [options] file

Options:
    -v  verbose mode (prints transactions and addresses without transactions)
    -s  start (allows to start at a certain position of the address list (e.g. if the block explorer stops responding)

```
