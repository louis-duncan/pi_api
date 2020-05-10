from flask import Flask, request, abort
import _functions
import json

app = Flask(__name__,)


@app.route('/')
def hello_world():
    print("Hello")
    return 'Hello World!'


@app.route('/mc_server', methods=["GET", "POST"])
def mc_server():
    if request.method == "POST":
        data = request.form
        if "command" in list(data.keys()):
            resp = _functions.submit_mc_command(data["command"])
            return resp
        else:
            abort(400, "No command supplied.")
    elif request.method == "GET":
        return '''<form method="POST">
                  Enter Command: <input type="text" name="command"><br>
              </form>'''


@app.route('/temp')
def resp_temp():
    return json.dumps(_functions.get_temp())


if __name__ == '__main__':
    app.run()
