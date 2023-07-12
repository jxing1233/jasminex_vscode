from ClinicalTrial import ClinicalTrial

class TrialsList:

  def __init__(self):
    self.trials = []

  def append(self, clinical_trial:ClinicalTrial):
    self.trials.append(clinical_trial)

  def count(self):
    return len(self.trials)

  def print_trials(self):
    for t in self.trials:
      print(t)

  def print_trials_data(self):
    for t in self.trials:
      print(t.name, t.focus, t.gender, t.age_range, sep="\t")


  def get_json(self):
    trial_data = []
    for t in self.trials:
      trial_data.append(
        {
          "name":t.name,
          "gender":t.gender,
          "focus":t.focus,
          "age_range":t.age_range,
        }
      )
    json_data = {
      "trials": trial_data
    }
    return json_data
  

  def sort_age(self):
    new_trials_list = []
    # DO stuff here to the new list
    return new_trials_list

  def sort_focus(self):
    new_trials_list = []
    # DO stuff here to the new list
    return new_trials_list

  def sort_name(self):
    new_trials_list = []
    # DO stuff here to the new list
    return new_trials_list

  def sort_gender(self):
    new_trials_list = []
    # DO stuff here to the new list
    return new_trials_list

  def filter(self, focus=None, age=None, gender=None):
    new_trials_list = []
    # DO stuff here to the new list
    return new_trials_list

# trials = TrialsList()
# x = ClinicalTrial('Nightmares','ALL','Sleep', [45,60])
# y = ClinicalTrial('Tallness','F','Height', [40,70])
# z = ClinicalTrial('Soda','M','Health', [20,100])
# trials.append(x)
# trials.append(y)
# trials.append(z)
# print(trials.count())
# #trials.print_trials_data()
# print(trials.get_json())

# trials.filter(age = 45, gender="M")
