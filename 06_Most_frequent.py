import pickle
import os
import  pandas as pd
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse import csr_matrix

# Making a table of the most frequent words for each cluster

dir_path = os.path.dirname(os.path.realpath(__file__))
pickle_file_mat = os.path.join(dir_path,'movies_matrix.pickle')
pickle_file_movie = os.path.join(dir_path,'movie_dict_full_file.pickle')
pickle_file_cluster = os.path.join(dir_path,'cluster.pickle')

with open(pickle_file_mat,'rb') as in_file:
    # Matrix movies*words
    Words_Movies_mat = pickle.load(in_file)

with open(pickle_file_movie, 'rb') as in_file:
    # total_words_set dictionary
    movies_dict = pickle.load(in_file)
    year_dict = pickle.load(in_file)
    total_words_set = pickle.load(in_file)

with open(pickle_file_cluster, 'rb') as in_file:
    cluster_labels = pickle.load(in_file)
    cluster_inertia = pickle.load(in_file)
    cluster_centers = pickle.load(in_file)
    cluster_to_words = pickle.load(in_file)

list_words = list(total_words_set)

freq_array = Words_Movies_mat.sum(axis=0)
#freq_sorted = np.sort(freq_array, axis = 1)

print('words',len(list_words))
print('freq',freq_array.shape)
dictionary = dict(zip(list_words, freq_array.T))

df = pd.DataFrame(columns = range(1,11))
#df.loc[i] = row