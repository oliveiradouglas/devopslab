from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Douglas Oliveira - Laboratório Pipeline DevOps - 11/08/2022"

if __name__ == '__main__':
    app.run()