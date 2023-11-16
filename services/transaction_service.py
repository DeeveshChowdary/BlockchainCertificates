# from app import app
from constants.web3 import getWeb3
import codecs
import json


def send_transaction(
    sender_address, sender_private_key, recipient_address, value, data
):
    web3 = getWeb3()
    nonce = web3.eth.getTransactionCount(sender_address)

    d = {
        "Transaction Type": "Certificate",
        "Certificate Hash": "THIS IS THE CERTIFICATE HASH",
        "Certificate Link": "https://chat.openai.com/chat/e283fdaa-d3b7-4dc7-999d-33dc9746306d",
    }

    text_data = json.dumps(d).encode("utf-8")

    print("TEXT DATA", text_data)
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
    print("STR", bytesStr)

    resp = eval(bytesStr.decode())
    return {"data": resp}
