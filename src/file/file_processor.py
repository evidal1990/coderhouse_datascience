import os


GENERAL_FOLDER = "results/general"
UNIVARIATE_STATS_FOLDER = "results/stats"


class FileProcessor():

    def __init__(self):
        if not os.path.exists(GENERAL_FOLDER):
            os.makedirs(GENERAL_FOLDER)

        if not os.path.exists(UNIVARIATE_STATS_FOLDER):
            os.makedirs(UNIVARIATE_STATS_FOLDER)

    def write_df_infos_file(self, dataframe):
        if dataframe.empty:
            raise Exception("Dataframe sem dados para serem lidos")

        path = f'{GENERAL_FOLDER}/df_infos.txt'
        with open(path, "w") as file:
            dataframe.info(buf=file)

    def write_df_stats_file(self, dataframe):
        if dataframe.empty:
            raise Exception("Dataframe sem dados para serem lidos")

        path = f'{GENERAL_FOLDER}/df_stats.txt'
        with open(path, "w") as file:
            file.write(dataframe.describe().T.to_string())

    def write_df_column_stats(self, dataframe):
        if dataframe.empty:
            raise Exception("Dataframe sem dados para serem lidos")

        for data in dataframe:
            path = f'{UNIVARIATE_STATS_FOLDER}/df_stats_{data}.txt'
            with open(path, "w") as file:
                file.write(dataframe[data].describe().to_string())
