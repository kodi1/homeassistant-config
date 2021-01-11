#!/usr/bin/python

import sqlite3 as lite
import os
import sys

db_path = '/storage/.kodi/userdata/Database'
#db_path = ''
db = os.path.join(db_path, 'TV40.db')

if __name__=="__main__":
  try:
    con = lite.connect(db)
    cur = con.cursor()
  except lite.Error as e:
      sys.exit("Could not open database %s: %s" % (db,e))

  cur.execute('''UPDATE channels
                SET iLastWatched = 0''')

  #for row in cur.execute('SELECT * FROM channels;'):
    #print row

  con.commit()
  con.close()
