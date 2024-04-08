import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# GET obtener a todos los personajes 
print("lista de los personajes creados")
ruta_get = url + "personajes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# GET listado
print("listar a los personajes por role: archer")
ruta_get = url + "personajes?role=Archer"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# DELETE eliminar el personaje con id
print("eliminar al personaje con id : 1")
ruta_delete = url + "personajes?id=1"
delete_response = requests.request(method="DELETE", url=ruta_delete)
print(delete_response.text)

# POST agrega un nuevo personaje 
print("lista con el nuevo personaje")
ruta_post = url + "personajes"
nuevo_personaje = {
    "id": 24345,
    "name": "Aragorn",
    "level": 10,
    "role": "Warrior",
    "charisma": 20,
    "strength": 15,
    "dexterity": 15,
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_personaje)
print(post_response.text)
