import hashlib

class Chain():
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []
        self.pool = []

    def proof_of_work(self, block):
        hash = hashlib.sha256()
        hash.update(str(block).encode("utf-8"))

        return (block.hash.hexdigest() == hash.hexdigest() and 
        int(hash.hexdigest(), 16) < 2**(256 - self.difficulty) and
        block.previous_hash == block[-1].hash)
    
    def add_to_chain(self, block):
        if self.proof_of_work(block):
            self.blocks.append(block)