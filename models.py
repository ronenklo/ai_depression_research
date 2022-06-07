from abc import ABC, abstractmethod
from subject_info import SubjectInfo
from typing import List
import numpy as np

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import text2emotion as te

class SortByWordNumber:
    #TODO a class that sorts by the number of happy, sad,.. words in each text
    pass

def get_labels(x: List[SubjectInfo]):
    labels = np.zeros(len(x))
    for j, subject in enumerate(x):
        if subject.phq_score <= 5:
            labels[j] = 0
        elif subject.phq_score >= 15:
            labels[j] = 1
        else:
            continue
    return labels



class BaseModel(ABC):

    @abstractmethod
    def train_model(self, x):
        pass

    @abstractmethod
    def fit(self, x):
        pass

class PerTextModel(BaseModel, ABC):

    def __init__(self):
        self.model = te.get_emotion
        self.clf = None

    def vectorize_data(self, x):
        analysis_order = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
        data_vect = np.zeros((len(x), 15))
        for j, subject in enumerate(x):
            idx = 0
            for k, text in enumerate([subject.event_description_txt, subject.first_cause_txt, subject.second_cause_txt]):
                text_data = self.model(text)
                for i in range(len(analysis_order)):
                    data_vect[j, idx] = self.model(text_data[analysis_order[i]])
                    idx += 1
        return data_vect

    def train_model(self, x):
        labels = get_labels(x)
        data_vect = self.vectorize_data(x)
        self.clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
        self.clf.fit(data_vect, labels)

    def fit(self, x):
        vectorized_data, labels = self.vectorize_data(x)
        self.clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
        self.clf.fit(vectorized_data, labels)


class EveryWordModel(BaseModel, ABC):

    def __init__(self, nlp_model):
        self.model = nlp_model
        self.clf = None


    def vectorize_data(self, x: List[SubjectInfo]):
        vectorized_data = np.zeros((len(x), 60))
        labels = np.zeros(len(x))
        for j, subject in enumerate(x):
            for k, text in enumerate((subject.event_description_txt, subject.first_cause_txt, subject.second_cause_txt)):
                text_word_score = np.zeros(len(text))
                split_text = text.split()
                for i in range(len(split_text)):
                    text_word_score[i] = self.model(split_text[i])
                if k == 0:
                    text_word_score.sort()
                    vectorized_data[j, 0: 10] = text_word_score[0:10]
                    vectorized_data[j, 10: 20] = text_word_score[len(text_word_score) - 10:]
                if k == 1:
                    text_word_score.sort()
                    vectorized_data[j, 20: 30] = text_word_score[0:10]
                    vectorized_data[j, 30: 40] = text_word_score[len(text_word_score) - 10:]
                if k == 2:
                    text_word_score.sort()
                    vectorized_data[j, 20: 30] = text_word_score[0:10]
                    vectorized_data[j, 30: 40] = text_word_score[len(text_word_score) - 10:]
            if subject.phq_score <= 5:
                labels[j] = 0
            elif subject.phq_score >= 15:
                labels[j] = 1
            else:
                continue
        return vectorized_data, labels


    def train_model(self, x: List[SubjectInfo]):
        vectorized_data, labels = self.vectorize_data(x)
        self.clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
        self.clf.fit(vectorized_data, labels)


    def fit(self, x):
        vectorized_data, labels = self.vectorize_data(x)
        return self.clf.predict(vectorized_data), labels