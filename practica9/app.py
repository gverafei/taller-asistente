import os
import openai
import requests
import json  # Para trabajar con json
from dotenv import load_dotenv
from flask import Flask, render_template, request
from gtts import gTTS
from hora import get_time  # Función que da la hora
from clima import get_weather  # Función que da el clima
from website import open_chrome  # Función que abre un sitio web
from lights import lights_on, lights_off  # Función que prende o apaga las luces

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

    # Aqui empieza la llamada al modelo de lenguaje
    # Sección de message
    messages = []
    # Aqui cambia su tono, como quieres que te hable
    messages.append(
        {
            "role": "system",
            "content": "Eres una asistente sarcástica, malhumurada y grosera. Utiliza las herramientas proporcionadas para asistir al usuario.",
        }
    )
    messages.append({"role": "user", "content": transcribed.text})

    # Sección de tools
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_time",
                "description": "Obtener la hora actual. Llama a esta función cada vez que necesites saber la hora, por ejemplo, cuando un cliente pregunte '¿Cuál es la hora actual?'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ubicacion": {
                            "type": "string",
                            "description": "La ubicación, debe ser una ciudad.",
                        }
                    },
                    "required": ["ubicacion"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Obtener el clima o temperatura actual. Llama a esta función cada vez que necesites saber el clima o temperatura, por ejemplo, cuando un cliente pregunte '¿Cuál es el clima actual?'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ubicacion": {
                            "type": "string",
                            "description": "La ubicación, debe ser una ciudad.",
                        }
                    },
                    "required": ["ubicacion"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "open_chrome",
                "description": "Abrir una página web o sitio web especifico. Llama a esta función cada vez que necesites abrir una página web, por ejemplo, cuando un cliente pregunte '¿Abre la página de facebook?'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "website": {
                            "type": "string",
                            "description": "El sitio al cual se desea ir.",
                        }
                    },
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "lights_on",
                "description": "Encender las luces. Llama a esta función cada vez que necesites encender las luces, por ejemplo, cuando un cliente pregunte 'Enciende las luces'.",
            },
        },
        {
            "type": "function",
            "function": {
                "name": "lights_off",
                "description": "Apagar las luces. Llama a esta función cada vez que necesites apagar las luces, por ejemplo, cuando un cliente pregunte 'Apaga las luces'.",
            },
        },
    ]

    # Enviamos el texto a OpenAI
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
    )

    # El modelo desea llamar alguna función?
    function_name = ""
    if response.choices[0].message.tool_calls:
        tool_call = response.choices[0].message.tool_calls[0]
        function_name = tool_call.function.name  # Que funcion?
        arguments = json.loads(tool_call.function.arguments)  # Con que datos?
        tool_id = tool_call.id  # Que id?

        # Se revisa que función se debe llamar
        if function_name == "get_time":
            # Agregamos la respuesta anterior
            messages.append(response.choices[0].message)
            # Agregamos el dato de la función local
            messages.append(
                {
                    "role": "tool",
                    "content": json.dumps(
                        {
                            "ubicacion": arguments["ubicacion"],
                            "hora": get_time(),
                        }
                    ),
                    "tool_call_id": tool_id,
                }
            )
            # Enviamos el texto a OpenAI
            response = openai.chat.completions.create(model="gpt-4o", messages=messages)
        elif function_name == "get_weather":
            # Agregamos la respuesta anterior
            messages.append(response.choices[0].message)
            # Agregamos el dato de la función local
            messages.append(
                {
                    "role": "tool",
                    "content": json.dumps(
                        {
                            "ubicacion": arguments["ubicacion"],
                            "clima": get_weather(arguments["ubicacion"]),
                        }
                    ),
                    "tool_call_id": tool_id,
                }
            )
            # Enviamos el texto a OpenAI
            response = openai.chat.completions.create(model="gpt-4o", messages=messages)
        elif function_name == "open_chrome":
            # Agregamos la respuesta anterior
            messages.append(response.choices[0].message)
            # Agregamos el dato de la función local
            messages.append(
                {
                    "role": "tool",
                    "content": json.dumps(
                        {
                            "website": arguments["website"],
                            "response": open_chrome(arguments["website"]),
                        }
                    ),
                    "tool_call_id": tool_id,
                }
            )
            # Enviamos el texto a OpenAI
            response = openai.chat.completions.create(model="gpt-4o", messages=messages)
        elif function_name == "lights_on":
            # Agregamos la respuesta anterior
            messages.append(response.choices[0].message)
            # Agregamos el dato de la función local
            messages.append(
                {
                    "role": "tool",
                    "content": json.dumps(
                        {
                            "response": lights_on(),
                        }
                    ),
                    "tool_call_id": tool_id,
                }
            )
            # Enviamos el texto a OpenAI
            response = openai.chat.completions.create(model="gpt-4o", messages=messages)
        elif function_name == "lights_off":
            # Agregamos la respuesta anterior
            messages.append(response.choices[0].message)
            # Agregamos el dato de la función local
            messages.append(
                {
                    "role": "tool",
                    "content": json.dumps(
                        {
                            "response": lights_off(),
                        }
                    ),
                    "tool_call_id": tool_id,
                }
            )
            # Enviamos el texto a OpenAI
            response = openai.chat.completions.create(model="gpt-4o", messages=messages)

    # Obtenemos el resultado
    result = ""
    for choice in response.choices:
        result += choice.message.content    

    # Voz natural
    elevenlabs_key = os.getenv("ELEVENLABS_API_KEY")
    print(elevenlabs_key)
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
    # print(response.status_code)
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
