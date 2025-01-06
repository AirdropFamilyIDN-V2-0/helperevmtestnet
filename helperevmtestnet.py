from web3 import Web3, HTTPProvider
import json
import random
import secrets
import time

print(f'Helper EVM Testnet By ADFMIDN Team | Support Multiplechain')
print(f'- Auto Send Native To Random Recipient Address')
print(f'- Auto Deploy Contract')
print(f'- Auto Interaction Contract')
print(f'- Auto Deploy Token')
print(f'- Auto Send Token To Random Recipient Address')
print(f'')

web3 = Web3(Web3.HTTPProvider(input('Input RPC Url [https://] : ')))
chainId = web3.eth.chain_id

if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else:
    print("Error Connecting Please Try Again Exit...")
    exit()

datadeploy = "0x6080604052348015600f57600080fd5b5061036a8061001f6000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c8063031d5d011461003b578063b588bfad14610059575b600080fd5b61004361006e565b6040516100509190610112565b60405180910390f35b61006c610067366004610161565b610100565b005b60606000805461007d906101d3565b80601f01602080910402602001604051908101604052809291908181526020018280546100a9906101d3565b80156100f65780601f106100cb576101008083540402835291602001916100f6565b820191906000526020600020905b8154815290600101906020018083116100d957829003601f168201915b5050505050905090565b600061010d828483610273565b505050565b60006020808352835180602085015260005b8181101561014057858101830151858201604001528201610124565b506000604082860101526040601f19601f8301168501019250505092915050565b6000806020838503121561017457600080fd5b823567ffffffffffffffff8082111561018c57600080fd5b818501915085601f8301126101a057600080fd5b8135818111156101af57600080fd5b8660208285010111156101c157600080fd5b60209290920196919550909350505050565b600181811c908216806101e757607f821691505b60208210810361020757634e487b7160e01b600052602260045260246000fd5b50919050565b634e487b7160e01b600052604160045260246000fd5b601f82111561010d576000816000526020600020601f850160051c8101602086101561024c5750805b601f850160051c820191505b8181101561026b57828155600101610258565b505050505050565b67ffffffffffffffff83111561028b5761028b61020d565b61029f8361029983546101d3565b83610223565b6000601f8411600181146102d357600085156102bb5750838201355b600019600387901b1c1916600186901b17835561032d565b600083815260209020601f19861690835b8281101561030457868501358255602094850194600190920191016102e4565b50868210156103215760001960f88860031b161c19848701351681555b505060018560011b0183555b505050505056fea264697066735822122055624fd2cb38f0bfa640ac81ca40f9a0bc410d13e12db84e10a0e36edf4217c664736f6c63430008190033"

