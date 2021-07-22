'''
This module provides functions manage the database.

'''

import sqlite3
from sqlite3 import Error

import os

sql_create_customers_table = ''' CREATE TABLE IF NOT EXISTS customers (
                                    customer_id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    email text,
                                    address text
                                ); '''

sql_create_orders_table = ''' CREATE TABLE IF NOT EXISTS orders (
                                    order_id integer PRIMARY KEY,
                                    status text,
                                    customer_id integer,
                                    FOREIGN KEY (customer_id)
                                        REFERENCES customers (customer_id)
                                ); '''

sql_create_products_table = '''CREATE TABLE IF NOT EXISTS products (
                                    product_id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    price real DEFAULT 0.00,
                                    stock integer DEFAULT 0
                                ); '''

sql_create_orderdetails_table = '''CREATE TABLE IF NOT EXISTS orderdetails (
                                        orderdetail_id integer PRIMARY KEY,
                                        quantity integer,
                                        order_id integer,
                                        product_id integer,
                                        FOREIGN KEY (order_id)
                                            REFERENCES orders (order_id),
                                        FOREIGN KEY (product_id)
                                            REFERENCES products (product_id)
                                    ); '''

class Database:
    def __init__(self):
        self.name = 'PyPetstore Database'
        self.db_file = os.path.join(os.getcwd(), 'data' + os.sep + 'pypetstore.db')
        self.conn = self.create_connection()
        self.tables = self.create_tables()

    def create_connection(self):
        '''Create the database connection to the SQLite database.'''
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            print('Succesfully connected to the database.')
            return conn
        except Error as e:
            print(e)

        return conn

    def create_tables(self):
        '''Create the SQLite tables.'''
        if self.conn:
            try:
                c = self.conn.cursor()
                # Create customers table
                c.execute(sql_create_customers_table)
                # Create orders table
                c.execute(sql_create_orders_table)
                # Create produts table
                c.execute(sql_create_products_table)
                # Create orderdetails table
                c.execute(sql_create_orderdetails_table)
                # Commit database
                self.conn.commit()
                c.close()
            except Error as e:
                print(e)
        else:
            print('Connection to the database failed.')


    def close_connection(self):
        '''Close the database connection.'''
        if self.conn:
            self.conn.close()

db = Database()