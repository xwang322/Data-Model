from nltk.corpus import wordnet
from itertools import chain

synonyms = wordnet.synsets('headphone')  # change this to find synoyms of the word 
lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
print(lemmas)