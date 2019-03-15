#Import the libraries into environment
#NLTK contains the routines for language processing text

import collections
import re
import nltk
from nltk.corpus import stopwords

#load the stop words list

stop_words = stopwords.words('english')

#Open the text file to process
#indicate the name of the file to open

fileName = input("Enter the name of the text file including the extension: ")

#Take the name of the text file and load into memory and process it

words = re.findall(r'\w+', open(fileName).read().lower())
most_common = collections.Counter(words).most_common(100)

#Create a list of words with their occurences 

most_common =  [(word, count) for word, count in most_common if word not in stop_words]

#Print the output to the screen

print ("Here are the results: ")
print(most_common)
