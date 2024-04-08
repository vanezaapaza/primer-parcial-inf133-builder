# Primer Parcial
## Programación Web III - RESTful Builder

### Antes de Empezar:

1. Realiza un **Fork** de este repositorio:
![Repositorio del Primer Parcial](https://live.staticflickr.com/65535/53638747703_0dc1434506_z.jpg)

2. Si vas a trabajar en tu equipo local clona el nuevo repositorio resultado del **Fork** y abrelo con **VSCode** o el editor de tu preferencia para trabajar tu solución. También puedes trabajar tu solución en **GitHub Codespaces**.

3. Completa tus datos personales en la siguiente tabla:
    | Nombre   | Apellido   | CI   |
    | -------- | ---------- | ---- |
    | `nombre` | `apellido` | `ci` |

4. Realiza un commit de esta modificación y sube los cambios a tu repositorio remoto ejecutando los siguientes comandos desde la terminal de tu equipo local o desde **GitHub Codespaces**:
    ```bash
    git add .
    git commit -m "datos actualizados"
    git push origin main
    ```
5. En la terminal ejecuta el siguiente comando para instalar las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

### Contexto:

Te han contratado como **Junior Back-End Developer** en una empresa de desarrollo de videojuegos. Tu primer tarea es desarrollar un **API RESTful** para administrar las información de los personajes de un nuevo videojuego RPG que se encuentra en desarrollo. Cada personaje del videojuego RPG tiene las siguientes características:

- id: Identificador único del personaje.
- name: Nombre del personaje.
- level: Nivel del personaje.
- role: Rol del personaje en el juego (Wizard, Warrior, Archer)
- health: Puntos de vida del personaje.
- intelligence: Puntos de inteligencia del personaje.
- charisma: Puntos de carisma del personaje.
- strength: Puntos de fuerza del personaje.
- dexterity: Puntos de destreza del personaje. 


### Tareas:
Construye una **API RESTful** que permita realizar las operaciones **CRUD** sobre los personajes del videojuego RPG. La API debe permitir realizar las siguientes operaciones:

1. Crear un nuevo personaje.
2. Listar todos los personajes
3. Buscar un personaje por su id.
4. Listar a todos los personajes del rol `Wizard`.
5. Listar a todos los personajes del rol `Warrior` con nivel mayor a 10.
6. Listar a todos los personajes del rol `Archer` con nivel mayor a 5 y carisma mayor a 10.
7. Actualizar el nivel de un personaje.
8. Actualizar inteligencia, carisma, fuerza y destreza de un personaje.
9. Eliminar al personaje con id 1.
10. Crear un nuevo personaje y procurar que el id sea único.

La **API RESTful** debe estar construida con el patron de diseño BUILDER y debe cumplir con los principios de desarrollo de Software DRY, KISS, YAGNI y la S de SOLID.

### Rutas y resultados esperados:

1. POST /characters
    - Datos a Enviar:
    ```json
    {
        "name": "Gandalf",
        "level": 10,
        "role": "Wizard",
        "health": 100,
        "intelligence": 20,
        "charisma": 15,
        "strength": 10,
        "dexterity": 10
    }
    ```
    - Respuesta Esperada:
    ```json
    {
        "name": "Gandalf",
        "level": 10,
        "role": "Wizard",
        "health": 100,
        "intelligence": 20,
        "charisma": 15,
        "strength": 10,
        "dexterity": 10
    }
    ```
2. GET /characters
    - Respuesta Esperada:
    ```json    
    {"1":{
            "name": "Gandalf",
            "level": 10,
            "role": "Wizard",
            "health": 100,
            "intelligence": 20,
            "charisma": 15,
            "strength": 10,
            "dexterity": 10
    }}
    ```
3. GET /characters/1
    - Respuesta Esperada:
    ```json
    {"1":{
            "name": "Gandalf",
            "level": 10,
            "role": "Wizard",
            "health": 100,
            "intelligence": 20,
            "charisma": 15,
            "strength": 10,
            "dexterity": 10
    }}
    ```
4. GET /characters/?role=Wizard
   - Respuesta Esperada:
    ```json
    {"1":{
        "name": "Gandalf",
        "level": 10,
        "role": "Wizard",
        "health": 100,
        "intelligence": 20,
        "charisma": 15,
        "strength": 10,
        "dexterity": 10
    }}
    ```
5. GET /characters/?role=Warrior&level=10
   - Respuesta Esperada:
    ```json
    {"2":{
        "name": "Aragorn",
        "level": 10,
        "role": "Warrior",
        "health": 100,
        "intelligence": 20,
        "charisma": 15,
        "strength": 10,
        "dexterity": 10
    }}
    ```
6. GET /characters/?role=Archer&level=5&charisma=10
   - Respuesta Esperada:
    ```json
    {"2":{
        "name": "Robin",
        "level": 5,
        "role": "Archer",
        "health": 100,
        "intelligence": 20,
        "charisma": 10,
        "strength": 10,
        "dexterity": 10
    }}
    ```
7. PUT /characters/1
   - Datos a Enviar:
    ```json
    {
        "level": 1
    }
    ```
    - Respuesta Esperada:
    ```json
    {
        "name": "Gandalf",
        "level": 1,
        "role": "Wizard",
        "health": 100,
        "intelligence": 20,
        "charisma": 15,
        "strength": 10,
        "dexterity": 10
    }
    ```
8. PUT /characters/2
   - Datos a Enviar:
    ```json
    {
        "intelligence": 30,
        "charisma": 20,
        "strength": 15,
        "dexterity": 15
    }
    ```
    - Respuesta Esperada:
    ```json
    {
        "name": "Aragorn",
        "level": 10,
        "role": "Warrior",
        "health": 100,
        "intelligence": 30,
        "charisma": 20,
        "strength": 15,
        "dexterity": 15
    }
    ```
9.  DELETE /characters/3
    - Respuesta Esperada:
    ```json
    {"message": "Character with id 3 has been deleted successfully"}
    ```
10. POST /characters
    - Datos a Enviar:
    ```json
    {
        "name": "Legolas",
        "level": 5,
        "role": "Archer",
        "health": 100,
        "intelligence": 20,
        "charisma": 15,
        "strength": 10,
        "dexterity": 10
    }
    ```
    - Respuesta Esperada:
    ```json
    {
        "name": "Legolas",
        "level": 5,
        "role": "Archer",
        "health": 100,
        "intelligence": 20,
        "charisma": 15,
        "strength": 10,
        "dexterity": 10
    }
    ```
11. GET /characters
    - Respuesta Esperada:
    ```json    
    {"1":{
            "name": "Gandalf",
            "level": 10,
            "role": "Wizard",
            "health": 100,
            "intelligence": 20,
            "charisma": 15,
            "strength": 10,
            "dexterity": 10
    },
    "2":{
            "name": "Aragorn",
            "level": 10,
            "role": "Warrior",
            "health": 100,
            "intelligence": 30,
            "charisma": 20,
            "strength": 15,
            "dexterity": 15
    },
    "4":{
            "name": "Legolas",
            "level": 5,
            "role": "Archer",
            "health": 100,
            "intelligence": 20,
            "charisma": 15,
            "strength": 10,
            "dexterity": 10
    }}
    ```

### Entrega:
1. La lógica de la API debe estar en el archivo `server.py`.
2. La lógica del cliente debe estar en el archivo `client.py`.
3. Una vez tengas los puntos 1 y 2 completados, realiza un commit con el mensaje "Entrega Final" y sube los cambios a tu repositorio remoto ejecutando los siguientes comandos desde la terminal de tu equipo local o desde **GitHub Codespaces**:
    ```bash
    git add .
    git commit -m "Entrega Final"
    git push origin main
    ```
4. Una vez completado el paso anterior adjunta la **URL** de tu repositorio de **GitHub** en la tarea asignada en **Google Classroom**. 

### Restricciones:

Durante el examen solo puede consultar los siguientes recursos:
- [Patrón de Diseño Builder](https://refactoring.guru/es/design-patterns/builder)
- [Documentación Oficial de Python](https://docs.python.org/3/)
- [Documentación de HTTP Server](https://docs.python.org/3/library/http.server.html)

### IMPORTANTE: 
- **No** se permite el uso de frameworks como Flask, Django, FastAPI, etc.
- **No** se permite el uso de librerías externas que no estén dentro del archivo `requirements.txt`.
- **No** se permite el uso de bases de datos.
- **No** se permite el uso de archivos para almacenar la información.
- La **API** debe ser **RESTful**.
- La API debe cumplir con las operaciones **CRUD**.
- La **API** debe cumplir con las rutas y resultados esperados.
- La estructura de la **API** debe estar construida con el patrón de diseño **BUILDER**.
- La **API** debe cumplir con los principios de desarrollo de Software **DRY, KISS, YAGNI y la S de SOLID**.
- Los ids de los personajes deben ser únicos y manejados de forma incremental correlativa.
