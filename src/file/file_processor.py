import os


GENERAL_FOLDER = "results/general"
UNIVARIATE_FOLDER = "results/univariate"


class FileProcessor():

    def __init__(self):
        if not os.path.exists(GENERAL_FOLDER):
            os.makedirs(GENERAL_FOLDER)

        if not os.path.exists(UNIVARIATE_FOLDER):
            os.makedirs(UNIVARIATE_FOLDER)

    def write_df_infos_file(self, dataframe):
        if dataframe.empty:
            raise Exception("Dataframe sem dados para serem lidos")
        with open(f'{GENERAL_FOLDER}/df_infos.txt', "w") as file:
            dataframe.info(buf=file)

    def write_df_stats_file(self, dataframe):
        if dataframe.empty:
            raise Exception("Dataframe sem dados para serem lidos")
        with open(f'{GENERAL_FOLDER}/df_stats.txt', "w") as file:
            file.write(dataframe.describe().T.to_string())

    def write_df_column_stats(self, dataframe, column_name):
        if dataframe.empty:
            raise Exception("Dataframe sem dados para serem lidos")

        for data in dataframe:
            with open(f'{UNIVARIATE_FOLDER}/df_stats_{data}.txt', "w") as file:
                file.write(dataframe[data].describe().to_string())
