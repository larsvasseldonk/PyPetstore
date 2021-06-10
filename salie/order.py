'''
This module provides functions to manage orders.

'''
import salie.database

db = salie.database.db

class Order:
    def __init__(self, customer_id, status = 'Open'):
        self.customer_id = customer_id
        self.status = status # Open, Cancelled, Closed
        self.to_db = self.create_order()

    def create_order(self):
        c = db.conn.cursor()
        sql = '''INSERT INTO orders (status, customer_id) VALUES (?,?);'''
        order = (self.status, self.customer_id)
        c.execute(sql, order)
        db.conn.commit()
        c.close()
        print('Order successfully added to the database.')

    @staticmethod
    def view_orders():
        '''This function returns all orders.'''
        c = db.conn.cursor()
        data = c.execute('''SELECT * FROM orders''').fetchall()
        if data:
            print("(id, 'status', 'customer_id')")
            for order in data:
                print(order)
        else:
            print('No orders found.')
        c.close()

    @staticmethod
    def search_order(order_id):
        '''Search order in the database.'''
        c = db.conn.cursor()
        sql = '''SELECT * FROM orders WHERE order_id = ?'''
        data = c.execute(sql, order_id).fetchone()
        if data:
            print('Order found:', data)
        else:
            print('Order does not exist.')
        c.close()
        return data