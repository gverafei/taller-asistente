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
    return render_template("index.html")


@app.route("/audio", methods=["POST"])
def audio():
    # Obtener audio grabado y transcribirlo
    audio = request.files.get("audio")
    audio.save("audio.mp3")
    audio_file = open("audio.mp3", "rb")
    transcribed = openai.audio.transcriptions.create(model="whisper-1", file=audio_file)

    # Enviamos el texto a OpenAI
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            # Aqui cambia su tono, como quieres que te hable
            {"role": "system", "content": "Eres un asistente como Alexa que responde con alguna broma junto con la respuesta."},
            {"role": "user", "content": transcribed.text},
        ],
    )

    result = ""
    for choice in response.choices:
        result += choice.message.content

    return {"result": "ok", "text": result}
