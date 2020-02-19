from flask import Flask

app = Flask(__name__)

print("intit.py", __name__)

import Shop.views