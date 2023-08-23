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
        print(json_data)
        return json_data
    
    # try implementing the following files for hw
    
    def sort_age(self):
        # self.trials_sorted = []
        self.trials = sorted(self.trials, key=lambda element: (element.age_range[0], element.age_range[1])) # sorts the input
        # element = every item looping through
        # lambda function
        # each element in self.trials
                # add case if the initial ages are equal --> go to end ages, if age ranges identical, order is alphabetical
        # print(self.trials)
        return self.trials

    def sort_focus(self):
        self.trials = sorted(self.trials, key=lambda element: (element.focus))
        '''
        for i in range(self.count() - 1):
            for j in range(self.count() - 1):
                if self.trials[j].focus >= self.trials[j + 1].focus:
                    self.trials[j], self.trials[j+1] = self.trials[j+1], self.trials[j]
        '''
        return self.trials

    # alphabetical order name
    def sort_name(self):
        self.trials = sorted(self.trials, key=lambda element: (element.name))
        '''
        for i in range(self.count() - 1):
            for j in range(self.count() - 1):
                if self.trials[j].name >= self.trials[j + 1].name:
                    self.trials[j], self.trials[j+1] = self.trials[j+1], self.trials[j]
        '''
        return self.trials

    def sort_gender(self):
        self.trials = sorted(self.trials, key=lambda element: (element.gender))
        '''
        for i in range(self.count() - 1):
            for j in range(self.count() - 1):
                if self.trials[j].gender >= self.trials[j + 1].gender:
                    self.trials[j], self.trials[j+1] = self.trials[j+1], self.trials[j]
        '''
        return self.trials

    def filter(self, focus=None, age=None, gender=None): # none = null, filter only by one instead of all, can ignore the ones = None, in calling function, say focus = ""
        '''
        new_trials_list = []
        for t in self.trials:
            if focus and focus in t.focus:
                new_trials_list.append(t)
            elif age and age <= t.age_range[1] and age >= t.age_range[0]:
                new_trials_list.append(t)
            elif gender and (gender == t.gender or t.gender == "ALL"):
                new_trials_list.append(t)

        for i in new_trials_list:
            if not (focus and focus in t.focus and age and age <= t.age_range[1] and age >= t.age_range[0] and gender and (gender == t.gender or t.gender == "ALL")):
                new_trials_list.remove(i)
        '''
        new_trials_list = []
        for t in self.trials:
            if focus and focus in t.focus and age and age <= t.age_range[1] and age >= t.age_range[0] and gender and (gender == t.gender or t.gender == "ALL"):
                new_trials_list.append(t)
            elif focus and focus in t.focus and age and focus in t.focus and age <= t.age_range[1] and age >= t.age_range[0] and not gender:
                new_trials_list.append(t)
            elif focus and focus in t.focus and gender and (gender == t.gender or t.gender == "ALL") and not age:
                new_trials_list.append(t)
            elif gender and (gender == t.gender or t.gender == "ALL") and age and age <= t.age_range[1] and age >= t.age_range[0] and not focus:
                new_trials_list.append(t)
            elif gender and (gender == t.gender or t.gender == "ALL") and not focus and not age:
                new_trials_list.append(t)
            elif focus and focus in t.focus and not age and not gender:
                new_trials_list.append(t)
            elif age and age <= t.age_range[1] and age >= t.age_range[0] and not gender and not focus:
                new_trials_list.append(t)
            elif not gender and not focus and not age:
                new_trials_list.append(t)
        return new_trials_list

    def all_focuses(self):
        set_of_focuses = set()
        for i in self.trials:
            for g in i.get_focus():
                set_of_focuses.add(g)
        list_of_focuses = list(set_of_focuses)
        return list_of_focuses
    
    '''
    def concatenate(self, other_list): # pass in only the second list
        self.trials.
    '''


'''
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
#trials.sort_age()
#trials.print_trials_data()
trials.sort_focus()
trials.print_trials_data()
trials.sort_name()
trials.print_trials_data()
trials.sort_gender()
trials.print_trials_data()
list1 = trials.filter(age = 45, gender = "M")
print(list1)
'''
