'''
This is the main module and provides the whole workflow.

'''

from pypetstore.customer import print_customers_menu, view_customers, create_customer, update_customer, delete_customer
from pypetstore.product import print_products_menu, view_products, create_product, update_product, delete_product
from pypetstore.order import print_orders_menu, view_orders, view_order, create_order, delete_order
from pypetstore.orderdetail import view_orderdetails, create_orderdetails

from pypetstore.util import print_main_menu

# import pypetstore.util
# import pypetstore.product
# import pypetstore.database
# import pypetstore.customer
# import pypetstore.order
# import pypetstore.orderdetail

from pypetstore.database import db

if __name__ == '__main__':
    loop = True
    while loop:
        choice = print_main_menu()
        # Orders
        if choice == '1':
            orders = True
            while orders:
                orders_input = print_orders_menu()
                # View all orders
                if orders_input == '1':
                    view_orders()
                # Create order
                elif orders_input == '2':
                    create_order()
                # Add orderdetails
                elif orders_input == '3':
                    create_orderdetails()
                # View order
                elif orders_input == '4':
                    view_order()
                # Delete order
                elif orders_input == '5':
                    delete_order()
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
                customers_input = print_customers_menu()
                # View customers
                if customers_input == '1':
                    view_customers()
                # Create customer
                elif customers_input == '2':
                    create_customer()
                # Update customer
                elif customers_input == '3':
                    update_customer()
                # Delete customer
                elif customers_input == '4':
                    delete_customer()
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
                products_input = print_products_menu()
                # View products
                if products_input == '1':
                    view_products()
                # Create product
                elif products_input == '2':
                    create_product()
                # Update product
                elif products_input == '3':
                    update_product()
                # Delete product
                elif products_input == '4':
                    delete_product()
                # Back
                elif products_input == '0':
                    products = False
                else:
                    print('Not a valid choice. Try again.')
            pass
        
        # Exit
        elif choice == '0':
            db.close_connection()
            loop = False

        else:
            print('Not a valid choice. Try again.')
