import sqlite3
database = 'miptnews.db'
db = sqlite3.connect(database)
c = db.cursor()
c.execute('CREATE TABLE miptnews (id INTEGER PRIMARY KEY, text VARCHAR(200), link VARCHAR(100), date UNIX_TIME, publish UNIX_TIME, chat_id INTEGER, message_id INTEGER)')
