import pymongo # meng-import library pymongo yang sudah kita install
from datetime import datetime
client = pymongo.MongoClient("mongodb+srv://Rosita28:Rosita28@cluster0.e3zc6ay.mongodb.net/?retryWrites=true&w=majority")
db = client['Rositaa'] # ganti sesuai dengan nama database kalian
my_collections = db['Rositaa2']


data = {"kecepatan": 90,
    "latitude": 6.2088,
    "longitude": 106.8456,
    "Timestamp": datetime.now()}


results = my_collections.insert_many([data])
print(results.inserted_ids) # akan menghasilkan ID dari data yang kita masukkan