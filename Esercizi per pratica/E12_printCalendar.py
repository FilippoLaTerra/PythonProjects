import calendar

def get_year():

    while(True):
        year = input("inserire l'anno:\n")

        try:
            year = int(year)
            if year >= 0:
                return year
            else:
                print("Anno non valido, l'anno deve essere maggiore o uguale a 0")     
        except:
            print("Anno non valido, l'anno deve essere maggiore o uguale a 0")        


def get_month():
    
    while(True):
        month = input("inserire il mese\n")

        try:
            month = int(month)
            if month <= 12 and month >= 1:
                return month
            else:
                print("Mese non valido, deve essere un numero compreso tra 1 e 12")
        except:
             print("Mese non valido, deve essere un numero compreso tra 1 e 12")    


print("\n" + calendar.month(get_year(), get_month()))