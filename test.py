import numpy as np
from sklearn.cluster import KMeans

# Generate synthetic data (age, ethnicity, gender)
np.random.seed(42)
num_samples = 100
age = np.random.randint(18, 65, num_samples)
ethnicity = np.random.choice(['White', 'Black', 'Asian', 'Hispanic'], num_samples)
gender = np.random.choice(['Male', 'Female', 'Unspecified'], num_samples)

# Encode categorical variables (ethnicity and gender)
ethnicity_mapping = {'White': 0, 'Black': 1, 'Asian': 2, 'Hispanic': 3}
gender_mapping = {'Male': 0, 'Female': 1, 'Unspecified': 2}
encoded_ethnicity = np.array([ethnicity_mapping[e] for e in ethnicity])
encoded_gender = np.array([gender_mapping[g] for g in gender])

# Combine features
X = np.column_stack((age, encoded_ethnicity, encoded_gender))

# Number of clusters (recommendation groups)
num_clusters = 3

# Apply K-means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
cluster_labels = kmeans.fit_predict(X)

# Generate recommendations based on clusters
recommendations = []
for cluster_id in range(num_clusters):
    cluster_indices = np.where(cluster_labels == cluster_id)[0]
    cluster_data = X[cluster_indices]
    mean_age = np.mean(cluster_data[:, 0])
    mean_ethnicity = np.argmax(np.bincount(cluster_data[:, 1].astype(int)))
    mean_gender = np.argmax(np.bincount(cluster_data[:, 2].astype(int)))
    recommended_gender = list(gender_mapping.keys())[list(gender_mapping.values()).index(mean_gender)]
    if recommended_gender == 'Unspecified':
        recommended_gender = 'Any'
    recommendations.append({
        'ClusterID': cluster_id,
        'MeanAge': mean_age,
        'RecommendedEthnicity': list(ethnicity_mapping.keys())[list(ethnicity_mapping.values()).index(mean_ethnicity)],
        'RecommendedGender': recommended_gender
    })

# Print recommendations
for recommendation in recommendations:
    print(recommendation)
