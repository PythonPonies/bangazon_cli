import sys
import sqlite3

class CustomerStatusManager():
    '''Method: changes user status from inactive to active
        Arguments: user, which indicates which user's status to change. Active = 1, inactive = 0.
        Author: L.Sales, Python Ponies
    '''

    def change_status(self, customer):
        with sqlite3.connect('../bangazon.db') as conn:
            c = conn.cursor()

            try:
                c.execute("UPDATE Customers SET active=0 WHERE active=1")
                c.execute("UPDATE Customers SET active=1 WHERE customer_name = '{}'".format(customer.get_customer_name()))
                c.execute("SELECT active FROM Customers WHERE active=1")
                status = c.fetchall()[0][0]
                return status
            except sqlite3.OperationalError:
                return "There was an error. Please try again."
          
if __name__ == '__main__':
    activeUser = CustomerStatusManager()
    activeUser.change_status("John Doe")