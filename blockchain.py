import hashlib
from datetime import datetime


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        # A block stored with a index and the timestamp
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.create_hash()

    def create_hash(self):
        # Create hash with sha 256bit encryption
        sha = hashlib.sha256()
        sha.update((str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()


def create_genesis_block():
    # A block for starting the block chain
    # Starting block with 0 index
    return Block(0, datetime.now(), "Starting geneis block", "0")


def new_block(previous_block):
    new_block_index = previous_block.index + 1
    new_block_timestamp = datetime.now()
    new_block_data = "Hey. A new block" + str(new_block_index) + "is added."
    previous_block_hash = previous_block.hash
    return Block(new_block_index, new_block_timestamp, new_block_data, previous_block_hash)


