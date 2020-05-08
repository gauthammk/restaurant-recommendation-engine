import zomatopy
import pandas as pd

output = pd.DataFrame()

# get the API key and initialise the authorisation for the API
API_key_file = open('APIkey.txt', 'r')
API_key = API_key_file.readline()
config = {
    'user_key': API_key
}
zomatoHandler = zomatopy.initialize_app(config)
API_key_file.close()

# print available categories for reference
print('Categories : ', zomatoHandler.get_categories())
# add category if needed
category_id = ''

# get the restaurant details for the city you are in
bengaluru_city_id = zomatoHandler.get_city_ID('bengaluru')
collection_id = '1'
start = 0
limit = 20
r_ids = zomatoHandler.restaurant_search(
    bengaluru_city_id, category_id, collection_id, start, limit)
# add the restaurants to the dataframe
# for r_id in r_ids:
#     tempDict = zomatoHandler.get_restaurant(r_id)
#     output = output.append(tempDict, ignore_index=True)

# output.to_csv('restaurant_data_set.csv')
