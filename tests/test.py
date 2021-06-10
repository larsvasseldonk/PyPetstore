
import unittest

import salie.customer

class TestCustomer(unittest.TestCase):
    def test_customer(self):
        customer = salie.customer.Customer('XX', 'xx@xx.com')
        self.assertIsInstance(customer, salie.customer.Customer)

if __name__ == '__main__':
    unittest.main()