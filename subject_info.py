import numpy as np


class SubjectInfo:
    def __init__(self, prolificID: str, first_mood_questions: np.ndarray,
                 event_description_txt: str, first_cause_txt: str, first_casue_questions_result: np.ndarray,
                 second_mood_questions: np.ndarray, second_cause_txt: str, second_cause_questions_result: np.ndarray,
                 third_mood_questions: np.ndarray, rumination_questions: np.ndarray, phq_score: int):
        self.prolificID = prolificID
        self.first_mood_questions = first_mood_questions
        self.event_description_txt = event_description_txt
        self.first_cause_txt = first_cause_txt
        self.first_casue_questions_result = first_casue_questions_result
        self.second_mood_questions = second_mood_questions
        self.second_cause_txt = second_cause_txt
        self.second_cause_questions_result = second_cause_questions_result
        self.third_mood_questions = third_mood_questions
        self.rumination_questions = rumination_questions
        self.phq_score = phq_score