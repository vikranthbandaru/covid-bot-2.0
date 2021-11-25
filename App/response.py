from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings 
warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)

URLS = ['https://www.unicef.org/india/coronavirus/covid-19','https://www.cdc.gov/coronavirus/2019-ncov/vaccines/facts.html','https://www.uptodate.com/contents/covid-19-questions-and-answers']

for i in range(0,2):
    article = Article(URLS[i]) 
    article.download()
    article.parse()
    article.nlp()
    corpus = article.text

def greeting_response(text):
    text = text.lower()

  #Bots greeting response
    bot_greetings = [ 'howdy','hi','hey','hello','hola']
  #Users greeting
    user_greetings = ['hi','hey','hello','hola', 'greetings','wassup','sup','hey bot','konnichiwa']


    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0,length))

    x = list_var
    for i in range(length):
      for j in range(length):
        if x[list_index[i]] > x[list_index[j]]:
          #swap
          temp = list_index[i]
          list_index[i] = list_index[j]
          list_index[j] = temp

    return list_index 

text = corpus
sentence_list = nltk.sent_tokenize(text) # A list of sentences
# print(sentence_list)


def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response=''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    print(similarity_scores)
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response+' '+sentence_list[index[i]]
            response_flag = 1
            j= j+1
        if j > 2:
            break

        if response_flag == 0:
            bot_response = bot_response+' '+"I do not understand your query, please try again."

        sentence_list.remove(user_input)

        return bot_response 

