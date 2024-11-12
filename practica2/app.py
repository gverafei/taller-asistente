# msg = "Hola mundo!"
# print(msg)


import os
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Cargar llaves del archivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file = open("audio.mp3", "rb")
transcribed = openai.audio.transcriptions.create(model="whisper-1", file=audio_file)
print("Resultado:", transcribed.text)