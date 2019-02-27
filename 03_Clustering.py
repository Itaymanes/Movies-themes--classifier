from __future__ import division
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from numbers import Number
from pandas import DataFrame
import sys, codecs, csv
import numpy
from collections import defaultdict
import pickle
import codecs
import os


def build_word_vector_matrix(tag_array):
    numpy_arrays = []
    labels_array = []
    f.seek(0)
    for c, r in enumerate(f):
        sr = r.split()
        if sr[0] in tag_array:
            labels_array.append(sr[0])
            numpy_arrays.append(numpy.array([float(i) for i in sr[1:]]))
    return numpy.array(numpy_arrays), labels_array, len(tag_array)

def find_word_clusters(labels_array, cluster_labels):
    cluster_to_words = defaultdict(list)
    for c, i in enumerate(cluster_labels):
        cluster_to_words[i].append(labels_array[c])
    return cluster_to_words

dir_path = os.path.dirname(os.path.realpath(__file__))
pickle_file = os.path.join(dir_path,'movie_dict_5k.pickle')
pickle_file_cluster = os.path.join(dir_path,'cluster.pickle')

with open(pickle_file,'rb') as in_file:
    movies_dict = pickle.load(in_file)
    year_dict = pickle.load(in_file)
    total_words_set = pickle.load(in_file)
input_vector_file = 'D:/Renana/GloVe-1.2/WordClusters/glove.6B.300d.txt'
f = codecs.open(input_vector_file, 'r', 'utf-8')

df, labels_array, array_len  = build_word_vector_matrix(total_words_set)

clusters_to_make = int(200)
kmeans_model = KMeans(init='k-means++', n_clusters=clusters_to_make, n_init=10)
kmeans_model.fit(df)

cluster_labels = kmeans_model.labels_
cluster_inertia = kmeans_model.inertia_
cluster_centers = kmeans_model.cluster_centers_
cluster_to_words = find_word_clusters(labels_array, cluster_labels)
for key in cluster_to_words:
    if len(cluster_to_words[key]) != 1:
        clusterList, cluster_label_array, cluster_len = build_word_vector_matrix(cluster_to_words[key])
        centroid = []
        centroid.append(cluster_centers[key])
        closest, _ = pairwise_distances_argmin_min(centroid, clusterList)
    else:
        closest = [0]

    cluster_to_words[key] = [cluster_to_words[key][closest[0]]] + cluster_to_words[key]


with open(pickle_file_cluster,'w+b') as out_file:
    pickle.dump(cluster_labels,out_file )
    pickle.dump(cluster_inertia, out_file)
    pickle.dump(cluster_centers, out_file)
    pickle.dump(cluster_to_words, out_file)
