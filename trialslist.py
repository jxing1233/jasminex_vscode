from clinicaltrial import clinicaltrial

class trialslist:

    def __init__(self): 
        self.trials = []

    def append(self, clinical_trial:clinicaltrial):
        self.trials.append(clinical_trial)

    def count(self):
        return len(self.trials)
    
    def print_trials(self):
        for t in self.trials:
            print(t)

    def print_trials_data(self):
        for t in self.trials:
            print(t.name, t.focus, t.gender, t.age_range, t.link, sep="\t")

    def get_json(self):
        json_data = {} # almost like dictionary, like electric vs gas cars
        trial_data = [] # list
        for t in self.trials:
            trial_data.append(
                {
                    'name':t.name,
                    'gender':t.gender,
                    'focus':t.focus,
                    'age_range':t.age_range,
                    'link':t.link,
                }
            )
        json_data = {
            'trial': trial_data
        }
        return json_data
    
    # try implementing the following files for hw
    
    def sort_age(self):
        # self.trials_sorted = []
        for i in range(self.count() - 1):
            # starter = i
            for j in range(self.count() - 1):
                if self.trials[j].age_range[0] >= self.trials[j + 1].age_range[0]:
                    self.trials[j], self.trials[j+1] = self.trials[j+1], self.trials[j]
                    # starter+=1
                elif self.trials[j].age_range[0] >= self.trials[j + 1].age_range[0]:
                    if self.trials[j].age_range[1] >= self.trials[j + 1].age_range[1]:
                        self.trials[j], self.trials[j+1] = self.trials[j+1], self.trials[j]
                        # starter+=1
                # add case if the initial ages are equal --> go to end ages, if age ranges identical, order is alphabetical
        return self.trials

    def sort_focus(self):
        for i in range(self.count() - 1):
            for j in range(self.count() - 1):
                if self.trials[j].focus >= self.trials[j + 1].focus:
                    self.trials[j], self.trials[j+1] = self.trials[j+1], self.trials[j]
        return self.trials

    def sort_name(self):
        for i in range(self.count() - 1):
            for j in range(self.count() - 1):
                if self.trials[j].name >= self.trials[j + 1].name:
                    self.trials[j], self.trials[j+1] = self.trials[j+1], self.trials[j]
        return self.trials

    def sort_gender(self):
        for i in range(self.count() - 1):
            for j in range(self.count() - 1):
                if self.trials[j].gender >= self.trials[j + 1].gender:
                    self.trials[j], self.trials[j+1] = self.trials[j+1], self.trials[j]
        return self.trials

    def filter(self, focus=None, age=None, gender=None): # none = null, filter only by one instead of all, can ignore the ones = None, in calling function, say focus = ""
        new_trials_list = []
        for t in self.trials:
            if focus and t.focus == focus:
                new_trials_list.append(t)
        pass


        



trials = trialslist()
x = clinicaltrial('Nightmares', 'ALL', 'Sleep', [45, 60], 'https://www.google.com/')
y = clinicaltrial('Soda', 'M', 'Health', [20, 60], 'https://www.google.com/')
z = clinicaltrial('Tallness', 'F', 'Height', [45, 70], 'https://www.google.com/')
trials.append(y)
trials.append(z)
trials.append(x)
print(trials.count())
trials.print_trials()
trials.print_trials_data()
#print(trials.get_json())
trials.sort_age()
#trials.print_trials_data()
#trials.sort_focus()
#trials.sort_name()
#trials.sort_gender()
list1 = trials.filter(age = 45, gender = "M")
print(list1)
