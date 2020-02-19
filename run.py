
from os import environ, sys
from Shop import app

if __name__ == "__main__":
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    PORT = int(environ.get('SERVER_PORT', sys.argv[1]))

app.run(HOST, PORT)

