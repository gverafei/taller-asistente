import os
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Cargar llaves del archivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Inicia Flask app
app = Flask(__name__)


# Para la petición raíz definimos la función index que regresa
# el archivo de template index.html
@app.route("/")
def index():
    return render_template("index1.html")