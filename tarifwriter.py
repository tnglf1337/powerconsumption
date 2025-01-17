from datetime import datetime

class TarifWriter:
    def __init__(self, file, tarif):
        self.file = file
        self.tarif = tarif
        self.date = datetime.today().date()
    
    def public_setTarif(self):
        with open(self.file, "w") as file:
            file.write("# Stand: {}\n{}".format(self.date, self.tarif))
            print("tarif sucessfully set to: {}", self.tarif)
