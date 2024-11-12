let blobs = [];
let stream;
let rec;
let recordUrl;
let audioResponseHandler;
let timeoutID;
const btnRecord = document.getElementById("record");
const btnStop = document.getElementById("stop");

// Se establece el 'handler' o 'callback' a llamar cuando termine la grabacion
function recorder(url, handler) {
    recordUrl = url;
    if (typeof handler !== "undefined") {
        audioResponseHandler = handler;
    }
}

// Esta es la que realiza la grabación
async function record() {
    try {
        document.getElementById("text").innerHTML = "<i>Grabando...</i>";
        btnRecord.style.display = "none";
        btnStop.style.display = "";
        document.getElementById("record-stop-label").style.display = "block"
        document.getElementById("record-stop-loading").style.display = "none"
        btnStop.disabled = false

        blobs = [];

        // Grabar audio usando el API que provee el navegador
        stream = await navigator.mediaDevices.getUserMedia({ audio: true, video: false })
        rec = new MediaRecorder(stream);
        rec.ondataavailable = e => {
            if (e.data) {
                blobs.push(e.data);
            }
        }

        // Al dejar de grabar, se manda el audio al servidor Flask
        rec.onstop = doPreview;

        // Se inicia la grabación
        rec.start();
        // se detiene automaticamente después de 10 segundos
        timeoutID = setTimeout(() => { stop(); }, 10000);
    } catch (e) {
        alert("No fue posible iniciar el grabador de audio! Favor de verificar que se tenga el permiso adecuado.");
    }
}

// Esta función toma el audio grabado y lo envía al servidor Flask
function doPreview() {
    if (!blobs.length) {
        console.log("No se pudo obtener el archivo de audio!");
    } else {
        console.log("Se pudo obtener el archivo de audio!");
        const blob = new Blob(blobs);

        // Usar fetch para enviar el audio grabado a Flask
        var fd = new FormData();
        fd.append("audio", blob, "audio");

        // Se envía el audio a Flask
        fetch(recordUrl, {
            method: "POST",
            body: fd,
        })
            .then((response) => response.json())
            .then(audioResponseHandler)
            .catch(err => {
                // No se pudo enviar el audio
                console.log("Oops: Ocurrió un error", err);
            });
    }
}

function stop() {
    clearTimeout(timeoutID);
    document.getElementById("text").innerHTML = "<i>Procesando...</i>";
    document.getElementById("record-stop-label").style.display = "none";
    document.getElementById("record-stop-loading").style.display = "block";
    btnStop.disabled = true;

    rec.stop();
}

// Llamar al handler al terminar la grabación
function handleAudioResponse(response) {
    if (!response || response == null) {
        //TODO subscribe you thief
        console.log("No response");
        return;
    }

    btnRecord.style.display = "";
    btnStop.style.display = "none";

    if (audioResponseHandler != null) {
        audioResponseHandler(response);
    }
}

// Se establecen los botones de grabar y stop
btnRecord.addEventListener("click", record);
btnStop.addEventListener("click", stop);

// Aqui inicia la aplicación
document.addEventListener('DOMContentLoaded', (event) => {
    // Se inicializa el ambiente para grabar y se define la
    // función que se ejecutará al recibir el texto generado
    recorder("/audio", response => {
        btnRecord.style.display = "";
        btnStop.style.display = "none";
        if (!response || response == null) {
            // No responde el API. Revisa los errores
            console.log("No response");
            return;
        }
        console.log("El texto fue: " + response.text)
        document.getElementById("text").innerHTML = response.text.replace(/\n/g, "<br />");
    });
});