import calendar 
from datetime import datetime

class FridaysInMonth:
    def __init__ (self):
        now = datetime.now()
        self.year = now.year
        self.month = now.month
        self.month_name = now.strftime('%B')
    def get_third_friday(self):
        _, num_days = calendar.monthrange(self.year, self.month)

        fridays = [] # This is a list

        for day in range(1, num_days+1):
            date = datetime(self.year, self.month, day)
            if date.weekday() == 4:
                fridays.append(date.strftime('%d-%m-%Y'))
            
        return fridays[2]
    
    def printFridayInMonth(self):
        friday = self.get_third_friday()
        print(f"Your Expiry Date of {self.month_name} is: {friday}")

fridaysInSep = FridaysInMonth()
fridaysInSep.printFridayInMonth()
