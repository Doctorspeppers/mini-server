from .packages.flask import Flask
from .packages.flask import request
app = Flask(__name__)

@app.route("/<env>")
def hello_world(env):
    with open("./envs/"+env,"r") as fp:

        return str(fp.contents)