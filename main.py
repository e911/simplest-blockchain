from blockchain import create_genesis_block, new_block


def create_blockchain():
    # Our block chain is a list
    blockchain=[create_genesis_block()]
    previous_block=blockchain[0]

    # Total blocks in chain
    number_of_blocks = 20

    for each_block in range(0, number_of_blocks):
        next_block = new_block(previous_block)
        blockchain.append(next_block)
        previous_block = next_block

        # Print details
        print("New block: Block {} added!! ".format(previous_block.index))
        print("Block data: {}".format(previous_block.data))
        print("Block hash: {}".format(previous_block.hash))


if __name__ == '__main__':
    create_blockchain()
