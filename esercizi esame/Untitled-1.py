



class Studente:
    
    def __init__(self, nome, codice, corso = ""):
        self.NomeEcognome = nome
        self.CodiceFiscale = codice
        self.CorsoDiStudi = corso
        self.Votazione = ""

    def assegnaVotazione(self, voto):
        if not self.CorsoDiStudi:
            return "Exception: Lo studente non segue nessun corso di studi"
        elif (voto > 0, voto < 100):
            self.Votazione = voto
        else:
            return "Exception: Voto non valido"

    def votazione(self):
        if not self.Votazione:
            return "N/A"
        else:
            return self.Votazione
            


studente1 = Studente("mario rossi", "MAROFSJNLO88")
studente2 = Studente("alessia bianchi", "ALBIAjbibwg66", "scienze politche")

print(studente1.assegnaVotazione(24))
print(studente2.assegnaVotazione(24))

print(studente1.votazione())
print(studente2.votazione())