from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

personajes = [
    {
        "id": 94725,
        "name": "Gandalf",
        "level": 10,
        "role": "Wizard",
        "charisma": 15,
        "strength": 10,
        "dexterity": 10,
    },
    {
        "id": 1,
        "name": "Robin",
        "level": 5,
        "role": "Archer",
        "charisma": 10,
        "strength": 10,
        "dexterity": 10,
    },
]

class PersonajesService:  
    
    @staticmethod
    def filter_personaje_by_role(role):
        return [personaje for personaje in personajes if personaje["role"] == role]

    @staticmethod
    def add_personaje(data):
        data["id"] = len(personajes) + 1
        personajes.append(data)
        return personajes


    @staticmethod
    def delete_personaje(data):
        data["id"] = len(personajes) + 1
        personajes.clear(data)
        return personajes

class HTTPResponseHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))


class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if parsed_path.path == "/personajes":
            if "role" in query_params:
                role = query_params["role"][0]
                personajes_filtrados = PersonajesService.filter_personaje_by_role(role)
                if personajes_filtrados != []:
                    HTTPResponseHandler.handle_response(self, 200, personajes_filtrados)
                else:
                    HTTPResponseHandler.handle_response(self, 204, [])
            else:
                HTTPResponseHandler.handle_response(self, 200, personajes)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_POST(self):
        if self.path == "/personajes":
            data = self.read_data()
            personajes = PersonajesService.add_personaje(data)
            HTTPResponseHandler.handle_response(self, 201, personajes)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )



    def do_DELETE(self):
        if self.path == "/personajes":
            data = self.read_data("id")
            personajes = PersonajesService.delete_personaje(data)
            HTTPResponseHandler.handle_response(self, 200, personajes)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()
