import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer


# retrieve the csv dataset file.
def getDataSet(fav_cuisines):
    url = 'restaurant_data_set.csv'
    restaurants = pd.read_csv(url)
    # add a new row with a temporary restaurant for predicting similarity
    # the temp restaurant works as a reference for the algorithm
    new_row = {'id': None, 'name': 'Temp Restaurant',
               'cuisines': fav_cuisines}
    restaurants = restaurants.append(new_row, ignore_index=True)
    return restaurants


def getRecommendations(restaurants, title):
    # initialise the vectorizer
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2),
                         min_df=0, stop_words='english')
    # appy word vectorization to the cuisines attribute of the dataset
    tfidf_matrix = tf.fit_transform(restaurants['cuisines'])
    # find the cosine similarity matrix
    # the value cosine_sim[i][j] represents
    # the cosine similarity between restaurant[i] and restaurant[j]
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    titles = restaurants['name']
    indices = pd.Series(restaurants.index, index=restaurants['name'])
    # find the index of the temp restaurant
    idx = indices[title]
    # generate an (index, similarity score) list
    # for the temp restaurant w.r.t other restaurants
    sim_scores = list(enumerate(cosine_sim[idx]))
    # sort the list to get the restaurants that are more similar
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # get the top n similar restaurants
    top_n = 5
    sim_scores = sim_scores[1:top_n]
    # display the names and indices of the top n similar restaurants
    restaurant_indices = [i[0] for i in sim_scores]
    return titles.iloc[restaurant_indices]


# add favourite cuisines to search for
fav_cuisines = input()
restaurants = getDataSet(fav_cuisines)
# find similarity
print(getRecommendations(restaurants, 'Temp Restaurant'))
