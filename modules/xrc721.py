from web3 import Web3
from web3._utils.encoding import (
    hexstr_if_str,
    to_bytes,
)
from decouple import config
import json
from math import pow

rpcUrl = config('NETWORK_URL')

# HTTPProvider:
w3 = Web3(Web3.HTTPProvider(rpcUrl))

# path of abi file
with open('./common/xrc721abi.json') as abiJson:
    xrc721abi = json.load(abiJson)


class XRC721:

    # name of token
    def name(tokenAddr):
        contractInstance = w3.eth.contract(address=tokenAddr, abi=xrc721abi)
        result = contractInstance.functions.name().call()
        return result

    # symbol
    def symbol(tokenAddr):
        contractInstance = w3.eth.contract(address=tokenAddr, abi=xrc721abi)
        result = contractInstance.functions.symbol().call()
        return result

    # ownerOf
    def ownerOf(tokenAddr, tokenId):
        contractInstance = w3.eth.contract(address=tokenAddr, abi=xrc721abi)
        result = contractInstance.functions.ownerOf(tokenId).call()
        return result

    # totalSupply
    def totalSupply(tokenAddr):
        token = Web3.toChecksumAddress(tokenAddr)
        contractInstance = w3.eth.contract(address=token, abi=xrc721abi)
        result = contractInstance.functions.totalSupply().call()
        resultt = str(result)
        return resultt

    # balanceOf
    def balanceOf(tokenAddr, ownerAddress):
        contractInstance = w3.eth.contract(address=tokenAddr, abi=xrc721abi)
        owner = Web3.toChecksumAddress(ownerAddress)
        result = contractInstance.functions.balanceOf(owner).call()
        return result

    # tokenUri
    def tokenURI(tokenAddr, tokenId):
        contractInstance = w3.eth.contract(address=tokenAddr, abi=xrc721abi)
        result = contractInstance.functions.tokenURI(tokenId).call()
        return result

    # tokenByIndex
    def tokenByIndex(tokenAddr, index):
        token = Web3.toChecksumAddress(tokenAddr)
        contractInstance = w3.eth.contract(address=token, abi=xrc721abi)
        result = contractInstance.functions.tokenByIndex(index).call()
        return result

    # token of owner by index
    def tokenofOwnerByIndex(tokenAddr, ownerAddress, index):
        token = Web3.toChecksumAddress(tokenAddr)
        contractInstance = w3.eth.contract(address=token, abi=xrc721abi)
        owner = Web3.toChecksumAddress(ownerAddress)
        result = contractInstance.functions.tokenOfOwnerByIndex(
            owner, index).call()
        return result

    # supportInterface
    def supportInterface(tokenAddr, interfaceId):
        token = Web3.toChecksumAddress(tokenAddr)
        contractInstance = w3.eth.contract(address=token, abi=xrc721abi)
        result = contractInstance.functions.supportsInterface(
            interfaceId).call()
        return result

    # getApproved
    def getApproved(tokenAddr, tokenId):
        contractInstance = w3.eth.contract(address=tokenAddr, abi=xrc721abi)
        result = contractInstance.functions.getApproved(tokenId).call()
        return result

    # Is approve for all
    def isApprovedForAll(tokenAddr, ownerAddress, spenderAddress):
        contractInstance = w3.eth.contract(address=tokenAddr, abi=xrc721abi)
        owner = Web3.toChecksumAddress(ownerAddress)
        spender = Web3.toChecksumAddress(spenderAddress)
        result = contractInstance.functions.isApprovedForAll(
            owner, spender).call()
        return result

    # approve
    def approve(tokenAddr, ownerAddress, ownerPrivateKey,  spenderAddress, tokenId):
        contractInstance = w3.eth.contract(address=tokenAddr, abi=xrc721abi)

        owner = Web3.toChecksumAddress(ownerAddress)
        spender = Web3.toChecksumAddress(spenderAddress)

        approveData = contractInstance.functions.approve(spender, tokenId)

        hexData = approveData._encode_transaction_data()

        data = hexstr_if_str(to_bytes, hexData)

        estimateGas = approveData.estimateGas({
            'from': owner,
        })

        nonce = w3.eth.getTransactionCount(owner)

        gasPrice = w3.eth.gas_price

        tx = {
            'nonce': nonce,
            'to': tokenAddr,
            'data': data,
            'gas': estimateGas,
            'gasPrice': gasPrice,
        }

        signedTx = w3.eth.account.signTransaction(tx, ownerPrivateKey)

        txHash = w3.eth.sendRawTransaction(signedTx.rawTransaction)
        return w3.toHex(txHash)

    # setApproveforall
    def setApprovalForAll(tokenAddr, ownerAddress, ownerPrivateKey,  spenderAddress, boolValue):
        contractInstance = w3.eth.contract(address=tokenAddr, abi=xrc721abi)

        owner = Web3.toChecksumAddress(ownerAddress)
        spender = Web3.toChecksumAddress(spenderAddress)

        approveData = contractInstance.functions.setApprovalForAll(
            spender, boolValue)

        hexData = approveData._encode_transaction_data()

        data = hexstr_if_str(to_bytes, hexData)

        estimateGas = approveData.estimateGas({
            'from': owner,
        })

        nonce = w3.eth.getTransactionCount(owner)

        gasPrice = w3.eth.gas_price

        tx = {
            'nonce': nonce,
            'to': tokenAddr,
            'data': data,
            'gas': estimateGas,
            'gasPrice': gasPrice,
        }

        signedTx = w3.eth.account.signTransaction(tx, ownerPrivateKey)

        txHash = w3.eth.sendRawTransaction(signedTx.rawTransaction)
        return w3.toHex(txHash)

    # transferFrom
    def transferFrom(tokenAddr, ownerAddress, spenderAddress,  spenderPrivateKey, receiver, tokenId):

        contractInstance = w3.eth.contract(address=tokenAddr, abi=xrc721abi)

        owner = Web3.toChecksumAddress(ownerAddress)
        receiverAddres = Web3.toChecksumAddress(receiver)
        spender = Web3.toChecksumAddress(spenderAddress)

        transferData = contractInstance.functions.transferFrom(
            owner, receiverAddres, tokenId)

        estimateGas = transferData.estimateGas({
            'from': spender,
        })

        hexData = transferData._encode_transaction_data()

        data = hexstr_if_str(to_bytes, hexData)

        nonce = w3.eth.getTransactionCount(spender)
        gasPrice = w3.eth.gas_price

        tx = {
            'nonce': nonce,
            'to': tokenAddr,
            'data': data,
            'gas': estimateGas,
            'gasPrice': gasPrice,
        }
        signedTx = w3.eth.account.signTransaction(tx, spenderPrivateKey)

        txHash = w3.eth.sendRawTransaction(signedTx.rawTransaction)
        return w3.toHex(txHash)

    # safeTransferFrom
    def safeTransferFrom(tokenAddr, ownerAddress, spenderAddress,  spenderPrivateKey, receiver, tokenId):

        contractInstance = w3.eth.contract(address=tokenAddr, abi=xrc721abi)

        owner = Web3.toChecksumAddress(ownerAddress)
        receiverAddres = Web3.toChecksumAddress(receiver)
        spender = Web3.toChecksumAddress(spenderAddress)

        transferData = contractInstance.functions.safeTransferFrom(
            owner, receiverAddres, tokenId)

        estimateGas = transferData.estimateGas({
            'from': spender,
        })

        hexData = transferData._encode_transaction_data()

        data = hexstr_if_str(to_bytes, hexData)

        nonce = w3.eth.getTransactionCount(spender)
        gasPrice = w3.eth.gas_price

        tx = {
            'nonce': nonce,
            'to': tokenAddr,
            'data': data,
            'gas': estimateGas,
            'gasPrice': gasPrice,
        }
        signedTx = w3.eth.account.signTransaction(tx, spenderPrivateKey)

        txHash = w3.eth.sendRawTransaction(signedTx.rawTransaction)
        return w3.toHex(txHash)
