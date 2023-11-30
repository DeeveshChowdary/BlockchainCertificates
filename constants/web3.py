from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

WEB3 = None


def getWeb3ProviderURI():
    return "http://127.0.0.1:7545"


def getWeb3():
    WEB3 = Web3(HTTPProvider(getWeb3ProviderURI()))
    WEB3.middleware_onion.inject(geth_poa_middleware, layer=0)
    return WEB3
