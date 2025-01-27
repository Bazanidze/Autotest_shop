def normal_price_product(price_product):
    price_product = price_product[0:-1]
    new_price_product = ""
    for sym in price_product:
        symbol = ","
        if symbol == sym:
            symbol = "."
            new_price_product += symbol
        else:
            new_price_product += sym
    new_price_product = float(new_price_product)
    return new_price_product
