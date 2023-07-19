

class clinicaltrial:

    def __init__(self, name, person, focus, age, link): # person = gender, age = age range
        self.name = name # string
        self.gender = person # string [ALL, female, male]
        self.focus = focus # list of strings
        self.age_range = age # list [starting_age, ending_age], list of 2 nums in months
        self.link = link

    def get_age_range(self):
        return self.age_range

    def get_display_ages(self):
        starting_age = self.age_range[0] // 12 # double slashes --> integer
        ending_age = self.age_range[1] // 12
        return f"{starting_age} - {ending_age}"

    def __str__(self): # override print statement
        return f'The clinical trial of {self.name} focusing on {self.focus} for the gender of {self.gender} for the ages of {self.get_display_ages()}, link is {self.link}'
    # f allows you to call variables/functions inside of a print statement


# x = clinicaltrial('A', 'ALL', 'Sleep')
# y = clinicaltrial('Tallness', 'F', 'Height')
# print(x)
# print(y)