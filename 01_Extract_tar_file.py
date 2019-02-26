import xml.etree.ElementTree as ET
import tarfile
from contextlib import closing
import gzip
from collections import defaultdict
import pickle
import os
import numpy as np

# important note!
# the way to connect the Id to the movie name:
# by using IMDB website: http://www.imdb.com/title/tt04037954/
# where '4037954' is the Id of the movie

def extract_year_movie_dict(name):
    # extract year of published and movie id
    ind_start_year_name = name.find('/en/')
    year = name[ind_start_year_name + 4:ind_start_year_name + 8]
    end_id = name.find('/', ind_start_year_name + 10)
    movie_id = name[ind_start_year_name + 9 : end_id]
    return movie_id, year

dir_path = os.path.dirname(os.path.realpath(__file__))
pickle_file = os.path.join(dir_path,'movie_dict_5k.pickle')
sparse_pickle_file = os.path.join(dir_path,'movies_matrix_5k.pickle')

if not os.path.isfile(pickle_file):
    movies_dict = defaultdict(dict)
    year_dict = defaultdict(set)
    total_words_set = set()

    with tarfile.open('C:/Users/itay manes/Downloads/en.tar.gz') as archive:
        for ind, member in enumerate(archive):
            count = defaultdict(int)
            if (ind % 5000 == 0):
                print(str(ind) +' iteration')
            movie_id, year = extract_year_movie_dict(member.name)
            if not (movie_id in year_dict[year]) and not (year[0] == '0'):               # using only single subtitle file
                year_dict[year].add(movie_id)
                if member.isreg() and member.name.endswith('.xml.gz'): # regular xml file
                    with closing(archive.extractfile(member)) as gzfile:
                        infile = gzip.open(gzfile)
                        tree = ET.parse(infile)
                        root = tree.getroot()
                        for elem in root:
                            for subelem in elem:
                                if not(subelem.text == None):
                                    count[subelem.text.lower()] += 1
                            movies_dict[movie_id] = count
            total_words_set.update(movies_dict[movie_id].keys())


    with open(pickle_file,'w+b') as out_file:
        pickle.dump(movies_dict,out_file )
        pickle.dump(year_dict, out_file)
        pickle.dump(total_words_set, out_file)

else:
    with open(pickle_file,'rb') as in_file:
        movies_dict = pickle.load(in_file)
        year_dict = pickle.load(in_file)
        total_words_set = pickle.load(in_file)

