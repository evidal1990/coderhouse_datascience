import os


RESULTS_FOLDER = "results"


class FileProcessor():

    def __init__(self, dataframe=None, folder="general", column=None):

        self.df = dataframe

        if self.df.empty:
            raise Exception("Dataframe sem dados para serem lidos")

        self.column = column
        self.folder = folder and f'{RESULTS_FOLDER}/{folder}'

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def write_df_infos_file(self):

        path = f'{self.folder}/df_infos.txt'
        with open(path, "w") as file:
            self.df.info(buf=file)

    def write_df_stats_file(self):

        path = f'{self.folder}/df_stats.txt'
        with open(path, "w") as file:
            file.write(self.df.describe().T.to_string())

    def write_df_column_stats(self, column):

        path = f'{self.folder}/df_{column}_stats.txt'
        with open(path, "w") as file:
            file.write(self.df[column].describe().to_string())

    def write_df_column_value_counts(self, column):

        path = f'{self.folder}/df_{column}_value_counts.txt'
        with open(path, "w") as file:
            value_counts = self.df[column].value_counts().reset_index()
            file.write(value_counts.to_string())
