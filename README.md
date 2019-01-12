# Movies-themes--classifier
Can we recognize movies' trends across years by their subtitles only?

The question: Can we recognize movies' trends across years by their subtitles only? inspired us to explore if we could give a reasonable answer, and it functions as the main goal for our final project in Data Science course in the Hebrew University. 
Details of the data and the tools that we have been used during the project:
-	Data - The data we used for this purpose is 17.6 Giga-bite tar file that we downloaded from the website www.opensubtitle.com, contains millions of subtitles for 105412 movies since 1865 to 2016 and can be seen at www.imdb.com. 
-	Glove - 
Main processing stages (for more details one can look at the codes in the appendix):
### 1-	Extract_tar_file – 
Opening the tar file, for each movie taking only the first file in the folder (assuming that other versions does not differ in the context), and counting how many times shows every word, in the course of building two dictionaries and one set:
o	Movie_dictionary – {Movie's id1: {word1: counts1, word2:counts2, ….}, …}
o	Year_dictionary – {Year1: Movie's id1, Movie's id2, …}
o	Total_words_set –{word1,word2,….}
### 2-	Sparse_Matrix_Movies – 
Using Movie_dictionary  and Total_words_set  from stage 1, building sparse matrix of movies id and words occurrences:
o	Words_Movies_matrix – size of the matrix [Movies * Total_words]
### 3-4	Clustering & Export the results to excel 
Applying the trained glove.6B.300d over our total words set in order to cluster the whole words to 200 clusters only. Exporting the results to excel and manually define the name of the cluster and marking the general or the non-informative as 'cluster to remove'. 
### 5-	Sparse_Matrix_Clusters –
sd
we cainterest ofThis question is the main inters
For this purpose we were
