import pandas as pd
import os
import numpy as np
from subject_info import SubjectInfo

SUM_FIELDS = ["Q1_1", "Q1_2", "Q1_3", "Q1_4", "Q1_5","Q1_6", "Q1_7", "Q1_8", "Q2"]
PROLIFIC_ID_CODE = "PROLIFIC_PID"
PHQ_SCORE_NAME = "PHQ_SCORE"


def load_phq(phq_dir_path):
    result_df = pd.DataFrame({PROLIFIC_ID_CODE: [], 'phq_score': []})
    result_df.set_index(PROLIFIC_ID_CODE, inplace=True)
    for file in os.listdir(phq_dir_path):
        filename = os.path.join(phq_dir_path, file)
        cur_data = pd.read_csv(filename)
        for index, row in cur_data.iterrows():
            try:
                cur_id = row[PROLIFIC_ID_CODE]
                phq_score = 0
                for column in cur_data:
                    if column in SUM_FIELDS:
                        phq_score += int(row[column])
                cur_df  =pd.DataFrame({PROLIFIC_ID_CODE: [cur_id], 'phq_score': [phq_score]})
                cur_df.set_index(PROLIFIC_ID_CODE, inplace=True)
                result_df = pd.concat([cur_df, result_df])
            except ValueError:
                continue
    return result_df


def load_second_study(second_study_results):
    df = pd.read_csv(second_study_results)
    df.set_index("Prolific ID", inplace=True)
    return df



def create_subject_list(first_study_df: pd.DataFrame, second_study_df: pd.DataFrame):
    lst = []
    for index, row in second_study_df.iterrows():
        if 'Prolific ID' in index or "ImportId" in index:
            continue
        prolificID = index
        first_mood_columns = ['Q48_1', 'Q49_1', 'Q50_1', 'Q51_1', 'Q52_1', 'Q53_1']
        first_mood_questions = np.array([row[cur_col] for cur_col in first_mood_columns])
        event_description_txt = row['Q16']
        first_cause_txt = row['Q17']
        first_cause_questions_columns = ['Q22_1', 'Q23_1', 'Q24_1', 'Q25_1','Q26_1', 'Q27_1', 'Q28_1', 'Q29_1']
        first_casue_questions_result = np.array([row[cur_col] for cur_col in first_cause_questions_columns])
        second_mood_columns = ['Q56_1', 'Q57_1', 'Q58_1', 'Q59_1', 'Q60_1', 'Q61_1']
        second_mood_questions = np.array([row[cur_col] for cur_col in second_mood_columns])
        second_cause_txt = row['Q11']
        second_case_questions_columns = ['Q30_1', 'Q31_1', 'Q32_1', 'Q33_1', 'Q34_1', 'Q35_1', 'Q36_1', 'Q37_1']
        second_cause_questions_result = np.array([row[cur_col] for cur_col in second_case_questions_columns])
        third_mode_columns = ['Q63_1', 'Q64_1', 'Q65_1', 'Q66_1', 'Q67_1', 'Q68_1']
        third_mood_questions = np.array([row[cur_col] for cur_col in third_mode_columns])
        rumination_columns = ['Q70_1', 'Q70_2', 'Q70_3', 'Q70_4', 'Q70_5', 'Q70_6','Q70_7', 'Q70_8', 'Q70_9', 'Q70_10',
                                'Q69_1', 'Q69_2', 'Q69_3', 'Q69_4', 'Q69_5', 'Q69_6', 'Q69_7', 'Q69_8', 'Q69_9', 'Q69_10'
                                , 'Q69_11', 'Q69_12']
        rumination_questions = np.array([row[cur_col] for cur_col in rumination_columns])
        phq_score = first_study_df['phq_score'][prolificID]
        lst.append(SubjectInfo(prolificID=str(prolificID), first_mood_questions=first_mood_questions, event_description_txt=event_description_txt,
                               first_cause_txt=first_cause_txt, first_casue_questions_result=first_casue_questions_result, second_mood_questions=second_mood_questions,
                               second_cause_txt=second_cause_txt, second_cause_questions_result=second_cause_questions_result,
                               third_mood_questions=third_mood_questions, rumination_questions=rumination_questions, phq_score=phq_score))
    return lst

def get_preprocess_data(first_study_path, second_study_path):
    first_study = load_phq(first_study_path)
    second_study = load_second_study(second_study_path)
    return create_subject_list(first_study, second_study)


def get_relevent_phq(phq_dir_path):
    df = load_phq(phq_dir_path)
    high_depression = []
    low_depression = []
    for index, row in df.iterrows():
        try:
            if df['phq_score'][index] >= 15:
                high_depression.append(index)
            elif df['phq_score'][index] <= 5:
                low_depression.append(index)
        except:
            continue
    print("high depression:")
    for d in high_depression:
        print(d)
    print("\n low depression")
    for l in low_depression:
        print(l)
if __name__ == '__main__':
    get_relevent_phq('PHQ_data')
    # first_study = load_phq("PHQ_data")
    # second_study = load_second_study('first_results.csv')
    # x = create_subject_list(first_study, second_study)
    # print(x[0].prolificID)