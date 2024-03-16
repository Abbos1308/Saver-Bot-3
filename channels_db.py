import sqlite3

class ChannelDB:
    def __init__(self,db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(f"{self.db_name}.db")
        self.cursor = self.conn.cursor()
    def create_db(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS channels
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, channel_id STRING)''')
        self.conn.commit()
    
    def add(self,channel_id):
        print(channel_id)
        self.cursor.execute("INSERT INTO channels (channel_id) VALUES (?)", (channel_id,))

        self.conn.commit()
        return True
    def delete(self,channel_id):
        try:
            cursorr.execute("DELETE FROM channels WHERE channel_id=?",(channel_id,))
            return True
        except:
            return False
    
    def get_list(self):
        self.cursor.execute("SELECT channel_id FROM channels")
        result = self.cursor.fetchall()
        return  [row[0] for row in result]

channel_db = ChannelDB("channels")
channel_db.create_db()