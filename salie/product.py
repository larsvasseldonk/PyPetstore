'''
This module provides functions to manage products.

'''

import salie.database

db = salie.database.db

class Product:

    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock
        self.to_db = self.create_product()

    def create_product(self):
        '''Create a product in the database.'''
        c = db.conn.cursor()
        sql = '''INSERT INTO products (name, price, stock) VALUES (?,?,?);'''
        customer = (self.name, self.price, self.stock)
        c.execute(sql, customer)
        db.conn.commit()
        c.close()
        print('Product successfully added to the database.')

    @staticmethod
    def view_products():
        '''This function returns all products inside the inventory.'''
        c = db.conn.cursor()
        data = c.execute('''SELECT * FROM products''').fetchall()
        if data:
            print("(id, 'name', 'price', 'stock')")
            for product in data:
                print(product)
        else:
            print('No products found.')
        c.close()

    @staticmethod
    def delete_product(product_id):
        '''Delete product from the database.'''
        c = db.conn.cursor()
        sql = '''DELETE FROM products WHERE product_id = ?;'''
        c.execute(sql, product_id)
        db.conn.commit()
        c.close()
        print('Product successfully deleted from the database.')

    @staticmethod
    def search_product(product_id):
        '''Search product in the database.'''
        c = db.conn.cursor()
        sql = '''SELECT * FROM products WHERE product_id = ?'''
        data = c.execute(sql, product_id).fetchone()
        if data:
            print('Product found:', data)
        else:
            print('Product does not exist.')
        c.close()
        return data
