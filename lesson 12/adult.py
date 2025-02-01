from challange.Person import Person

class adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 < = bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return 'overweight'
        else:
            return "obese"
..