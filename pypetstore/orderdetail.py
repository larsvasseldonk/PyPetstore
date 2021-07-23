'''
This module provides functions to manage orderdetails.

'''

# from pypetstore.order import Order

import pypetstore.order
from pypetstore.product import Product, view_products

from pypetstore.database import db

class Orderdetail:
    def __init__(self, order, product, quantity: int):
        self.id = None
        self.order_id = order.get_id()
        self.product_id = product.get_id()
        self.product_name = product.get_name()
        self.unit_costs = product.get_price()
        self.total_costs = float(self.unit_costs) * float(quantity)
        self.quantity = int(quantity)
        product.set_stock(product.get_stock() - self.quantity)
        product.to_db(action='update')

    def set_id(self, id):
        self.id = str(id)

    def get_id(self):
        return self.id

    def to_db(self):
        '''Create an orderdetail in the database.'''
        c = db.conn.cursor()
        sql = '''INSERT INTO orderdetails (quantity, order_id, product_id) VALUES (?,?,?);'''
        orderdetail = (self.quantity, self.order_id, self.product_id)
        c.execute(sql, orderdetail)
        db.conn.commit()
        c.close()
        print('Orderdetail successfully added to the database.')

    def print_nicely(self, header=True):
        if header:
            print('{:<5} {:<10} {:<5} {:<5}'.format('Order Id', 'Product name', 'Unit costs', 'Quantity'))
        print('{:<5} {:<10} {:<5} {:<5}'.format(self.order_id, self.product_name, self.unit_costs, self.quantity))

    @staticmethod
    def search_orderdetail(orderdetail_id):
        '''Search order details in the database.'''
        c = db.conn.cursor()
        sql = '''SELECT * FROM orderdetails WHERE orderdetail_id = ?'''
        data = c.execute(sql, str(orderdetail_id)).fetchone()
        if data:
            order = pypetstore.order.Order.search_order(data[2])
            product = Product.search_product(data[3])
            if order and product:
                orderdetail = Orderdetail(order, product, data[1])
                orderdetail.set_id(data[0])
            else:
                print('Product or order not found.')
        else:
            orderdetail = None
            print('Orderdetail does not exist.')
        c.close()
        return orderdetail


def view_orderdetails(order_id):
    '''Print orderdetails of an order.'''
    if pypetstore.order.Order.search_order(order_id):
        c = db.conn.cursor()
        sql = '''SELECT od.orderdetail_id, od.order_id, od.quantity, p.name, c.name
                    FROM orderdetails as od 
                    INNER JOIN products as p
                        ON p.product_id = od.product_id
                    INNER JOIN orders as o
                        ON o.order_id = od.order_id
                    INNER JOIN customers as c
                        ON c.customer_id = o.customer_id
                    WHERE od.order_id = ?'''
        data = c.execute(sql, order_id).fetchall()
        if data:
            # print("(id, 'order_id', 'quantiy', 'product', 'customer')")
            print('{:<5} {:<10} {:<5} {:<5}'.format('Order Id', 'Product name', 'Unit costs', 'Quantity'))
            for each in data:
                orderdetail = Orderdetail.search_orderdetail(each[0])
                orderdetail.print_nicely(header=False)
        else:
            print('Order does not have any details.')
        c.close()

def create_orderdetails():
    order_id = input('Enter order_id: ')
    order = pypetstore.order.Order.search_order(order_id)
    if order:
        view_products()
        product_id = input('Enter product_id: ')
        product = Product.search_product(product_id)
        if product:
            quantity = input('Enter quantity: ')
            orderdetail = Orderdetail(order, product, quantity)
            orderdetail.to_db()
            print(f'Product {product.get_name()} with id {product.get_id()} successfully added to Order {order.get_id()}.')
            
class Test():
    def __init__(self, name):
        self.name = name
        
    def foo():
        def hello():
            pass
        hello()
            
def test_3():
    pass
    
def test_1():
    test_3()
    def test_nested():
        create_orderdetails()
        def test_4():
            pass
        test_4()
    test_nested()
    

# Does test_1 also include test_nested dependencies?