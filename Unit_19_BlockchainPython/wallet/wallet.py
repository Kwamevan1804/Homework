# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
import os
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
from eth_account import Account
from bit import PrivateKeyTestnet, PrivateKey, wif_to_key
from bit.network import NetworkAPI


# Load and set environment variables
load_dotenv("keys.env")
mnem_user = os.getenv("MNEMONIC")


# Import constants.py and necessary functions from bit and web3
from constants import *


# establish ETH connection
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)


# Create a function called `derive_wallets`
def derive_wallets(crypto):
    command = './derive -g --mnemonic=mnem_user --cols=address,index,path,privkey,pubkey,pubkeyhash,xprv,xpub --format=json --coin={} --numderive=3'.format(crypto)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)


#Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {'btctest': derive_wallets(BTCTEST), 'eth': derive_wallets(ETH), 'btc': derive_wallets(BTC)}

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST or coin == BTC:
        return PrivateKeyTestnet(priv_key)
    else:
        print("Invalid coin type")
        

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": to, "value": amount}
        )
        return {
            "from": account.address,
            "to": to,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
        }
    elif coin == BTCTEST or coin == BTC:
        return PrivateKeyTestnet.prepare_transaction(account.address, 
                                                     [(to, amount, BTC)])
    else:
        print("Invalid coin")
   

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, to, amount):
    raw_tx = create_tx(coin, account, to, amount)
    if coin == ETH:
        signed = account.sign_transaction(raw_tx)
        return w3.eth.sendRawTransaction(signed.rawTransaction)
    elif coin == BTCTEST or coin == BTC:        
        signed = account.sign_transaction(raw_tx)
        return NetworkAPI.broadcast_tx_testnet(signed)
    else:
        print("Invalid coin")
    print(result.hex())    
    return result.hex()    


# function to get address balances
def balances(coin, address, privkey):
    if coin == ETH:
        return w3.eth.getBalance(address)
    elif coin == BTCTEST or coin == BTC: 
        key = PrivateKeyTestnet(privkey)
        return key.get_balance()


# function to get ETH transaction status
def tx_status(txid):
    return w3.eth.getTransaction(txid)