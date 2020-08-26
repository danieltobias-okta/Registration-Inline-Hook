from flask import Flask, request, jsonify, redirect
import json

app = Flask(__name__)

url = "https://tobias.okta.com"


@app.route("/register", methods = ['GET', 'POST'])
def register():
    return jsonify(commands = [ { "type" : "com.okta.action.update", "value": { "registration":"ALLOW"}}, {"type":"com.okta.user.profile.update", "value":{"registrationNumber":12345}}])

@app.route("/", methods = ['GET'])
def index():
    return redirect(url + "/signin/register")

if __name__ == "__main__":
    app.run(debug=True, port=80)