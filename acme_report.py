"""Random Product and Summary Generation"""
from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(num_products=30):
    """Function To Generate List of Products"""
    products = []

    for i in range(num_products):
        adj = sample(ADJECTIVES, 1)
        noun = sample(NOUNS, 1)
        name = adj[0] + ' ' + noun[0]
        price = randint(5, 101)
        weight = randint(5, 101)
        flammability = uniform(0.0, 2.5)

        products.append(Product(name, price, weight, flammability))

    return products


def inventory_report(products):
    """Function To Generate Inventory Report"""
    names = []
    price = []
    weight = []
    flammability = []

    for product in products:
        names.append(product.name)
        price.append(product.price)
        weight.append(product.weight)
        flammability.append(product.flammability)

    unique = set()

    for name in names:
        unique.add(name)

    print('------------------------------------------')
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('------------------------------------------')
    print(f'Unique product names: {len(unique)}')
    print(f'Average price: {sum(price) / len(price)}')
    print(f'Average weight: {sum(weight) / len(weight)}')
    print(f'Average flammability: {sum(flammability) / len(flammability)}')

    if __name__ == '__main__':
        inventory_report(generate_products())
