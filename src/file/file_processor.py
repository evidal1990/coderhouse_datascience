import os


class FileProcessor():

    def __init__(self):
        if not os.path.exists("results"):
            os.makedirs("results")

    def write_df_info_file(self, dataframe):
        try:
            if dataframe.empty:
                raise Exception("Dataframe sem dados para serem lidos")
            with open("results/df_infos.txt", "w") as file:
                dataframe.info(buf=file)
        except Exception as exception:
            print(exception)

    def write_df_description_file(self, dataframe):
        try:
            if dataframe.empty:
                raise Exception("Dataframe sem dados para serem lidos")
            with open("results/df_describe.txt", "w") as file:
                file.write(dataframe.describe().T.to_string())
        except Exception as exception:
            print(exception)
