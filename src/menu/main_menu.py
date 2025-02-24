import sys
from file.file_processor import FileProcessor


OPTION_EXIT = 0
OPTION_FILE_ANALYSIS = 1
OPTION_COLUMN_VALUE_COUNTS = 2
OPTION_COLUMN_ANALYSIS = 3
OPTION_GRAPH = 4


class MainMenu():

    def __init__(self, df):
        self.df = df

    def print_options(self):
        while (True):
            print("\nMENU INICIAL")
            print("0-Sair")
            print("1-Gerar arquivo info() e describe()")
            print("2-Gerar arquivo value_counts()")
            print("3-Gerar arquivo describe() de uma coluna específica")
            print("4-Gerar gráfico para análise")

            option = int(input("Escolha uma opção: "))
            if option == OPTION_EXIT:
                self.exit()
            elif option == OPTION_FILE_ANALYSIS:
                file_processor = FileProcessor(dataframe=self.df)

                print("Gerando arquivos...")
                file_processor.write_df_infos_file()
                file_processor.write_df_stats_file()
                print("Arquivos gerados com sucesso!")
            elif option == OPTION_COLUMN_VALUE_COUNTS:
                for data in self.df:
                    file_processor = FileProcessor(
                        dataframe=self.df, folder="columns")
                    file_processor.write_df_column_value_counts(column=data)
            elif option == OPTION_COLUMN_ANALYSIS:
                for data in self.df:
                    file_processor = FileProcessor(
                        dataframe=self.df, folder="stats")
                    file_processor.write_df_column_stats(column=data)
            elif option == OPTION_GRAPH:
                pass
