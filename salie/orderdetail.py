'''
This module provides functions to manage orderdetails.

'''

import salie.database
import salie.order

db = salie.database.db

class Orderdetail:
    def __init__(self, order_id, product_id, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.to_db = self.create_orderdetail()

    def create_orderdetail(self):
        '''Create an orderdetail in the database.'''
        c = db.conn.cursor()
        sql = '''INSERT INTO orderdetails (quantity, order_id, product_id) VALUES (?,?,?);'''
        orderdetail = (self.quantity, self.order_id, self.product_id)
        c.execute(sql, orderdetail)
        db.conn.commit()
        c.close()
        print('Orderdetail successfully added to the database.')

    @staticmethod
    def view_orderdetails(order_id):
        '''Print orderdetails of an order.'''
        if salie.order.Order.search_order(order_id):
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
                print("(id, 'order_id', 'quantiy', 'product', 'customer')")
                for orderdetail in data:
                    print(orderdetail)
            else:
                print('Order does not have any details.')
            c.close()