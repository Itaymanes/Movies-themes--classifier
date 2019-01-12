import pickle
import os
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse import csr_matrix

# Building Sparse Matrix of Clusters(Movies_id*Total_words)
dir_path = os.path.dirname(os.path.realpath(__file__))
pickle_file = os.path.join(dir_path,'cluster.pickle')
pickle_file_movie = os.path.join(dir_path,'movie_dict_full_file.pickle')
sparse_pickle_file = os.path.join(dir_path,'cluster_matrix_check.pickle')

with open(pickle_file, 'rb') as in_file:
    cluster_labels = pickle.load(in_file)
    cluster_inertia = pickle.load(in_file)
    cluster_centers = pickle.load(in_file)
    cluster_to_words = pickle.load(in_file)

with open(pickle_file_movie, 'rb') as in_file:
    movies_dict = pickle.load(in_file)
    year_dict = pickle.load(in_file)
    total_words_set = pickle.load(in_file)
list_words = list(total_words_set)
Words_Clusters_mat = lil_matrix((len(total_words_set), len(cluster_to_words)))
list_k = sorted(cluster_to_words, key=lambda k: len(cluster_to_words[k]), reverse=True)
for ind_cluster, k in enumerate(list_k):
    r = np.zeros([1,len(total_words_set)])
    for ind, words in enumerate(list_words):
        if words in cluster_to_words[k]:
            r[0,ind] = 1
    Words_Clusters_mat[:,ind_cluster] = r.T
    if (ind_cluster % 20) == 0:
        print(ind_cluster)

with open(sparse_pickle_file, 'w+b') as out_file:
    pickle.dump(Words_Clusters_mat, out_file)










