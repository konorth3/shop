
from os import environ
from Shop import app

if __name__ == "__main__":
    HOST = environ.get('SERVER_HOST', 'localhost')
    PORT = int(environ.get('SERVER_PORT', '8000'))

app.run(HOST, PORT)

