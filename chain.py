from block import Block

from transaction import Transaction

class StrawChain:

    def __init__(self):

        self.chain = [self.create_genesis()]

        self.balances = {}

    def create_genesis(self):

        return Block(

            0,

            [{"message": "Welcome to Straw Chain 🍓"}],

            "0"

        )

    def latest_block(self):

        return self.chain[-1]

    def mint(self, wallet, amount):

        self.balances[wallet] = self.balances.get(wallet, 0) + amount

    def send(self, sender, receiver, amount):

        if self.balances.get(sender, 0) < amount:

            return "Not enough Strawberry Token"

        tx = Transaction(

            sender,

            receiver,

            amount

        )

        self.balances[sender] -= amount

        self.balances[receiver] = self.balances.get(receiver, 0) + amount

        block = Block(

            len(self.chain),

            [tx.to_dict()],

            self.latest_block().hash

        )

        self.chain.append(block)

        return "🍓 Transaction complete"

    def show_chain(self):

        for block in self.chain:

            print(block.__dict__)
