from subprocess import call


def open_chrome(website):
    website = "" if website is None else website
    # Funciona para windows, si tienes otro SO o navegador, busca el ejecutable
    call("C:/Program Files/Google/Chrome/Application/chrome.exe " + website)
    # Quizas funcione este para linux
    #call("google-chrome" + website)
    return "Listo, ya abrí el sitio web solicitado."
