import os


RESULTS_FOLDER = "results/"
GENERAL_FOLDER = f'{RESULTS_FOLDER}/general'


class FileProcessor():

    def __init__(self, dataframe=None, folder=None):

        self.df = dataframe

        if self.df.empty:
            raise Exception("Dataframe sem dados para serem lidos")

        self.folder = folder and f'{RESULTS_FOLDER}/{folder}'

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        if not os.path.exists(GENERAL_FOLDER):
            os.makedirs(GENERAL_FOLDER)

    def write_df_infos_file(self):

        path = f'{self.folder}/df_infos.txt'
        with open(path, "w") as file:
            self.df.info(buf=file)

    def write_df_stats_file(self):

        path = f'{self.folder}/df_stats.txt'
        with open(path, "w") as file:
            file.write(self.df.describe().T.to_string())

    def write_df_column_stats(self, column):

        path = f'{self.folder}/df_stats.txt'
        with open(path, "w") as file:
            file.write(self.df[column].describe().to_string())

    def write_df_column_value_counts(self):

        path = f'{self.folder}/df_value_counts.txt'
        with open(path, "w") as file:
            value_counts = self.df[self.folder].value_counts().reset_index()
            file.write(value_counts.to_string())
