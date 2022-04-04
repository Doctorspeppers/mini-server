from .packages.flask import Flask
from .packages.flask import request
app = Flask(__name__)

@app.route("/latest/meta-data/tags/instance/<var>")
def hello_world(var):
    env_vars = []
    with open("./.env","r") as fp:
        lines = fp.readlines()
        for line in lines:
            env_vars[line.split("=")[0]] = line.split("=")[1]
        return env_vars[var]
