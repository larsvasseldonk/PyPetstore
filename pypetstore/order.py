'''
This module provides functions to manage orders.

'''

from salie.customer import Customer
from salie.orderdetail import view_orderdetails

from salie.database import db

class Order:
    def __init__(self, customer, status = 'Open'):
        self.id = None
        self.customer_id = customer.get_id()
        self.customer_name = customer.get_name()
        self.customer_email = customer.get_email()
        self.status = status # Open, Cancelled, Closed

    def set_id(self, id):
        self.id = str(id)

    def get_id(self):
        return self.id

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def to_db(self, action='insert'):
        c = db.conn.cursor()
        if action == 'update':
            if self.id:
                sql = '''UPDATE orders SET status=? WHERE order_id=?;'''
                order = (self.status, self.id)
                print('Order updated to the database.')
        elif action == 'delete':
            sql = '''DELETE FROM orders WHERE order_id=?;'''
            order = (self.id)
            print('Order deleted from the database.')
        elif action == 'insert':
            sql = '''INSERT INTO orders (status, customer_id) VALUES (?,?);'''
            order = (self.status, self.customer_id)
            print('Order added to the database.')
        c.execute(sql, order)
        db.conn.commit()
        c.close()

    def print_nicely(self, header=True):
        if header:
            print('{:<8} {:<15} {:<10} {:<10}'.format('Id','Customer Name','Customer Id','Status'))
        print('{:<8} {:<15} {:<10} {:<10}'.format(self.get_id(), self.customer_name, self.customer_id, self.get_status()))

    @staticmethod
    def search_order(order_id):
        '''Search order in the database.'''
        c = db.conn.cursor()
        sql = '''SELECT * FROM orders WHERE order_id = ?'''
        data = c.execute(sql, str(order_id)).fetchone()
        if data:
            customer = Customer.search_customer(data[2])
            if customer:
                order = Order(customer, data[1])
                order.set_id(data[0])
        else:
            order = None
            print('Order does not exist.')
        c.close()
        return order

def view_orders():
    '''This function returns all orders.'''
    c = db.conn.cursor()
    data = c.execute('''SELECT * FROM orders''').fetchall()
    if data:
        # print("(id, 'status', 'customer_id')")
        print('{:<8} {:<15} {:<10} {:<10}'.format('Id','Customer Name','Customer Id','Status'))
        for each in data:
            order = Order.search_order(each[0])
            order.print_nicely(header=False)
    else:
        print('No orders found.')
    c.close()

def view_order():
    order_id = input('Enter order_id: ')
    order = Order.search_order(order_id)
    if order:
        order.print_nicely()
        view_orderdetails(order_id)

def create_order():
    customer_id = input('Enter customer_id: ')
    customer = Customer.search_customer(customer_id)
    if customer:
        order = Order(customer)
        order.to_db()
        print(f'Order {order.get_id()} successfully created.')

def delete_order():
    order_id = input('Enter order_id: ')
    order = Order.search_order(order_id)
    if order:
        order.to_db(action='delete')
        print(f'Order {order.get_id()} successfully deleted.')

def print_orders_menu():
    '''This function prints the orders menu.'''
    print('\n-- Orders --\n')
    print('1. View all orders')
    print('2. Create order')
    print('3. Add orderdetails')
    print('4. View order')
    print('5. Delete order')
    print('0. Back\n')
    return input('Enter your choice [1-5]: ')