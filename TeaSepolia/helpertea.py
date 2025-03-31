from web3 import Web3, HTTPProvider
import json
import random
import secrets
import time

print(f'Helper EVM Tea Sepolia Testnet By ADFMIDN Team')
print(f'- Auto Send Native To Random Recipient Address')
print(f'- Auto Deploy Contract')
print(f'- Auto Interaction Contract')
print(f'- Auto Send Spesific Token To Random Recipient Address')
print(f'')

web3 = Web3(Web3.HTTPProvider("https://tea-sepolia.g.alchemy.com/public"))
chainId = web3.eth.chain_id

# if  web3.is_connected() == True:
    # print("Web3 Connected...\n")
# else:
    # print("Error Connecting Please Try Again Exit...")
    # exit()

datadeploy = "0x6080604052348015600f57600080fd5b5061036a8061001f6000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c8063031d5d011461003b578063b588bfad14610059575b600080fd5b61004361006e565b6040516100509190610112565b60405180910390f35b61006c610067366004610161565b610100565b005b60606000805461007d906101d3565b80601f01602080910402602001604051908101604052809291908181526020018280546100a9906101d3565b80156100f65780601f106100cb576101008083540402835291602001916100f6565b820191906000526020600020905b8154815290600101906020018083116100d957829003601f168201915b5050505050905090565b600061010d828483610273565b505050565b60006020808352835180602085015260005b8181101561014057858101830151858201604001528201610124565b506000604082860101526040601f19601f8301168501019250505092915050565b6000806020838503121561017457600080fd5b823567ffffffffffffffff8082111561018c57600080fd5b818501915085601f8301126101a057600080fd5b8135818111156101af57600080fd5b8660208285010111156101c157600080fd5b60209290920196919550909350505050565b600181811c908216806101e757607f821691505b60208210810361020757634e487b7160e01b600052602260045260246000fd5b50919050565b634e487b7160e01b600052604160045260246000fd5b601f82111561010d576000816000526020600020601f850160051c8101602086101561024c5750805b601f850160051c820191505b8181101561026b57828155600101610258565b505050505050565b67ffffffffffffffff83111561028b5761028b61020d565b61029f8361029983546101d3565b83610223565b6000601f8411600181146102d357600085156102bb5750838201355b600019600387901b1c1916600186901b17835561032d565b600083815260209020601f19861690835b8281101561030457868501358255602094850194600190920191016102e4565b50868210156103215760001960f88860031b161c19848701351681555b505060018560011b0183555b505050505056fea264697066735822122055624fd2cb38f0bfa640ac81ca40f9a0bc410d13e12db84e10a0e36edf4217c664736f6c63430008190033"

msg_abi = json.loads('[{"inputs": [{"internalType": "string","name": "newMessage","type": "string"}],"name": "writeMessage","outputs": [],"stateMutability": "nonpayable","type": "function"}]')

token_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_spender","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]')

def log(txt):
    f = open('dataevmteasepolia.txt', "a")
    f.write(txt + '\n')
    f.close()
    
def get_base_gas_price():
    """Retrieve the base gas price from the latest block."""
    latest_block = web3.eth.get_block('latest')
    base_fee_per_gas = latest_block.get('baseFeePerGas', None)

    if base_fee_per_gas is None:
        raise ValueError("Base fee per gas not available in this block.")

    return base_fee_per_gas

