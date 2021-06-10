'''
This module provides functions to manage customers.

'''

import salie.database

db = salie.database.db

class Customer:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.address = None
        self.to_db = self.create_customer()

    def create_customer(self):
        '''Create a customer in the database.'''
        c = db.conn.cursor()
        sql = '''INSERT INTO customers (name, email) VALUES (?,?);'''
        customer = (self.name, self.email)
        c.execute(sql, customer)
        db.conn.commit()
        c.close()
        print('Customer added to the database.')

    def edit_customer(self):
        c = db.conn.cursor()
        sql = '''UPDATE customers SET name = ?, email = ? WHERE customer_id = ?;'''
        customer = (self.name, self.email)
        c.execute(sql, customer)
        db.conn.commit() 
        c.close()

    @staticmethod
    def view_customers():
        '''This function returns all customers.'''
        c = db.conn.cursor()
        data = c.execute('''SELECT * FROM customers''').fetchall()
        if data:
            print("(id, 'name', 'email', 'address')")
            for customer in data:
                print(customer)
        else:
            print('No customers found.')
        c.close()

    @staticmethod
    def delete_customer(customer_id):
        '''Delete customer from the database.'''
        c = db.conn.cursor()
        sql = '''DELETE FROM customers WHERE customer_id = ?;'''
        c.execute(sql, customer_id)
        db.conn.commit()
        c.close()
        print('Customer successfully deleted from the database.')

    @staticmethod
    def search_customer(customer_id):
        '''Search customer in the database.'''
        c = db.conn.cursor()
        sql = '''SELECT * FROM customers WHERE customer_id = ?'''
        data = c.execute(sql, customer_id).fetchone()
        if data:
            print('Customer found:', data)
        else:
            print('Customer does not exist.')
        c.close()
        return data # data is None when customer is not found