def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
