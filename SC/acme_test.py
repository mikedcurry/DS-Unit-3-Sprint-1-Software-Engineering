import random
import unittest
from acme import Product
from acme_report import generate_products, adj, noun


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_explode(self):
        """Test if the product will actually explode it ratio is high"""
        prod = Product('Test Product', weight=20, flammability=20)
        self.assertEqual(prod.explode, '...BABOOOOMMMm!!!!')

    def test_stealage(self):
        prod = Product('Test Product', price=20, weight=1)
        self.assertEqual(prod.stealability, 'Very stealable!')


# Need to finish the acme_report first before returning to this...
class AcmeReportTests(unittest.TestCase):
    """Tests the Acme Report"""
    def test_default_num_products(self):
        g = generate_products()
        self.assertEqual(len(g), 30)

# I created my orignial list diferently than the instructions presuposes...
    def test_legal_names(self):
        prod_names = []
        c = 0
        while c < 30:     # Because it is default I can assume it's 30 here...
            synth = random.choice(adj), ' ', random.choice(noun)
            prod_names.append(synth)
            c = c+1
        names = []
        gs = generate_products()
        for g in gs:
            names.append(g.name)
        for name in names:
            self.assertIn(names, prod_names)

if __name__ == '__main__':
    unittest.main()
