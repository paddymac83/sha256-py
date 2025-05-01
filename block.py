import hashlib

class Block():
    def __init__(self, data, previous_block):
        self.data = data
        self.previous_hash = previous_block.hash
        self.nonce = 0
        self.hash = hashlib.sha256()

    def mine(self, difficulty):
        self.hash.update(str(self).encode("utf-8"))
        while int(self.hash.hexdigest(), 16) > 2**(256 - difficulty):
            self.nonce += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode("utf-8"))
    
    def __str__(self):
        return "{}{}{}".format(self.previous_block, self.data, self.nonce)

