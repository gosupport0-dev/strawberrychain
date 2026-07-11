import hashlib

def create_wallet(name):

    return hashlib.sha256(name.encode()).hexdigest()
