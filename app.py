import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>OscarProj</h1><p>This was created with an empty flask skeleton.</p>"


if __name__ == '__main__':
    app.run()