from modules.xrc20 import XRC20


# tokenAddress = '0x167e25A843f66B7A08676CaAb299b5Fc48Bd5263'

# ownerAddr = '0xd55fec67b56bcfcfcd8229ec21558af15bcc3e79'

# ownerPrivate = '292c60e78b78c11332262cdb2a9104218f2f4ba8c6ccdaf58651d10437280b9e'

# spender = '0x3a82257d9fe0bff2d3ae3665ffce6e57239c3f56'

# spenderprivate = 'a53d7a88720a32d50e35ea1c143c2b8278188b0d16ca00f4a010faced47dbf79'

# receiver = '0xcd0d8f3c097fb77a5f079e400881599ec4b36fbb'


token20 = '0xA2F80aceFfc0a74FA1c38706Df5d65998590484c'

owner = '0x13fF5E7D23E676aCbDA9942c5dA7fee3a22df0Df'

privateofowner = '92243ded48e2f263dc88b61f15915f220cb77c4c8eeff822ef4196a7fc7c5de0'

spender = '0xd0d1158cf0c1c4a9346645a694f2e0419418ea88'

spenderprivate = 'ce68b8f55c19f752a04b673c9c400008d4cace97a7a184b9cb6b3118a6d8bc2d'

receiver = '0x13441e18a2da86830a47b212c76e7f8ae0fbe3f3'

receiverPrivate = 'bc635344409bff0769116bbce590a98a4a6247f6c0cdadaeeee4be1315ebf30d'

account4 = '0x179d92c28c170f629391e13c891d0db0fec3e96d'

account4private = 'b4cdc4980bee76ed6d380b4aaf8138b0784205f941af39d3bfdfec94e38041c2'

amount = 5


# a = XRC20.decimal(tokenAddress)

# a = XRC20.totalSupply(tokenAddress)

# a = XRC20.symbol(tokenAddress)

a = XRC20.balanceOf(token20, owner)

# a = XRC20.name(token20)

TokenAddress = '0x167e25A843f66B7A08676CaAb299b5Fc48Bd5263'
OwnerAddress = '0xd55fec67b56bcfcfcd8229ec21558af15bcc3e79'
SpenderAddress = '0x3a82257d9fe0bff2d3ae3665ffce6e57239c3f56'

a = XRC20.allowance(TokenAddress, OwnerAddress, SpenderAddress)

# a = XRC20.getApprove(token20, owner, privateofowner, spender, amount)

# a = XRC20.transferXDC(owner, spender, privateofowner, amount)

# a = XRC20.transferToken(token20, owner,
#                         privateofowner, spender, amount)
# a = XRC20.increaseAllowance(token20, owner,
#                             privateofowner, spender, amount)
# a = XRC20.decreaseAllowance(token20, owner,
#                             privateofowner, spender, amount)

# a = XRC20.transferFrom(token20, owner,
#                        spenderprivate, spender, receiver, amount)

print(a)
