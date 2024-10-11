
# # items = [
# #         {"id":"83b82413-c636-44cd-976a-da63b515e61e", 
# #                     "item":{
# #                             "name" : "apple juice",
# #                             "price": 100
# #                             }
# #         },
# #         {"id":"5945d473-eec6-40f5-a75c-477978b01eca",
# #                     "item":{
# #                             "name" : "bloodey marry",
# #                             "price" : 50
# #                             }
# #         }   
# # ]

## it is datastructre we used but now we will create a database, these code will connect to the database.





import pyodbc


class ItemDatabase:
    def __init__(self):
        """
            create a connection with our database
            SERVER will be the host name provided by the server, when app is deployed online.
            
        """
        self.conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=DESKTOP-F27P7II;DATABASE=cafe;',timeout=30)  # timeout (Optional): Increase the timeout value if needed becz of network latency issues and server response timeout.
        self.cursor = self.conn.cursor()

    # get all items
    def get_items(self):
        query = "SELECT * FROM item"
        self.cursor.execute(query)
        items = []
        for row in self.cursor.fetchall():
            item_dic = {}
            item_dic["id"] = row[0]
            item_dic["name"] = row[1]
            item_dic["price"] = row[2]
            items.append(item_dic)
        return items
    
    # get item by id
    def get_item(self, item_id):
        query = f"SELECT * FROM item WHERE id ='{item_id}'"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dic = {}
            item_dic["id"] = row[0]
            item_dic["name"] = row[1]
            item_dic["price"] = row[2]
            return [item_dic]
        
    
    # add an item
    def add_item(self, id, body):
        query = f"insert into item (id,name, price) values('{id}', '{body['name']}', {body['price']})"
        self.cursor.execute(query) #it give view of executed (query) not commits the changes
        self.conn.commit()  # commit the transaction to save the changes

    
    # update an item
    def update_item(self, id, body):
        query = f"UPDATE item SET price = {body['price']}, name = '{body['name']}' WHERE id = '{id}';"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        self.conn.commit()
        return True

    
    # delete an item
    def delete_item(self, id):
        query = f"DELETE FROM item WHERE id='{id}';"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        self.conn.commit()
        return True



# db = ItemDatabase()
# (db.add_item('83b824c63644cd976ada63b515p87L', {'name':'badam shake', 'price':60}))
# print(db.get_items())
