class Transaction:

    def __init__(self, sender, receiver, amount):

        self.sender = sender

        self.receiver = receiver

        self.amount = amount

        self.fee = 0   # Straw Chain has zero gas fees

    def to_dict(self):

        return {

            "from": self.sender,

            "to": self.receiver,

            "amount": self.amount,

            "gas_fee": self.fee

        }