datatoken = "0x6080604052601260025f6101000a81548160ff021916908360ff1602179055503480156200002b575f80fd5b50612710423360405160200162000044929190620002d7565b604051602081830303815290604052805190602001205f1c62000068919062000333565b6040516020016200007a9190620003c2565b6040516020818303038152906040525f908162000098919062000646565b506103e84233604051602001620000b192919062000778565b604051602081830303815290604052805190602001205f1c620000d5919062000333565b604051602001620000e7919062000802565b6040516020818303038152906040526001908162000106919062000646565b505f60025f9054906101000a900460ff16600a620001259190620009b4565b620f424042336040516020016200013e929190620002d7565b604051602081830303815290604052805190602001205f1c62000162919062000333565b6200016e919062000a04565b90508060038190555060035460045f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f20819055503373ffffffffffffffffffffffffffffffffffffffff165f73ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef6003546040516200021c919062000a5f565b60405180910390a35062000a7a565b5f819050919050565b5f819050919050565b620002526200024c826200022b565b62000234565b82525050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f620002838262000258565b9050919050565b5f8160601b9050919050565b5f620002a2826200028a565b9050919050565b5f620002b58262000296565b9050919050565b620002d1620002cb8262000277565b620002a9565b82525050565b5f620002e482856200023d565b602082019150620002f68284620002bc565b6014820191508190509392505050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601260045260245ffd5b5f6200033f826200022b565b91506200034c836200022b565b9250826200035f576200035e62000306565b5b828206905092915050565b5f81905092915050565b7f546f6b656e0000000000000000000000000000000000000000000000000000005f82015250565b5f620003aa6005836200036a565b9150620003b78262000374565b600582019050919050565b5f620003ce826200039c565b9150620003dc82846200023d565b60208201915081905092915050565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806200046757607f821691505b6020821081036200047d576200047c62000422565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f60088302620004e17fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82620004a4565b620004ed8683620004a4565b95508019841693508086168417925050509392505050565b5f819050919050565b5f6200052e6200052862000522846200022b565b62000505565b6200022b565b9050919050565b5f819050919050565b62000549836200050e565b62000561620005588262000535565b848454620004b0565b825550505050565b5f90565b6200057762000569565b620005848184846200053e565b505050565b5b81811015620005ab576200059f5f826200056d565b6001810190506200058a565b5050565b601f821115620005fa57620005c48162000483565b620005cf8462000495565b81016020851015620005df578190505b620005f7620005ee8562000495565b83018262000589565b50505b505050565b5f82821c905092915050565b5f6200061c5f1984600802620005ff565b1980831691505092915050565b5f6200063683836200060b565b9150826002028217905092915050565b6200065182620003eb565b67ffffffffffffffff8111156200066d576200066c620003f5565b5b6200067982546200044f565b62000686828285620005af565b5f60209050601f831160018114620006bc575f8415620006a7578287015190505b620006b3858262000629565b86555062000722565b601f198416620006cc8662000483565b5f5b82811015620006f557848901518255600182019150602085019450602081019050620006ce565b8683101562000715578489015162000711601f8916826200060b565b8355505b6001600288020188555050505b505050505050565b7f73796d626f6c00000000000000000000000000000000000000000000000000005f82015250565b5f620007606006836200036a565b91506200076d826200072a565b600682019050919050565b5f6200078582856200023d565b602082019150620007978284620002bc565b601482019150620007a88262000752565b91508190509392505050565b7f53594d00000000000000000000000000000000000000000000000000000000005f82015250565b5f620007ea6003836200036a565b9150620007f782620007b4565b600382019050919050565b5f6200080e82620007dc565b91506200081c82846200023d565b60208201915081905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f8160011c9050919050565b5f808291508390505b6001851115620008b5578086048111156200088d576200088c6200082b565b5b60018516156200089d5780820291505b8081029050620008ad8562000858565b94506200086d565b94509492505050565b5f82620008cf5760019050620009a1565b81620008de575f9050620009a1565b8160018114620008f75760028114620009025762000938565b6001915050620009a1565b60ff8411156200091757620009166200082b565b5b8360020a9150848211156200093157620009306200082b565b5b50620009a1565b5060208310610133831016604e8410600b8410161715620009725782820a9050838111156200096c576200096b6200082b565b5b620009a1565b62000981848484600162000864565b925090508184048111156200099b576200099a6200082b565b5b81810290505b9392505050565b5f60ff82169050919050565b5f620009c0826200022b565b9150620009cd83620009a8565b9250620009fc7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8484620008be565b905092915050565b5f62000a10826200022b565b915062000a1d836200022b565b925082820262000a2d816200022b565b9150828204841483151762000a475762000a466200082b565b5b5092915050565b62000a59816200022b565b82525050565b5f60208201905062000a745f83018462000a4e565b92915050565b610d7b8062000a885f395ff3fe608060405234801561000f575f80fd5b5060043610610091575f3560e01c8063313ce56711610064578063313ce5671461013157806370a082311461014f57806395d89b411461017f578063a9059cbb1461019d578063dd62ed3e146101cd57610091565b806306fdde0314610095578063095ea7b3146100b357806318160ddd146100e357806323b872dd14610101575b5f80fd5b61009d6101fd565b6040516100aa919061094e565b60405180910390f35b6100cd60048036038101906100c891906109ff565b610288565b6040516100da9190610a57565b60405180910390f35b6100eb610375565b6040516100f89190610a7f565b60405180910390f35b61011b60048036038101906101169190610a98565b61037b565b6040516101289190610a57565b60405180910390f35b61013961065b565b6040516101469190610b03565b60405180910390f35b61016960048036038101906101649190610b1c565b61066d565b6040516101769190610a7f565b60405180910390f35b610187610682565b604051610194919061094e565b60405180910390f35b6101b760048036038101906101b291906109ff565b61070e565b6040516101c49190610a57565b60405180910390f35b6101e760048036038101906101e29190610b47565b6108a4565b6040516101f49190610a7f565b60405180910390f35b5f805461020990610bb2565b80601f016020809104026020016040519081016040528092919081815260200182805461023590610bb2565b80156102805780601f1061025757610100808354040283529160200191610280565b820191905f5260205f20905b81548152906001019060200180831161026357829003601f168201915b505050505081565b5f8160055f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f20819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925846040516103639190610a7f565b60405180910390a36001905092915050565b60035481565b5f8160045f8673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205410156103fc576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016103f390610c2c565b60405180910390fd5b8160055f8673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205410156104b7576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016104ae90610c94565b60405180910390fd5b8160045f8673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8282546105039190610cdf565b925050819055508160045f8573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8282546105569190610d12565b925050819055508160055f8673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8282546105e49190610cdf565b925050819055508273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040516106489190610a7f565b60405180910390a3600190509392505050565b60025f9054906101000a900460ff1681565b6004602052805f5260405f205f915090505481565b6001805461068f90610bb2565b80601f01602080910402602001604051908101604052809291908181526020018280546106bb90610bb2565b80156107065780601f106106dd57610100808354040283529160200191610706565b820191905f5260205f20905b8154815290600101906020018083116106e957829003601f168201915b505050505081565b5f8160045f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f2054101561078f576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161078690610c2c565b60405180910390fd5b8160045f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8282546107db9190610cdf565b925050819055508160045f8573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f82825461082e9190610d12565b925050819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040516108929190610a7f565b60405180910390a36001905092915050565b6005602052815f5260405f20602052805f5260405f205f91509150505481565b5f81519050919050565b5f82825260208201905092915050565b5f5b838110156108fb5780820151818401526020810190506108e0565b5f8484015250505050565b5f601f19601f8301169050919050565b5f610920826108c4565b61092a81856108ce565b935061093a8185602086016108de565b61094381610906565b840191505092915050565b5f6020820190508181035f8301526109668184610916565b905092915050565b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f61099b82610972565b9050919050565b6109ab81610991565b81146109b5575f80fd5b50565b5f813590506109c6816109a2565b92915050565b5f819050919050565b6109de816109cc565b81146109e8575f80fd5b50565b5f813590506109f9816109d5565b92915050565b5f8060408385031215610a1557610a1461096e565b5b5f610a22858286016109b8565b9250506020610a33858286016109eb565b9150509250929050565b5f8115159050919050565b610a5181610a3d565b82525050565b5f602082019050610a6a5f830184610a48565b92915050565b610a79816109cc565b82525050565b5f602082019050610a925f830184610a70565b92915050565b5f805f60608486031215610aaf57610aae61096e565b5b5f610abc868287016109b8565b9350506020610acd868287016109b8565b9250506040610ade868287016109eb565b9150509250925092565b5f60ff82169050919050565b610afd81610ae8565b82525050565b5f602082019050610b165f830184610af4565b92915050565b5f60208284031215610b3157610b3061096e565b5b5f610b3e848285016109b8565b91505092915050565b5f8060408385031215610b5d57610b5c61096e565b5b5f610b6a858286016109b8565b9250506020610b7b858286016109b8565b9150509250929050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f6002820490506001821680610bc957607f821691505b602082108103610bdc57610bdb610b85565b5b50919050565b7f496e73756666696369656e742062616c616e63650000000000000000000000005f82015250565b5f610c166014836108ce565b9150610c2182610be2565b602082019050919050565b5f6020820190508181035f830152610c4381610c0a565b9050919050565b7f416c6c6f77616e636520657863656564656400000000000000000000000000005f82015250565b5f610c7e6012836108ce565b9150610c8982610c4a565b602082019050919050565b5f6020820190508181035f830152610cab81610c72565b9050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f610ce9826109cc565b9150610cf4836109cc565b9250828203905081811115610d0c57610d0b610cb2565b5b92915050565b5f610d1c826109cc565b9150610d27836109cc565b9250828201905080821115610d3f57610d3e610cb2565b5b9291505056fea2646970667358221220db53408075d895f30ce35bc0daa8a2e4a690cc5f54ab91d47e51ea013c06cc4564736f6c63430008140033"

