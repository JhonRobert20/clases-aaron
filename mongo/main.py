from pymongo import MongoClient, errors
from bson.objectid import ObjectId

# Conexión a MongoDB
username = "rootuser"
password = "rootpassword"
database_name = "aaron"
collection_name = "peliculas"

# Cadena de conexión con autenticación
connection_string = f"mongodb://{username}:{password}@localhost:27018/?authMechanism=DEFAULT"

# Conexión a MongoDB usando la cadena de conexión
client = MongoClient(connection_string)
db = client[database_name]
collection = db[collection_name]

# eliminar una base de datos completa con todas sus colecciones
# db.command("dropDatabase")

# a =  hola, dime
# a_splited = a.split(",") # => [hola, dime]

# a_replaced = a.replace(",", "_") # => hola_ dime

# Para borrar una db no tiene que tener collections dentro
# db_to_delete = client["peliculas"].drop_collection("aaron")

database_to_delete = client["sadasd"]
collections_to_delete = database_to_delete.list_collection_names()

for collection in collections_to_delete:
    database_to_delete.drop_collection(collection)


def create_document(document):
    try:
        collection.insert_one(document)
        print("Documento insertado con éxito.")
    except errors.DuplicateKeyError:
        print("Error: el documento ya existe en la base de datos.")
    except Exception as e:
        print(f"Error al insertar: {e}")

def read_document(query={}):
    try:
        documents = collection.find(query)
        for doc in documents:
            print(doc)
    except Exception as e:
        print(f"Error al leer: {e}")

def update_document(query, new_values):
    try:
        collection.update_one(query, {"$set": new_values})
        print("Documento actualizado con éxito.")
    except Exception as e:
        print(f"Error al actualizar: {e}")

def delete_document(query):
    try:
        collection.delete_one(query)
        print("Documento eliminado con éxito.")
    except Exception as e:
        print(f"Error al eliminar: {e}")


if __name__ == "__main__":
    # Insertar documento de ejemplo
    doc_example = {"nombre": "Juan", "edad": 30}
    doc_pelis = {"Terror": "Viernes 13", "duracion": 120}
    doc_test = {"name": __name__}
    doc_aaron = __name__
    create_document(doc_test)
    create_document(doc_example)

    create_document(doc_pelis)

    # # Leer documentos
    # print("\nDocumentos con el nombre Juan:")
    # read_document({"nombre": "Juan"})
    #
    # Actualizar documento
    update_document({"_id": ObjectId("65416a75a3de7f4cdc255ae0")}, {"titulo": "Pulpo Fiction"})

    #
    # # Confirmar la actualización
    print("\nDocumentos actualizados con el titulo : Pulpo Fiction")
    read_document({"titulo": "Pulpo Fiction"})
    #
    # # Eliminar documento
    delete_document({"titulo": "Pulpo Fiction"})
    #
    # # Confirmar la eliminación
    print("\nDocumentos después de la eliminación:")
    read_document({"titulo": "Pulpo Fiction"})
