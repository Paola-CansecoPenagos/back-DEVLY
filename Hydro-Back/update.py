from pymongo import MongoClient

# Conexión al servidor MongoDB (asegúrate de reemplazar los valores correspondientes)
client = MongoClient('mongodb+srv://sensorsDevly:devly1@sensorsdevly.wnv4cc4.mongodb.net')
db = client.Sensors

# Actualización de los documentos con el campo "temperature"
collection = db.datos

# Filtro para seleccionar los documentos que contienen el campo "temperature"
filter = {"humedity": {"$exists": True}}

# Actualización: establecer el nuevo valor para el campo "temperature"
new_temperature_value = 70  # Reemplaza con el nuevo valor que deseas establecer
update = {"$set": {"humedity": new_temperature_value}}

# Uso del método update_many() para realizar la actualización masiva
result = collection.update_many(filter, update)

print(f"Documentos actualizados: {result.modified_count}")