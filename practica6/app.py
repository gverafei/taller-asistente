import os
import openai
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request
from gtts import gTTS

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
            {
                "role": "system",
                "content": "Eres una asistente sarcástica, malhumurada y grosera.",
            },
            {"role": "user", "content": transcribed.text},
        ],
    )

    result = ""
    for choice in response.choices:
        result += choice.message.content

    # Voz natural
    elevenlabs_key = os.getenv("ELEVENLABS_API_KEY")
    CHUNK_SIZE = 1024
    # Utiliza la voz llamada Bella
    url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"
    # Utiliza la voz llamada Glinda
    # url = "https://api.elevenlabs.io/v1/text-to-speech/z9fAnlkpzviPz146aGWa"
    # Utiliza la voz llamada Jessica
    # url = "https://api.elevenlabs.io/v1/text-to-speech/cgSgspJ2msm6clMCkdW9"
    # Utiliza la voz llamada Charlotte
    # url = "https://api.elevenlabs.io/v1/text-to-speech/XB0fDUnXU5powFXDhCwa"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": elevenlabs_key,
    }

    data = {
        "text": result,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.55, "similarity_boost": 0.75},
    }

    # Se guarda en static/response.mp3
    file_name = "response.mp3"
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        with open("static/" + file_name, "wb") as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
    else:
        # Voz sencilla
        tts = gTTS(result, lang="es", tld="com.mx")
        tts.save("static/response.mp3")

    return {"result": "ok", "text": result, "file": "response.mp3"}
