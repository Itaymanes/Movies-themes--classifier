import pickle
import os
import sys, codecs, csv
import codecs

dir_path = os.path.dirname(os.path.realpath(__file__))
pickle_file = os.path.join(dir_path,'movie_dict_70k.pickle')
pickle_file_cluster = os.path.join(dir_path,'cluster.pickle')

with open(pickle_file_cluster,'rb') as in_file:
    cluster_labels = pickle.load(in_file)
    cluster_inertia = pickle.load(in_file)
    cluster_centers = pickle.load(in_file)
    cluster_to_words = pickle.load(in_file)

imageData = open(dir_path + '\\clusters.csv', 'w', newline='')
imageDataWriter = csv.writer(imageData)

cluster_final = {}
for k in sorted(cluster_to_words, key=lambda k: len(cluster_to_words[k]), reverse=True):
    for ind, x in enumerate(cluster_to_words[k]):
        a = x.encode("ascii")
        cluster_to_words[k][ind] = bytes.decode(a)
    imageDataWriter.writerow(cluster_to_words[k])
imageData.close()
