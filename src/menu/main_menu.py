import sys
from file.file_processor import FileProcessor
from menu.graph_menu import GraphMenu
from menu.const.main_menu_option import MainMenuOption


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

            option = MainMenuOption(input("Escolha uma opção: "))
            print(option)
            if option == MainMenuOption.EXIT:
                sys.exit()
            elif option == MainMenuOption.FILE_ANALYSIS:
                file_processor = FileProcessor(dataframe=self.df)

                print("Gerando arquivos...")
                file_processor.write_df_infos_file()
                file_processor.write_df_stats_file()
                print("Arquivos gerados com sucesso!")
            elif option == MainMenuOption.COLUMN_ANALYSIS:
                for data in self.df:
                    file_processor = FileProcessor(
                        dataframe=self.df, folder="columns")
                    file_processor.write_df_column_value_counts(column=data)
            elif option == MainMenuOption.COLUMN_VALUES:
                for data in self.df:
                    file_processor = FileProcessor(
                        dataframe=self.df, folder="stats")
                    file_processor.write_df_column_stats(column=data)
            elif option == MainMenuOption.GRAPH:
                graph_menu = GraphMenu(df=self.df)
                graph_menu.print_options()
            else:
                print("Opção inválida")
