import hashlib

class Block():
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = hashlib.sha256()

    def mine(self, difficulty):
        # updates the sha256() init hash with __str__ which is the data + nonce + previous hash
        self.hash.update(str(self).encode("utf-8"))
        while int(self.hash.hexdigest(), 16) > 2**(256 - difficulty):  # PoW
            self.nonce += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode("utf-8"))  # re-hash with the updated hash
    
    def __str__(self):
        # returns the previous block (and its hash) and appends the current data and nonce
        return "{}{}{}".format(self.previous_hash.hexdigest(), self.data, self.nonce)

