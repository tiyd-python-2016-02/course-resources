from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

positive_words = [
    'sassy',
    'goat'
]

negative_words = [
    'sad',
    'panda'
]

vectorizer = CountVectorizer()

vectorizer.fit(positive_words + negative_words)

print('feature names:')
print(vectorizer.get_feature_names())

X = vectorizer.transform(positive_words + negative_words)
y = ['positive'] * len(positive_words) + ['negative'] * len(negative_words)

classifier = MultinomialNB()

classifier.fit(X, y)

print('train score:', classifier.score(X, y))

print('posi', classifier.predict(vectorizer.transform(['you\re a sassy pants'])))

print('neg', classifier.predict(vectorizer.transform(['you\re a sad panda'])))

print('not sure?', classifier.predict(vectorizer.transform(['you are a sassy sad goat panda'])))
