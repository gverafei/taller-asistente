from os import getenv
from phue import Bridge


def lights_on():
    # Obtiene la dirección del bridge
    bridge_ip_address = getenv("bridge_ip_address")
    b = Bridge(bridge_ip_address)
    b.connect()

    # Se obtienen todas las luces disponibles
    lights = b.get_light_objects("name")

    # Se encienden
    for light in lights:
        lights[light].on = True

    return "Se ha realizo la encendida de las luces"


def lights_off():
    # Obtiene la dirección del bridge
    bridge_ip_address = getenv("bridge_ip_address")
    b = Bridge(bridge_ip_address)
    b.connect()

    # Se obtienen todas las luces disponibles
    lights = b.get_light_objects("name")

    # Se encienden
    for light in lights:
        lights[light].on = False

    return "Se ha realizo el apagado de las luces"
