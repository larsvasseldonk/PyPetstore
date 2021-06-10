'''
This is the main module and provides the whole workflow.

'''

import salie.util
import salie.product
import salie.database
import salie.customer
import salie.order
import salie.orderdetail

db = salie.database.db

if __name__ == '__main__':
    loop = True
    while loop:
        salie.util.print_main_menu()
        choice = input('Enter your choice [1-4]: ')
        # Orders
        if choice == '1':
            orders = True
            while orders:
                salie.util.print_orders_menu()
                orders_input = input('Enter your choice [1-4]: ')
                # View orders
                if orders_input == '1':
                    salie.order.Order.view_orders()
                # Create order
                elif orders_input == '2':
                    customer_id = input('Enter customer_id: ')
                    customer = salie.customer.Customer.search_customer(customer_id)
                    if customer:
                        salie.order.Order(customer[0])
                # Add orderdetails
                elif orders_input == '3':
                    order_id = input('Enter order_id: ')
                    order = salie.order.Order.search_order(order_id)
                    if order:
                        salie.product.Product.view_products()
                        product_id = input('Enter product_id: ')
                        product = salie.product.Product.search_product(product_id)
                        if product:
                            quantity = input('Enter quantity: ')
                            salie.orderdetail.Orderdetail(order_id, product_id, quantity)
                # View order
                elif orders_input == '4':
                    order_id = input('Enter order_id: ')
                    salie.orderdetail.Orderdetail.view_orderdetails(order_id)
                # Back
                elif orders_input == '0':
                    orders = False
                else:
                    print('Not a valid choice. Try again.')
            pass

        # Customers
        elif choice == '2':
            customers = True
            while customers:
                salie.util.print_customers_menu()
                customers_input = input('Enter your choice [1-3]: ')
                # View customers
                if customers_input == '1':
                    salie.customer.Customer.view_customers()
                # Create customer
                elif customers_input == '2':
                    name = input('Enter name: ')
                    email = input('Enter email: ')
                    salie.customer.Customer(name, email)
                # Delete customer
                elif customers_input == '3':
                    customer_id = input('Enter customer_id: ')
                    salie.customer.Customer.delete_customer(customer_id)
                # Back
                elif customers_input == '0':
                    customers = False
                else:
                    print('Not a valid choice. Try again.')
            pass
        
        # Products
        elif choice == '3':
            products = True
            while products:
                salie.util.print_products_menu()
                products_input = input('Enter your choice [1-4]: ')
                # View products
                if products_input == '1':
                    salie.product.Product.view_products()
                # Create product
                elif products_input == '2':
                    name = input('Enter name: ')
                    price = input('Enter price: ')
                    stock = input('Enter stock: ')
                    salie.product.Product(name, price, stock)
                # Delete product
                elif products_input == '3':
                    product_id = input('Enter product_id: ')
                    salie.product.Product.delete_product(product_id)
                # Back
                elif products_input == '0':
                    products = False
                else:
                    print('Not a valid choice. Try again.')
            pass

        # Finance
        elif choice == '4':
            finance = True
            while finance:
                salie.util.print_finance_menu()
                finance_input = input('Enter your choice [1-2]: ')
                # View sales
                if finance_input == '1':
                    pass
                # Back
                elif finance_input == '0':
                    finance = False
                else:
                    print('Not a valid choice. Try again.')
            pass
        
        # Exit
        elif choice == '0':
            db.close_connection()
            loop = False

        else:
            print('Not a valid choice. Try again.')
