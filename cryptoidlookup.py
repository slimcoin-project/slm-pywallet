from typing import cast, Union
import json, time, sys
from urllib.request import Request, urlopen
from http.client import HTTPResponse

"""This script looks up to cryptoid to look which addresses of a pywallet dump have transactions in it.
   Requires python 3.
   Without options it just print out addresses it finds transactions for.

   Uses some code snippets of pypeerassets (BSD 3-Clause License)
   Source: https://github.com/PeerAssets/pypeerassets
   (c) PeerAssets project 2019
   
   
   Options:
   -v - Verbose (shows transactions)"""

COIN="slm"
EXPLORER_URL = 'https://chainz.cryptoid.info/explorer/'
EXPLORER_API = 'https://chainz.cryptoid.info/{}/api.dws'.format(COIN)



def get_url(url: str) -> Union[dict, int, float, str]:
    '''Perform a GET request for the url and return a dictionary parsed from
       the JSON response.'''

    request = Request(url, headers={"User-Agent": "pywalletlookup"})
    response = cast(HTTPResponse, urlopen(request))
    if response.status != 200:
        raise Exception(response.reason)
    return json.loads(response.read().decode())



def listtransactions(address: str) -> list:

    query = 'address.summary.dws?coin={net}&id={addr}'.format(
        net=COIN,
        addr=address,
        )
    response = cast(dict, get_url(EXPLORER_URL + query))
    return [tx[1].lower() for tx in response["tx"]]


def getdump(filename: str) -> dict:
    with open(filename, "r") as f:
       walletdump = json.load(f)

    return walletdump


def main(args):
    verbose = True if "-v" in args else False
    start = args[args.index("-s") + 1] if "-s" in args else 0
    wdump = getdump(args[1])
    try:
        addresslist = wdump["keys"][start:]
    except KeyError:
        print("No addresses found in this wallet dump.")
        return

    for item in addresslist:
        address = item.get("addr")
        if verbose: print("Looking up address:", address)

        try:
            txes = listtransactions(address)
        except KeyError:
            txes = {}
        if len(txes) == 0:
            if verbose: print("Address", address, "without transactions.")
        else:
            if verbose:
                print("Address with {} transactions: {}".format(len(txes), address))
                print(txes)
            else:
                print(address)

        time.sleep(10)


if __name__ == "__main__":
    main(sys.argv)
