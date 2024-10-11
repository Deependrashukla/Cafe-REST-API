

import pyodbc

class UserDatabase:
    def __init__(self):
        self.conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=DESKTOP-F27P7II;DATABASE=cafe;',timeout=30)  # timeout (Optional): Increase the timeout value if needed becz of network latency issues and server response timeout.
        self.cursor = self.conn.cursor()

    # get all users
    def get_user(self, id):
        query = f"SELECT * FROM users  WHERE id = {id};"
        self.cursor.execute(query)
        user_dict = {}
        result = self.cursor.fetchone()
        if result is not None:
            user_dict['id'], user_dict['username'], user_dict['password'] = result
            return user_dict
    
    
    # add an user
    def add_user(self, username, password):
        query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}');"
        try:
            self.cursor.execute(query)
            self.conn.commit()  
            return True
        except Exception:
            return False

    
    # delete an user
    def delete_user(self, id):
        query = f"DELETE FROM users WHERE id = {id};"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        self.conn.commit()
        return True
    
    def verify_user(self, username, password):
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result is not None:
            return result[0]
        
        


# db = UserDatabase()
# (db.delete_user(2))
# print(db.get_user(1))
