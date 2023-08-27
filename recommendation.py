import numpy as np
from sklearn.cluster import KMeans
# import scrapingtest
# import database
import numbers

# all_trials = scrapingtest.fetch_data()
# trials_list2 = database.get_data()
# all_trials.trials = all_trials.trials + trials_list2.trials



def prep_data(all_trials):
    # np.random.seed(42)

    # Prep Data
    min_age_column = []
    max_age_column = []
    name_column = []
    ethnicity_column = []
    gender_column = []

    for trial in all_trials.trials :
        # not all the trials have the correct age data set in the correct format. I will assume its open to all ages
        if isinstance(trial.age_range[0], numbers.Number):
            min_age_column.append(trial.age_range[0])
        else:
            min_age_column.append(0)

        if isinstance(trial.age_range[1], numbers.Number):
            max_age_column.append(trial.age_range[1])
        else:
            max_age_column.append(100)

        # max_age_column.append(trial.age_range[1])
        name_column.append(trial.name)

        if type(trial.ethnicity) is list :
          ethnicity_column.append(trial.ethnicity[0])
        else:
          ethnicity_column.append(trial.ethnicity)

        if(trial.gender == 'males'):
          gender_column.append('male')
        elif(trial.gender == 'females'):
          gender_column.append('female')
        else:
          gender_column.append(trial.gender)

    min_age_column = np.array(min_age_column)
    max_age_column = np.array(max_age_column)
    # name_column = np.array(name_column)
    ethnicity_column = np.array(ethnicity_column)
    gender_column = np.array(gender_column)

    # Encode categorical variables (ethnicity and gender)
    ethnicity_mapping = {
      'African American': 0, 
      'Asian': 1, 
      'Hispanic': 2, 
      'Middle Eastern': 3, 
      'N/A': 4, 
      'Native American': 5, 
      'Pacific Islander': 6, 
      'South Asian': 7, 
      'White': 8 
    }
    gender_mapping = {'male': 0, 'female': 1, 'all': 2}

    encoded_ethnicity = np.array([ethnicity_mapping[e] for e in ethnicity_column])
    encoded_gender = np.array([gender_mapping[g] for g in gender_column])

    # Combine features
    X = np.column_stack((min_age_column, max_age_column, encoded_ethnicity, encoded_gender))

    # Number of clusters (recommendation groups)
    num_clusters = 5

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(X)


    # Create a dictionary to map cluster IDs to names
    cluster_name_mapping = {cluster_id: [] for cluster_id in range(num_clusters)}
    for i, name in enumerate(name_column):
        cluster_name_mapping[cluster_labels[i]].append(name)

    return (ethnicity_mapping, gender_mapping, kmeans, cluster_name_mapping)

def get_recommendation(all_trials, age, ethnicity, gender, numRecommendations = 5):
    
    ethnicity_mapping, gender_mapping, kmeans, cluster_name_mapping = prep_data(all_trials)

    encoded_ethnicity = ethnicity_mapping[ethnicity]
    encoded_gender = gender_mapping[gender]

    input_data = np.array([[age, age, encoded_ethnicity, encoded_gender]])
    cluster_id = kmeans.predict(input_data)[0]

    recommended_names = cluster_name_mapping[cluster_id]
    if len(recommended_names) == 0:
        return []

    size = min(len(recommended_names), numRecommendations)

    return np.random.choice(recommended_names, size)





# if __name__ == "__main__":

#   recommendations = get_recommendation(18, "Hispanic", "male")

#   if len(recommendations) == 0:
#     print("No recommendations available")
#   else:
#     for r in recommendations:
#       print(r)

#   gender_set = set()
#   for trial in all_trials.trials :
#     if type(trial.gender) is list :
#       gender_set.add(trial.gender[0])
#     else:
#       gender_set.add(trial.gender)
