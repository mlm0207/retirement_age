from datetime import date


class RetirementAgeCalculator:

    def __init__(self, year_of_birth, month_of_birth):
        self.year_of_birth = year_of_birth
        self.month_of_birth = month_of_birth
        self.current_year = date.today().year
        self.retirement_age = 0
        self.retirement_months = 0
        self.month_of_retirement = ""
        self.year_of_retirement = 0
        self.set_retirement_age_and_months()
        self.set_year_of_retirement()
        self.set_month_of_retirement()


    def get_current_age(self):
        age = self.current_year - self.year_of_birth
        return age


    def get_month(self, month):
        months = [0, "January", "February", "March", "April", "May", "June", "July",
                  "August", "September", "October", "November", "December"]
        return months[month]


    def set_retirement_age_and_months(self):

        if self.year_of_birth < 1943:
            self.retirement_age = 65

            if self.year_of_birth == 1938:
                self.retirement_months = 2
            elif self.year_of_birth == 1939:
                self.retirement_months = 4
            elif self.year_of_birth == 1940:
                self.retirement_months = 6
            elif self.year_of_birth == 1941:
                self.retirement_months = 8
            elif self.year_of_birth == 1942:
                self.retirement_months = 10

        elif self.year_of_birth < 1960:
            self.retirement_age = 66

            if self.year_of_birth == 1955:
                self.retirement_months = 2
            elif self.year_of_birth == 1956:
                self.retirement_months = 4
            elif self.year_of_birth == 1957:
                self.retirement_months = 6
            elif self.year_of_birth == 1958:
                self.retirement_months = 8
            elif self.year_of_birth == 1959:
                self.retirement_months = 10

        else:
            self.retirement_age = 67


    def set_month_of_retirement(self):
        birth_and_retirement_month = self.month_of_birth + self.retirement_months

        if birth_and_retirement_month > 12:
            self.year_of_retirement = self.year_of_retirement + 1

        if birth_and_retirement_month == 12:
            self.month_of_retirement = self.get_month(birth_and_retirement_month)

        else:
            self.month_of_retirement = self.get_month(birth_and_retirement_month % 12)


    def set_year_of_retirement(self):
        self.year_of_retirement = self.retirement_age - self.get_current_age() + self.current_year
