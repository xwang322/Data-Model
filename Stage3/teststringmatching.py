from py_stringmatching import simfunctions, tokenizers
x = 'this is a string matching package for data science class'
y = 'this string matching package can be used to generate features'
f = simfunctions.cosine(tokenizers.whitespace(x), tokenizers.whitespace(y))
print(f)
a = 'power first 6cyy3 ivory surge protection outlet strip'
b = 'power first 6cyy5 ivory surge protection outlet strip'
a1 = a.split(' ')
b1 = b.split(' ')
print(a1,b1)
tfidf = simfunctions.tfidf(a1,b1)
jaccard = simfunctions.jaccard(a1,b1)
print(tfidf,jaccard)