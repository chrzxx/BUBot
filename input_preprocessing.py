import json
import numpy as np
import random
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import langdetect as ld

words = []
classes = []
documents = []
stemmer = PorterStemmer()
stemming = []
ignore_words = ['?', '!']
stop_words = set(stopwords.words('english'))