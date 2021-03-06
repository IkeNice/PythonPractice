import os
import sqlite3
import json
import pprint

filename = 'mydb.db'
create = not os.path.exists(filename)
db = sqlite3.connect(filename)
cursor = db.cursor()
if create:
    cursor = db.cursor()
    cursor.execute("CREATE TABLE crews("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,"
                   "crew_name TEXT UNIQUE NOT NULL)")
    cursor.execute("CREATE TABLE styles("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,"
                   "style_name TEXT UNIQUE NOT NULL)")
    cursor.execute("CREATE TABLE dancers("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,"
                   "crew_id INTEGER NOT NULL,"
                   "style_id INTEGER NOT NULL,"
                   "dancer_name TEXT UNIQUE NOT NULL,"
                   "FOREIGN KEY(crew_id) REFERENCES crews(id),"
                   "FOREIGN KEY(style_id) REFERENCES styles(id))")

    cursor.execute("CREATE TABLE dancers_info"
                   "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,"
                   "crew_name TEXT NOT NULL"
                   "style_name TEXT NOT NULL"
                   "dancer_name TEXT NOT NULL")
    db.commit()

# cursor = db.cursor()
# cursor.execute("INSERT INTO crews(crew_name) VALUES ('No Team')")
# cursor.execute("INSERT INTO crews(crew_name) VALUES ('Jabbawockeez')")
# cursor.execute("INSERT INTO crews(crew_name) VALUES ('Kinjaz')")

# cursor.execute("INSERT INTO styles(style_name) VALUES('Hip-Hop')")
# cursor.execute("INSERT INTO styles(style_name) VALUES('Popping')")
# cursor.execute("INSERT INTO styles(style_name) VALUES('Breaking')")

# cursor.execute("INSERT INTO dancers(crew_id, style_id, dancer_name) VALUES(2, 3, 'Steven Lor')")
# cursor.execute("INSERT INTO dancers(crew_id, style_id, dancer_name) VALUES(1, 2, 'Dytto')")
# cursor.execute("INSERT INTO dancers(crew_id, style_id, dancer_name) VALUES(1, 1, 'Taylor Hatala')")
# cursor.execute("INSERT INTO dancers(crew_id, style_id, dancer_name) VALUES(2, 3, 'Ben Chung')")
# cursor.execute("INSERT INTO dancers(crew_id, style_id, dancer_name) VALUES(2, 1, 'Phil Tayag')")
# cursor.execute("INSERT INTO dancers(crew_id, style_id, dancer_name) VALUES(3, 1, 'Anthony Lee')")
# cursor.execute("INSERT INTO dancers_info(crew_name, style_name, dancer_name) VALUES('test', 'test', 'test')")
# db.commit()

cursor2 = db.cursor()
cursor2.execute("SELECT d.id, c.crew_name, s.style_name, d.dancer_name FROM dancers d "
                "INNER JOIN crews c ON d.crew_id = c.id "
                "INNER JOIN styles s ON d.style_id = s.id")
# cursor2.execute("select * from dancers ORDER BY id")

# records = cursor2.fetchall()
# # pprint.pprint(records)
# res = {}
# resList = []
# for i, record in enumerate(records):
#     res["id"] = records[i][0]
#     res["crew_name"] = records[i][1]
#     res["style_name"] = records[i][2]
#     res["dancer_name"] = records[i][3]
#     resList.append(res.copy())
#
# with open("data_file.json", "w") as write_file:
#     json.dump(resList, write_file, indent=4)


with open("data_file.json", "r") as read_file:
    dancersList = json.load(read_file)
# pprint.pprint(dancersList)
pprint.pprint(dancersList[len(dancersList)-1])
print("\r\n")

cursor = db.cursor()
cursor.execute("SELECT * FROM dancers_info")
records = cursor.fetchall()
pprint.pprint(records)
print("\r\n")

# gen = [(dancersList[len(dancersList)-1]['crew_name'],
#        dancersList[len(dancersList)-1]['style_name'],
#        dancersList[len(dancersList)-1]['dancer_name'])]
# cursor.executemany("INSERT INTO dancers_info(crew_name, style_name, dancer_name) VALUES (?,?,?)", gen)
cursor.execute("INSERT INTO dancers_info(crew_name, style_name, dancer_name) "
               "VALUES('{0}', '{1}', '{2}')".format(dancersList[len(dancersList)-1]['crew_name'],
                                                    dancersList[len(dancersList)-1]['style_name'],
                                                    dancersList[len(dancersList)-1]['dancer_name']))
db.commit()

cursor.execute("SELECT * FROM dancers_info")
records = cursor.fetchall()
pprint.pprint(records)
