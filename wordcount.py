#Import the libraries into environment
#NLTK contains the routines for language processing text

import collections
import re
import nltk
from nltk.corpus import stopwords

#load the stop words list

stop_words = stopwords.words('english')

#open the text file to process
#indicate the name of the file to open

words = re.findall(r'\w+', open('common.txt').read().lower())
most_common = collections.Counter(words).most_common(100)

#Create an array of words with their occurences 

most_common =  [(word, count) for word, count in most_common if word not in stop_words]

#Print the output to a screen

print ("Here are the results: ")
print(most_common)
