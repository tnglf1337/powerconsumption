class TarifReader:
    def __init__(self, file):
        self.file = file  # Speichert den Dateinamen

    def public_readtarif(self):
        tarif = 0.0  # Standardwert
        try:
            with open(self.file, "r") as file:  # Öffne die Datei
                for row in file:
                    # Überspringe Zeilen, die mit "#" beginnen
                    if not row.strip().startswith("#"):
                        content = row.strip()
                        try:
                            tarif = float(content.replace(",", "."))
                            return tarif  # Ersten gültigen Tarif zurückgeben
                        except ValueError:
                            print(f"Fehlerhafte Zeile: '{content}'")
            # Falls keine gültige Zeile gefunden wird
            print(f"Kein gültiger Tarif gefunden. Standardwert: {tarif}")
            return tarif
        except FileNotFoundError:
            print(f"Datei '{self.file}' nicht gefunden.")
            return tarif
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            return tarif