from textblob import TextBlob
import numpy as np
from sklearn import tree
from transformers import pipeline

text = '''
There is something nice about the sun, striking my face.
Now I am very happy.
And now I am very sad. 

'''

# blob = TextBlob(text)
# print("tabgs", blob.tags)           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

# blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])
#
# for sentence in blob.sentences:
#     print(sentence)
#     print(sentence.sentiment.polarity)
#     print(sentence.sentiment.subjectivity )


def get_analysis_vect(text):
    polarity = []
    subjectivity = []
    blob = TextBlob(text)
    for sentence in blob.sentences:
        polarity.append(sentence.sentiment.polarity)
        subjectivity.append(sentence.sentiment.subjectivity)
    return np.array(polarity), np.array(subjectivity)

def predict(X, y):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, y)
    return clf


if __name__ == '__main__':
    classifier = pipeline("sentiment-analysis")
    res = classifier("This is the happiest wedding")
    print(res)