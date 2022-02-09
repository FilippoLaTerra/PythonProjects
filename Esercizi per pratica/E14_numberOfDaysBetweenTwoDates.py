import calendar

class Date():

    def __init__(self, year, month, day):
        self.Year = year
        self.Month = month
        self.Day = day

    def toString(self):
        return str(self.Day) + "/" + str(self.Month) + "/" + str(self.Year)

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
            print("Anno non valido, l'anno deve essere un numero intero")        

def get_month():
    
    while(True):
        month = input("inserire il mese\n")

        try:
            month = int(month)
            if month <= 12 and month >= 1:
                return month
            else:
                print("Mese non valido, deve essere compreso tra 1 e 12")
        except:
             print("Mese non valido, deve essere un numero intero")    

def get_day(year, month):

    while(True):
        day = input("inserire il giorno\n")

        try:
            day = int(day)

            match month:
                
                case 4, 6, 9, 11: 
                    if day <= 31 and day >= 1:
                        return day
                    else:
                        print("Giorno non valido")

                case 2: 
                    if calendar.isleap(year):
                        if day <= 29 and day >= 1:
                            return day
                        else:
                            print("Giorno non valido")
                    else:
                        if day <= 28 and day >= 1:
                            return day
                        else:
                            print("Giorno non valido")
                
                case _: 
                    if day <= 30 and day >= 1:
                        return day
                    else:
                        print("Giorno non valido")
               
        except:
             print("Mese non valido, deve essere un numero intero")

def get_date():

    year = get_year()
    month = get_month()
    day = get_day(year, month)

    return Date(year, month, day)


date1 = get_date()
print(date1.toString())

date2= get_date()
print(date2.toString())


