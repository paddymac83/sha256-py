from block import Block

block = Block("Hello World!")
block.mine(20)
print(block.hash.hexdigest())
print(block.nonce)
print(block.data)