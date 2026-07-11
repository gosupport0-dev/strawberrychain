import hashlib

import json

import time

class Block:

    def __init__(self, index, transactions, previous_hash):

        self.index = index

        self.timestamp = time.time()

        self.transactions = transactions

        self.previous_hash = previous_hash

        self.hash = self.make_hash()

    def make_hash(self):

        data = json.dumps({

            "index": self.index,

            "timestamp": self.timestamp,

            "transactions": self.transactions,

            "previous_hash": self.previous_hash

        }, sort_keys=True)

        return hashlib.sha256(data.encode()).hexdigest()
