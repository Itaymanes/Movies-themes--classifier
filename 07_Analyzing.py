import pickle
import os
import pandas as pd
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse import csr_matrix

dir_path = os.path.dirname(os.path.realpath(__file__))
pickle_final_mat = os.path.join(dir_path, 'final_matrix.pickle')

if not os.path.isfile(pickle_final_mat):
    # Organizing data as DataFrame

    pickle_mat_movie = os.path.join(dir_path, 'movies_matrix.pickle')
    pickle_mat_cluster = os.path.join(dir_path, 'cluster_matrix_check.pickle')
    pickle_file_movie = os.path.join(dir_path, 'movie_dict_full_file.pickle')
    cluster_excel = os.path.join(dir_path, 'clusters_csv.xlsx')

    with open(pickle_mat_movie, 'rb') as in_file:
        Movies_mat = pickle.load(in_file)
    with open(pickle_mat_cluster, 'rb') as in_file:
        Clusters_mat = pickle.load(in_file)
    Clusters_mat = Clusters_mat.tocsr()
    #Clusters_mat = Clusters_mat.transpose()

    with open(pickle_file_movie, 'rb') as in_file:
        Movies_dict = pickle.load(in_file)
        year_dict = pickle.load(in_file)

    # Correcting the matrix
    list_ids = []
    for ind_movies, id_movies in enumerate(Movies_dict):
        list_ids.append(id_movies)
    s_ids = set(list_ids)

    list_years = []
    s_y = set()
    for i in year_dict:
        for k in year_dict[i]:
            s_y.add(k)
            list_years.append(i)
    s_not = s_ids - s_y
    list_ids_fin = [x for x in list_ids if x not in s_not]

    final_mat = Movies_mat * Clusters_mat
    cl_excel = pd.read_excel(cluster_excel, usecols=0, index_col=0, header=None)
    relevant_cols = [not ('Remove' in i) for i in cl_excel.index]

    df = pd.DataFrame(final_mat.todense(), index=list_ids, columns=cl_excel.index)
    df = df.loc[list_ids_fin]
    df = df.div(df.sum(axis=1), axis=0)  # Normelaize
    df = df.iloc[:, relevant_cols]
    df_year = df
    df_year['YEAR'] = list_years
    df_justy_year = df_year.groupby(['YEAR']).mean()

    with open(pickle_final_mat, 'w+b') as out_file:
        pickle.dump(df, out_file)
        pickle.dump(df_justy_year, out_file)
        pickle.dump(df_year, out_file)

else:
    with open(pickle_final_mat, 'rb') as in_file:
        df = pickle.load(in_file)
        df_year = pickle.load(in_file)


def Sample_plot(df):
    M_name_list = ['Pretty Woman(1990)','Jurassic Park(1993)', 'The Birds(1963)', 'Kill Bill: Vol. 1(2003)', 'Shrek(2001)','The Matrix(1999)']
    M_id_list = ['100405', '107290', '56869', '266697', '126029','133093']
