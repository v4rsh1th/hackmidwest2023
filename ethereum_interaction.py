from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))  # Connect to your Ethereum node
contract_address = "0x454D250D4BBB18f00f34c22dE8F0C327Ea2df220"
private_key = "0xc62cb25cd1d79c09411568d004fa0bd37aa5029db40a5c2339ea250ab7021034"

# Load the contract ABI
with open('ContentLicense.json', 'r') as abi_file:
    contract_abi = json.load(abi_file)

contract = w3.eth.contract(address=contract_address, abi=contract_abi)
account = w3.eth.account.privateKeyToAccount(private_key)

def license_content(value_in_wei):
    nonce = w3.eth.getTransactionCount(account.address)
    tx = contract.functions.licenseContent().buildTransaction({
        'chainId': 1,  # Mainnet
        'gas': 2000000,
        'gasPrice': w3.toWei('30', 'gwei'),
        'nonce': nonce,
        'value': value_in_wei
    })
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return w3.toHex(tx_hash)