msg_abi = json.loads('[{"inputs": [{"internalType": "string","name": "newMessage","type": "string"}],"name": "writeMessage","outputs": [],"stateMutability": "nonpayable","type": "function"}]')

token_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_spender","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]')

def log(txt):
    f = open('datarecipeint.txt', "a")
    f.write(txt + '\n')
    f.close()

def sendToken(sender, key, ctraddr, amount, recipient):
    try:
        gasPrice = web3.eth.gas_price
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

def deployToken(sender, key):
    try:
        gasPrice = web3.eth.gas_price
        nonce = web3.eth.get_transaction_count(sender)
        gasAmount = web3.eth.estimate_gas({
            'chainId': chainId,
            'from': sender,
            'data': datatoken,
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        deploytoken_tx = {
            'chainId': chainId,
            'from': sender,
            'data': datatoken,
            'gasPrice': gasPrice,
            'gas': gasAmount,
            'nonce': nonce
        }
        
        #sign & send the transaction
        tx_hash = web3.eth.send_raw_transaction(web3.eth.account.sign_transaction(deploytoken_tx, key).rawTransaction)
        #get transaction hash
        print(f'Processing Deploy Token From {sender} ...')
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Deploy Token Success From {sender} Success!')
        print(f'TX-ID & Token Address : {str(web3.to_hex(tx_hash))} & {transaction_receipt.contractAddress}')
        return transaction_receipt.contractAddress
    except Exception as e:
        print(f'Error : {e}')
        pass

def writeContract(sender, key, ctraddr):
    try:
        gasPrice = web3.eth.gas_price
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
        gasPrice = web3.eth.gas_price
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
        gasPrice = web3.eth.gas_price
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
                    tknaddr = deployToken(sender.address, sender.key)
                    print(f'')
                    sendToken(sender.address, sender.key, tknaddr, amountrandom, recipient.address)
                    print(f'')
    except Exception as e:
        print(f'Error : {e}')
        pass
        
sendTX()
