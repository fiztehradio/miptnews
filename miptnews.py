#!/usr/bin/env python3
#-*- coding: UTF 8 -*-

import os
import sqlite3
from objs.bot import ExportBot

database = 'miptnews.db'

if not os.path.isfile(database):
    db = sqlite3.connect(database)
    c = db.cursor()
    c.execute('CREATE TABLE miptnews (id INTEGER PRIMARY KEY, text VARCHAR(200), link VARCHAR(100), date UNIX_TIME, publish UNIX_TIME, chat_id INTEGER, message_id INTEGER)')

bot = ExportBot()
bot.detect()
bot.public_posts()
