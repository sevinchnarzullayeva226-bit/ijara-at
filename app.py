flats = []

def add_flat(address, rooms, price):
    flats.append({"address": address, "rooms": rooms, "price": price})

def list_flats():
    for i, f in enumerate(flats, 1):
        print(i, f["address"], f["rooms"], f["price"])
