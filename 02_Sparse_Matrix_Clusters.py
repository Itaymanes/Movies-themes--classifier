import pickle
import os
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse import csr_matrix

# Building Sparse Matrix (Movies_id*Total_words)
dir_path = os.path.dirname(os.path.realpath(__file__))
pickle_file = os.path.join(dir_path,'movie_dict_5k.pickle')
sparse_pickle_file = os.path.join(dir_path,'movies_matrix_5k.pickle')

with open(pickle_file, 'rb') as in_file:
    movies_dict = pickle.load(in_file)
    year_dict = pickle.load(in_file)
    total_words_set = pickle.load(in_file)

list_words = list(total_words_set)
Words_Movies_mat = lil_matrix((len(movies_dict.keys()), len(total_words_set)))

for ind_movies, id_movies in enumerate (movies_dict):
    r = np.zeros([1,len(total_words_set)])
    for ind, words in enumerate(list_words):
        if words in movies_dict[id_movies]:
            r[0,ind] = movies_dict[id_movies][words]
    Words_Movies_mat[ind_movies,:] = r
Words_Movies_mat = Words_Movies_mat.tocsr()

with open(sparse_pickle_file, 'w+b') as out_file:
    pickle.dump(Words_Movies_mat, out_file)