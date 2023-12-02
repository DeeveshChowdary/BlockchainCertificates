# from app import app
from constants.web3 import getWeb3
import codecs
import json


def send_transaction(
    sender_address, sender_private_key, recipient_address, value, data
):
    web3 = getWeb3()
    nonce = web3.eth.getTransactionCount(sender_address)

    text_data = json.dumps(data).encode("utf-8")

    tx = {
        "nonce": nonce,
        "to": recipient_address,
        "value": value,
        "gas": 2000000,
        "gasPrice": web3.toWei("50", "gwei"),
        "data": text_data,
    }
    signed_tx = web3.eth.account.signTransaction(tx, sender_private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    if receipt:
        return tx_hash.hex()


def get_transaction_details(transaction_hash):
    web3 = getWeb3()
    text = web3.eth.getTransaction(transaction_hash).input

    bytesStr = codecs.decode("{}".format(text[2:]), "hex_codec")

    resp = eval(bytesStr.decode())
    return {"data": resp}


def get_all_transactions(public_id):
    web3 = getWeb3()
    ending_blocknumber = web3.eth.blockNumber

    # print("ENDING BLOCK", ending_blocknumber)

    respo = []

    for x in range(ending_blocknumber):
        block = web3.eth.getBlock(x, True)
        for transaction in block.transactions:
            if transaction["to"] == public_id:
                respo.append(
                    {
                        "transaction_hash": transaction["hash"].hex(),
                        "from": str(transaction["from"]),
                        "transaction_details": get_transaction_details(
                            transaction["hash"]
                        ),
                    }
                )

    pending_tx_filter = web3.eth.filter("pending")
    pending_tx = pending_tx_filter.get_new_entries()

    for t in pending_tx:
        transaction = web3.eth.getTransaction(t)
        if transaction["to"] == public_id:
            respo.append(
                {
                    "transaction_hash": transaction["hash"].hex(),
                    "from": str(transaction["from"]),
                    "transaction_details": get_transaction_details(transaction["hash"]),
                }
            )

    return respo
