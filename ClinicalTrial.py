class ClinicalTrial:

  def __init__(self, name, gender, focus, age_range = [0,1200]):
    self.name = name
    self.gender = gender
    self.focus = focus
    self.age_range = age_range


  def get_display_ages(self):
    starting_age = self.age_range[0] // 12
    ending_age = self.age_range[1] // 12
    return f"{starting_age} - {ending_age}"


  def __str__(self):
    return f'The clincal trial of {self.name} focusing on {self.focus} for the gender of {self.gender} for the ages of {self.get_display_ages()}' 
