from acme import Product
import random


adj = ['useful', 'cute', 'decent', 'strong', 'boring', 'federal',
       'pure', 'suitable', 'practical', 'sacred']

noun = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', 'Bowlingball', 'Elephant',
        'Crane', 'Computer', 'Train', 'Blanket']


# random.choice(seq)

def generate_products(n=30):
    '''Generate n random pruducts using product_list
    '''\
    # Begin with enpty list
    products = []
    prod_names = []
    c = 0

    while c < (n+1):
        synth = random.choice(adj) + ' ' + random.choice(noun)
        prod_names.append(synth)
        c = c+1

    for _ in list(range(n)):
        product = Product(name=random.sample(prod_names, k=1),
                          price=random.randint(5, 100),
                          weight=random.randint(5, 100),
                          flammability=random.uniform(0, 2.5))
        products.append(product)

    return products


# NOT DONE... PICK UP HERE...
def inventory_report(products):
    names = []
    prices = []
    weights = []
    flames = []
    gs = generate_products()
    for g in gs:
        names.append(g.name)
        prices.append(g.price)
        weights.append(g.weight)
        flames.append(g.flammability)
    print('Number of Unique Products', len(names))
    print('Average Price: ', sum(prices) / len(prices))
    print('Average Weight: ', sum(weights) / len(weights))
    print('Average Flammability', sum(flames) / len(flames))

    # print('Number of Unique Products:', len(products))
    # print('Average Price: ', mean(products[]))


if __name__ == '__main__':
    inventory_report(generate_products())
