from modules.xrc721 import XRC721

token721 = '0xb9E382185F5F9AfD07BEBAE25447632B6c61E6ED'

tokenId = 88

# token3 = '0x94405c8749057d13778fb6aad0ec6b9569e80268'
# token3owner = '0xd19a435dfa78386e728e7444287f2f2d0b78d110'
# tokenId3 = 2088


index = 0

owner = '0xcd0d8f3c097fb77a5f079e400881599ec4b36fbb'

ownerpriavte = '660d80db20b3d5f07849fa47f9d60090b976ebc120cd19fa0615acfa675fe440'

spender = '0x0c833ab94f64c0f3fd5ce273f9db31f8a2185939'

spenderPrivate = 'f78f241d00719adddf391f8dab88dd15d33c54bae09c548a2fe2ed1e635199a8'

receiver = '0xd55fec67b56bcfcfcd8229ec21558af15bcc3e79'

receiverPrivate = '292c60e78b78c11332262cdb2a9104218f2f4ba8c6ccdaf58651d10437280b9e'

interfaceId = '0x80ac58cd'

boolValue = True

a = XRC721.name(token721)
# a = XRC721.symbol(token721)
# a = XRC721.ownerOf(token721, tokenId)
# a = XRC721.totalSupply(token3)
# a = XRC721.balanceOf(token721, owner)
# a = XRC721.tokenURI(token721, tokenId)
# a = XRC721.tokenByIndex(token, index)

# a = XRC721.tokenofOwnerByIndex(token3, token3owner, index)

# a = XRC721.supportInterface(token3, interfaceId)

# will return address who has approve
# a = XRC721.getApproved(token721, tokenId)

# will return true of false
# a = XRC721.isApprovedForAll(token721, owner, spender)

# a = XRC721.approve(token721, receiver, receiverPrivate, spender, tokenId)

# a = XRC721.setApprovalForAll(
#     token721, owner, ownerpriavte, spender, boolValue)

# a = XRC721.transferFrom(token721, owner, spender,
#                         spenderPrivate, receiver, tokenId)

# a = XRC721.safeTransferFrom(
#     token721, receiver, spender, spenderPrivate, owner, tokenId)


print(a)
