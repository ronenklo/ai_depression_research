from textblob import TextBlob
import numpy as np
from sklearn import tree
from transformers import pipeline
from data_reader import get_preprocess_data
from subject_info import SubjectInfo
import text2emotion as te
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
    # classifier = pipeline("sentiment-analysis", model='arpanghoshal/EmoRoBERTa')
    # print(classifier("please help"))
    # data = get_preprocess_data("PHQ_data", 'first_results.csv')
    # index = 4
    # res1 = classifier(data[index].first_cause_txt)
    # res2 = classifier(data[index].event_description_txt)
    # res3 = classifier(data[index].second_cause_txt)
    # print("phq_score: ", data[index].phq_score)
    # print(res1)
    # print(res2)
    # print(res3)
    # from transformers import pipeline

    # classifier = pipeline("text-classification", model='arpanghoshal/EmoRoBERTa',
    #                       return_all_scores=True)
    # prediction = classifier("I feel like I have felt so many emotions in the last few weeks. None of them were positive, and it scares the hell out of me.", )
    # print(prediction)
    print(te.get_emotion("I dreamt about the war and it was hard"))

    """
    Output:
    [[
    {'label': 'sadness', 'score': 0.0006792712374590337}, 
    {'label': 'joy', 'score': 0.9959300756454468}, 
    {'label': 'love', 'score': 0.0009452480007894337}, 
    {'label': 'anger', 'score': 0.0018055217806249857}, 
    {'label': 'fear', 'score': 0.00041110432357527316}, 
    {'label': 'surprise', 'score': 0.0002288572577526793}
    ]]
    """