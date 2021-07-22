'''
This module provides functions to manage products.

'''

from salie.database import db

class Product:

    def __init__(self, name, price, stock=0):
        self.id = None
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def set_id(self, id):
        self.id = str(id)

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_price(self, price):
        self.price = float(price)

    def get_price(self):
        return self.price

    def set_stock(self, stock):
        self.stock = int(stock)

    def get_stock(self):
        return self.stock

    def to_db(self, action='insert'):
        '''Insert, update or delete product in the database.'''
        c = db.conn.cursor()
        if action == 'update':
            if self.id:
                sql = '''UPDATE products SET name=?, price=?, stock=? WHERE product_id=?;'''
                product = (self.name, self.price, self.stock, self.id)
        elif action == 'delete':
            sql = '''DELETE FROM products WHERE product_id = ?;'''
            product = (self.id)
        elif action == 'insert':
            sql = '''INSERT INTO products (name, price, stock) VALUES (?,?,?);'''
            product = (self.name, self.price, self.stock)
        c.execute(sql, product)
        db.conn.commit()
        c.close()

    def print_nicely(self, header=True):
        if header:
            print('{:<5} {:<10} {:<5} {:<5}'.format('Id','Name','Price', 'Stock'))
        print('{:<5} {:<10} {:<5} {:<5}'.format(self.id, self.name, self.price, self.stock))

    @staticmethod
    def search_product(product_id):
        '''Search product in the database.'''
        c = db.conn.cursor()
        sql = '''SELECT * FROM products WHERE product_id = ?'''
        data = c.execute(sql, str(product_id)).fetchone()
        product = None
        if data:
            product = Product(data[1], data[2], data[3])
            product.set_id(data[0])
        else:
            print('Product does not exist.')
        c.close()
        return product

def view_products():
    '''This function returns all products inside the inventory.'''
    c = db.conn.cursor()
    data = c.execute('''SELECT * FROM products''').fetchall()
    if data:
        print('{:<5} {:<10} {:<5} {:<5}'.format('Id','Name','Price', 'Stock'))
        for each in data:
            product = Product.search_product(each[0])
            product.print_nicely(header=False)
    else:
        print('No products found.')
    c.close()

def create_product():
    name = input('Enter name: ')
    price = input('Enter price: ')
    stock = input('Enter stock: ')
    product = Product(name, price, stock)
    product.to_db()
    print(f'Product with id {product.get_id()} succesfully created.')

def update_product():
    product_id = input('Enter product_id: ')
    product = Product.search_product(product_id)
    if product:
        name = input('Enter new name: ')
        price = input('Enter new price: ')
        stock = input('Enter new stock: ')
        product.set_name(name)
        product.set_price(price)
        product.set_stock(stock)
        product.to_db(action='update')
        print(f'Product with id {product.get_id()} successfully updated.')

def delete_product():
    product_id = input('Enter product_id: ')
    product = Product.search_product(product_id)
    if product:
        product.to_db(action='delete')
        print(f'Product {product.get_id()} successfully deleted.')

def print_products_menu():
    '''This function prints the products menu.'''
    print('\n-- Products --\n')
    print('1. View all products')
    print('2. Create product')
    print('3. Update product')
    print('4. Delete product')
    print('0. Back\n')
    return input('Enter your choice [1-4]: ')
