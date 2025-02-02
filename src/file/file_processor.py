import os


class FileProcessor():

    def __init__(self):
        if not os.path.exists("results"):
            os.makedirs("results")

    def write_df_infos_file(self, dataframe):
        if dataframe.empty:
            raise Exception("Dataframe sem dados para serem lidos")
        with open("results/df_infos.txt", "w") as file:
            dataframe.info(buf=file)

    def write_df_stats_file(self, dataframe):
        if dataframe.empty:
            raise Exception("Dataframe sem dados para serem lidos")
        with open("results/df_stats.txt", "w") as file:
            file.write(dataframe.describe().T.to_string())