def sendToken(sender, key, ctraddr, amount, recipient):
    try:
        getGasPrice = web3.from_wei(int(get_base_gas_price()), 'gwei')
        max_priority_fee = (5*getGasPrice)/100
        max_fee = getGasPrice + max_priority_fee
        gasPrice = web3.to_wei(max_fee, 'gwei')
        nonce = web3.eth.get_transaction_count(sender)
        totalamount = web3.to_wei(amount, 'ether')
        token_contract = web3.eth.contract(address=web3.to_checksum_address(ctraddr), abi=token_abi)
        nametkn = token_contract.functions.name().call()
        gasAmount = token_contract.functions.transfer(recipient, totalamount).estimate_gas({
            'chainId': chainId,
            'from': sender,
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        token_tx = token_contract.functions.transfer(recipient, totalamount).build_transaction({
            'chainId': chainId,
            'from': sender,
            'gasPrice': gasPrice,
            'gas': gasAmount,
            'nonce': nonce
        })
        
        #sign & send the transaction
        tx_hash = web3.eth.send_raw_transaction(web3.eth.account.sign_transaction(token_tx, key).rawTransaction)
        #get transaction hash
        print(f'Processing Send {amount} {nametkn} From {sender} To {recipient} ...')
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Send {amount} {nametkn} From {sender} To {recipient} Success!')
        print(f'TX-ID : {str(web3.to_hex(tx_hash))}')
    except Exception as e:
        print(f'Error : {e}')
        pass

def writeContract(sender, key, ctraddr):
    try:
        getGasPrice = web3.from_wei(int(get_base_gas_price()), 'gwei')
        max_priority_fee = (5*getGasPrice)/100
        max_fee = getGasPrice + max_priority_fee
        gasPrice = web3.to_wei(max_fee, 'gwei')
        nonce = web3.eth.get_transaction_count(sender)
        msg_contract = web3.eth.contract(address=web3.to_checksum_address(ctraddr), abi=msg_abi)
        gasAmount = msg_contract.functions.writeMessage("test").estimate_gas({
            'chainId': chainId,
            'from': sender,
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        msg_tx = msg_contract.functions.writeMessage("test").build_transaction({
            'chainId': chainId,
            'from': sender,
            'gasPrice': gasPrice,
            'gas': gasAmount,
            'nonce': nonce
        })
        
        #sign & send the transaction
        tx_hash = web3.eth.send_raw_transaction(web3.eth.account.sign_transaction(msg_tx, key).rawTransaction)
        #get transaction hash
        print(f'Processing Interaction On Contract {ctraddr} From {sender} ...')
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Interaction On Contract {ctraddr} From {sender} Success!')
        print(f'TX-ID : {str(web3.to_hex(tx_hash))}')
    except Exception as e:
        print(f'Error : {e}')
        pass

def deployContract(sender, key):
    try:
        getGasPrice = web3.from_wei(int(get_base_gas_price()), 'gwei')
        max_priority_fee = (5*getGasPrice)/100
        max_fee = getGasPrice + max_priority_fee
        gasPrice = web3.to_wei(max_fee, 'gwei')
        nonce = web3.eth.get_transaction_count(sender)
        gasAmount = web3.eth.estimate_gas({
            'chainId': chainId,
            'from': sender,
            'data': datadeploy,
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        deploy_tx = {
            'chainId': chainId,
            'from': sender,
            'data': datadeploy,
            'gasPrice': gasPrice,
            'gas': gasAmount,
            'nonce': nonce
        }
        
        #sign & send the transaction
        tx_hash = web3.eth.send_raw_transaction(web3.eth.account.sign_transaction(deploy_tx, key).rawTransaction)
        #get transaction hash
        print(f'Processing Deploy Contract From {sender} ...')
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Deploy Contract Success From {sender} Success!')
        print(f'TX-ID & Contract Address : {str(web3.to_hex(tx_hash))} & {transaction_receipt.contractAddress}')
        return transaction_receipt.contractAddress
    except Exception as e:
        print(f'Error : {e}')
        pass

def sendNative(sender, key, amount, recipient):
    try:
        getGasPrice = web3.from_wei(int(get_base_gas_price()), 'gwei')
        max_priority_fee = (10*getGasPrice)/100
        max_fee = getGasPrice + max_priority_fee
        gasPrice = web3.to_wei(max_fee, 'gwei')
        nonce = web3.eth.get_transaction_count(sender)
        totalamount = web3.to_wei(amount, 'ether')
        gasAmount = web3.eth.estimate_gas({
            'chainId': chainId,
            'from': sender,
            'to': recipient,
            'value': totalamount,
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        native_tx = {
            'chainId': chainId,
            'from': sender,
            'to': recipient,
            'value': totalamount,
            'gasPrice': gasPrice,
            'gas': gasAmount,
            'nonce': nonce
        }
        
        #sign & send the transaction
        tx_hash = web3.eth.send_raw_transaction(web3.eth.account.sign_transaction(native_tx, key).rawTransaction)
        #get transaction hash
        print(f'Processing Send {amount} Native From {sender} To {recipient} ...')
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Send {amount} Native From {sender} To {recipient} Success!')
        print(f'TX-ID : {str(web3.to_hex(tx_hash))}')
    except Exception as e:
        print(f'Error : {e}')
        pass

amountmin = float(input('Min Send Amount : '))
amountmax = float(input('Max Send Amount : '))
tknaddr = web3.to_checksum_address(input('Input Token Address : '))
print(f'')         
def sendTX():
    try:
        while True:
            with open('pvkeylist.txt', 'r') as file:
                local_data = file.read().splitlines()
                for pvkeylist in local_data:
                    sender = web3.eth.account.from_key(pvkeylist)
                    recipient = web3.eth.account.from_key(secrets.token_hex(32))
                    log(f'{recipient.address}|{web3.to_hex(recipient.key)}')
                    amountrandom = random.uniform(amountmin, amountmax)
                    sendNative(sender.address, sender.key, amountrandom, recipient.address)
                    print(f'')
                    ctraddr = deployContract(sender.address, sender.key)
                    print(f'')
                    writeContract(sender.address, sender.key, ctraddr)
                    print(f'')
                    sendToken(sender.address, sender.key, tknaddr, amountrandom, recipient.address)
                    print(f'')
    except Exception as e:
        print(f'Error : {e}')
        pass
        
sendTX()
