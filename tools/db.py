import os
from tinydb import TinyDB, Query

db_path=os.path.abspath(os.path.join(os.path.dirname(__file__),"../db"))
db_file=os.path.join(db_path, 'db.json')

db = TinyDB(db_file)
query= Query()

def DB(dictname, key, value, flag):
	dict= {dictname: {key: value, 'flag': flag}}

	return dict


flag = 'True'




