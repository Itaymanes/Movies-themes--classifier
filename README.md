# Movies themes classifier
#### Can we recognize movies' trends across years by their subtitles only?

The question: Can we recognize movies' trends across years by their subtitles only? Inspired us to explore if we could give a reasonable answer. Thus, this question stands as the main goal for our final project in Data Science course.
In our opinion, in this case a good answer should hold at least two restrictions:
-	Sanity check - see if the themes (from here we will use the term – clusters to depict the themes) of the movies makes sense (i.e. will be surprising and misleading if ‘Lord of the rings’ have high value of ‘Us elections’).
-	Significant difference of the frequent and usage of some clusters across decades or other periods of time (if there is not difference we stay without interesting insights). 

Details of the data and the tools that we have been used during the project:
-	Data - The data we used for this purpose is 17.6 Giga-bite tar file that we downloaded from the website www.opensubtitle.com, contains almost one million of subtitles for 105,412 movies since 1865 to 2016 and can be seen at www.imdb.com. 
-	Glove – GloVe is an unsupervised learning algorithm for obtaining vector representations for words. Training is performed on aggregated global word-word co-occurrence statistics from a corpus, and the resulting representations showcase interesting linear substructures of the word vector space. (https://nlp.stanford.edu/projects/glove/). We were using the trained 300 dimensions file – ‘glove.42B.300d.txt’.
-	Power BI - To analyze our data we used Microsoft power BI. This tool helped us analyze the information we produced. He presented us in a clear way the trends over the years. 
Download Power BI Desktop 

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
Applying the trained ‘glove.42B.300d.txt’ over our total words set in order to cluster the whole words to 200 clusters only. Exporting the results to excel and manually define the name of the cluster and marking the general or the non-informative as 'cluster to remove'. 
An example of the output:


### 5-	Sparse_Matrix_Clusters –
Using Total_words_set  from stage 1, and clusters dictionary from stage 3,  building sparse matrix of words and clusters:
o	Clusters_matrix – size of the matrix [Total_words*Clusters]

### 6-	Analyzing data
Multiplication of the two matrices (stages 2 & 5) to get one matrix of [Movies * clusters], and then preforming sanity check and plotting the wanted graphs.

## Results:
In the graph below, we have selected different films and selected different topics to show how the topics are distributed across films. For Example “Pretty Woman” The main topics are Food, Bank/Money & Science fiction. Since we know that the film does not deal with science fiction and the cluster names is selected manually, we will conclude that there is an error in this matter. Besides, in general, we see that the division of the topics across the various films is entirely consistent with reality. 




In the graph below we picked three clusters and plotted their evolution over time in 100 years (1916-2016) in order to get insights about trends in the cinema. It is easy to see that at the beginning of the graph (till ~ 1935) the lines are more “noisy” since the amount of movies is much smaller and it is hard to say something strong about trends in this period of time. On the other hand, while the cluster ‘meds’ seems to oscillate around the same value, the cluster ‘US election’ have some noticeable spikes across time. 


<p align="center">
  <img src="https://i.imgur.com/8PrMYib.png" width="650" title="plot">
</p>


Below is example of the ability to see how the topics divided per selected year. For example the year 2014 we can see the mainly topics are Medicine and Middle East. In file attached you have the ability to choose a year and so see the topics related to that year. 






### Points for discussion:
-	Number of clusters
-	Normalization approaches
-	Further steps:
o	Ordering the clusters by the most frequent words and use it for “tuning” the clusters’ names.
o	Supply more data, such as reviews and summaries.

