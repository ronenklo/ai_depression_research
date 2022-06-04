import pandas as pd
import os


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
    df.drop(labels='StartDate', inplace=True, axis=1)
    df.drop(labels='EndDate', inplace=True, axis=1)
    df.drop(labels='Status', inplace=True, axis=1)
    df.drop(labels='IPAddress', inplace=True, axis=1)
    df.drop(labels='Progress', inplace=True, axis=1)
    df.drop(labels='Duration (in seconds)', inplace=True, axis=1)
    df.drop(labels='Finished', inplace=True, axis=1)
    df.drop(labels='RecordedDate', inplace=True, axis=1)
    df.drop(labels='ResponseId', inplace=True, axis=1)
    df.drop(labels='RecipientLastName', inplace=True, axis=1)
    df.drop(labels='RecipientFirstName', inplace=True, axis=1)
    df.drop(labels='PROLIFIC_PID', inplace=True, axis=1)
    df.drop(labels='RecipientEmail', inplace=True, axis=1)
    df.drop(labels='ExternalReference', inplace=True, axis=1)
    df.drop(labels='LocationLatitude', inplace=True, axis=1)
    df.drop(labels='LocationLongitude', inplace=True, axis=1)
    df.drop(labels='DistributionChannel', inplace=True, axis=1)
    df.drop(labels='UserLanguage', inplace=True, axis=1)
    df.drop(labels='Q15', inplace=True, axis=1)
    print(df)
if __name__ == '__main__':
    # df = load_phq("PHQ_data")
    # print(df)
    load_second_study('first_results.csv')