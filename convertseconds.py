def secondsToHours(seconds):
    return int(seconds) / 3600

def saveUptime(seconds, file):
    with open(file, "w")as file:
        file.write(str(seconds))

def getUptime(file):
    with open(file, "r") as file:
        return int(file.read())

def seconds_to_hms(seconds):
    hours = seconds // 3600  # Stunden berechnen
    seconds %= 3600  # Restliche Sekunden nach Stunden berechnen
    minutes = seconds // 60  # Minuten berechnen
    seconds %= 60  # Restliche Sekunden berechnen

    # Das Format in hh:mm:ss umwandeln
    return f"{hours:02}:{minutes:02}:{seconds:02}"