# cigar_recommender

WHAT IS THIS PROJECT ABOUT?

This is a personal project. Here, I am trying to build a machine learning model 
which will recommend me cigars based on the cigars that I liked and disliked in past. 

WHERE IS THE PROJECT CURRENTLY?

I am scraping cigar data from the web. I have two scripts to do that. 
One script scrapes various features about cigars, especially the link to each cigar's individual webpage.
Second script reads the information the first one creates and saves various information about cigars into a .csv file.
I am scraping information about cigars from Privada Cigar Club which is the shop I buy my cigars. I hope they don't mind.
I don't do anything commercial with the information I got from your website, guys. The sole purpose of this project is fun
and finding cigars for my taste with less effort.

HOW IT WORKS?

I used Beautiful Soup 4 to scrape various information about cigars from Privada Cigar Club's website. 
"scrape_cigars.py" gets "Brand", "Link", "Price", "Rating" info from on all "Rare" cigars on the website
and saves all the information in a table form as a .csv file (cigars.csv).

"scrape_reviews.py":

  1. Reads "cigars.csv"
  2. Opens links on the .csv file for each cigar
  3. Reads "Brand", "Description", "Reviewer", "User_Type", "Date", "Review", and "Rating" for each cigar
  4. Saves all the data in a table format as a .csv file (cigar_reviews.csv)

FUTURE WORK

Next, I want to create a dataset based on cigars I have tried so far including the same type of information as in the "cigar_reviews.csv" dataset.
I'll add one more column labeling each cigar as "Liked" or "Disliked". I'll perform NLP on the ground truth data 
to find most frequent words for "likes" and "dislikes". I can do some other NLP-based analysis to get some features that I can use to identify
"likes" and "dislikes". Finally, I'll build various machine-learning models and assess their performance. We'll see how it goes.

