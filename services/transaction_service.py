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

def send_transaction_helper(contract, sender_private_key, recipient_address, data):
    account = accounts.add(sender_private_key)
    tx = contract.sendTransaction(recipient_address, json.dumps(data), {'from': account})
    return tx

def get_transaction_details(transaction_hash):
    web3 = getWeb3()
    text = web3.eth.getTransaction(transaction_hash).input

    bytesStr = codecs.decode("{}".format(text[2:]), "hex_codec")

    resp = eval(bytesStr.decode())
    return {"data": resp}

def get_transaction_details_helper(transaction_hash):
    web3 = getWeb3()
    tx = web3.eth.get_transaction(transaction_hash)
    input_data = tx.input
    return input_data

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

def get_all_transactions_helper(recipient_address):
    contract = getWeb3()
    filter = contract.events.TransactionMade.createFilter(fromBlock=0, argument_filters={'to': recipient_address})
    events = filter.get_all_entries()
    transactions = [{'from': event.args, 'to': event.args.to, 'jsonData': event.args.jsonData} for event in events]
    return transactions
