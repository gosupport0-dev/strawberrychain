from chain import StrawChain

from wallet import create_wallet

print("🍓 Starting Straw Chain...")

print("🍓 Strawberry Token (STRAW)")

print("⛽ Gas Fees: 0")

straw = StrawChain()

creator = create_wallet("strawberry_creator")

user = create_wallet("user_wallet")

# Create supply

straw.mint(

    creator,

    1000000000

)

print("Total Supply: 1,000,000,000 STRAW")

# Send tokens

print(

    straw.send(

        creator,

        user,

        500

    )

)

print("\nWallet balances:")

print(straw.balances)

print("\nBlockchain:")

straw.show_chain()
