# import psycopg2
#
#
# class MenuItem:
#     def __init__(self, name=None, price=None):
#         self.name = name
#         self.price = price
#
#     def create_connection(self):
#         HOSTNAME = 'localhost'
#         USERNAME = 'postgres'
#         PASSWORD = 'Famille24'
#         DATABASE = 'restaurant'
#         PORT = '5432'
#
#         connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE, port=PORT)
#
#         return connection
#
#     def save(self, cursor, quey):
#         connection = create_connection()
#         cursor = connection.cursor()
#
#         query = "INSERT INTO menu_item(item_id,name_item,price) VALUES ('{self.name}', {self.price})"
#         cursor.execute(query)
#         results = cursor.fetchall()
#         connection.close()
#
#     def delete(self,cursor,query):
#         connection = create_connection()
#         cursor = connection.cursor()
#
#         query = "delete from menu where name = '{self.name}'"
#         cursor.execute(query)
#         results = cursor.fetchall()
#         connection.close()
#
# item = MenuItem('Burger', 35)
# item.save()

import psycopg2
from tabulate import tabulate

class MenuItem:
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price

    def __open_database(self):
        HOSTNAME = 'localhost'
        USERNAME = 'postgres'
        PASSWORD = 'Famille24'
        DATABASE = 'Restaurant'
        self.connect = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        self.cursor = self.connect.cursor()

    def save(self):
        self.__open_database()
        self.cursor.execute(f"insert into menu(name, price) values ('{self.name}', {self.price}) ")
        self.connect.commit()
        self.connect.close()

    def delete(self):
        self.__open_database()
        self.cursor.execute(f"delete from menu where name = '{self.name}'")
        self.connect.commit()
        self.connect.close()


    def update(self,other_name,other_price):
        self.__open_database()
        self.cursor.execute(f"update menu set price ={other_price}  where name = '{other_name}'")
        self.connect.commit()
        self.connect.close()

    def all(self):
        self.__open_database()
        self.cursor.execute("select * from menu")
        self.connect.commit()
        results = self.cursor.fetchall()
        self.connect.close()
        print(tabulate(results, headers=['id','Name', 'Price']))

    def get_by_name(self,item):
        self.__open_database()
        self.cursor.execute(f"(select * from menu where name ='{item}')")
        item = self.cursor.fetchall()
        if len(item) != 0:
            self.connect.close()
            print(tabulate(item, headers=['id','Name', 'Price']))
            print( )
        else:
            return 'None'

item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Salad', 37)
item.get_by_name('Burger')
item.all()
items = MenuItem().all()
items