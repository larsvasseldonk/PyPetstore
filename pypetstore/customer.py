'''
This module provides functions to manage customers.

'''

from pypetstore.database import db

class Customer:

    def __init__(self, name, email):
        self.id = None
        self.name = name
        self.email = email
        self.address = None

    def set_id(self, id):
        self.id = str(id)

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def to_db(self, action='insert'):
        '''Insert or update the customer in the database.'''
        c = db.conn.cursor()
        if action == 'update':
            if self.id:
                sql = '''UPDATE customers SET name=?, email=? WHERE customer_id=?;'''
                customer = (self.name, self.email, self.id)
                print('Customer updated to the database.')
        elif action == 'delete':
            sql = '''DELETE FROM customers WHERE customer_id=?;'''
            customer = (self.id)
        elif action == 'insert':
            sql = '''INSERT INTO customers (name, email) VALUES (?,?);'''
            customer = (self.name, self.email)
            print('Customer added to the database.')
        c.execute(sql, customer)
        db.conn.commit()
        c.close()

    def print_nicely(self, header=True):
        if header:
            print('{:<5} {:<10} {:<15}'.format('Id','Name','Email'))
        print('{:<5} {:<10} {:<15}'.format(self.get_id(), self.get_name(), self.get_email()))

    @staticmethod
    def search_customer(customer_id):
        '''Search customer in the database.'''
        c = db.conn.cursor()
        sql = '''SELECT * FROM customers WHERE customer_id = ?'''
        data = c.execute(sql, str(customer_id)).fetchone()
        customer = None
        if data:
            customer = Customer(data[1], data[2])
            customer.set_id(data[0])
        else:
            print('Customer does not exist.')
        c.close()
        return customer # data is None when customer is not found

def view_customers():
    '''This function returns all customers.'''
    c = db.conn.cursor()
    data = c.execute('''SELECT * FROM customers''').fetchall()
    if data:
        print('{:<5} {:<10} {:<15}'.format('Id','Name','Email'))
        for each in data:
            customer = Customer.search_customer(each[0])
            customer.print_nicely(header=False)
    else:
        print('No customers found.')
    c.close()

def create_customer():
    name = input('Enter name: ')
    email = input('Enter email: ')
    customer = Customer(name, email)
    customer.to_db()
    print(f'Customer succesfully created.')

def update_customer():
    customer_id = input('Enter customer_id: ')
    customer = Customer.search_customer(customer_id)
    if customer:
        name = input('Enter new name: ')
        email = input('Enter new email: ')
        customer.set_name(name)
        customer.set_email(email)
        customer.to_db(action='update')
        print(f'Customer {customer.get_id()} successfully updated.')

def delete_customer():
    customer_id = input('Enter customer_id: ')
    customer = Customer.search_customer(customer_id)
    if customer:
        customer.to_db(action='delete')
        print(f'Customer {customer.get_id()} successfully deleted.')

def print_customers_menu():
    '''This function prints the customers menu.'''
    print('\n-- Customers --\n')
    print('1. View all customers')
    print('2. Create customer')
    print('3. Update customer')
    print('4. Delete customer')
    print('0. Back\n')
    return input('Enter your choice [1-4]: ')