flats = []

def add_flat(address, rooms, price):
    flats.append({"address": address, "rooms": rooms, "price": price})

def list_flats():
    for i, f in enumerate(flats, 1):
        print(i, f["address"], f["rooms"], f["price"])

tenants = []

def add_tenant(name, flat_id):
    tenants.append({"name": name, "flat": flat_id})
