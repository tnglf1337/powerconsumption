def kwh(stunde, watt=225):
    """
        watt=150 im durchschnitt bei officenutzung
        watt=300 im durchschnitt bei gaming
        watt=225 ist einfach mittelwert
    """

    return watt * stunde / 1000
