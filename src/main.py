import os
import sys
import pandas as pandas

from dotenv import load_dotenv
from file.file_processor import FileProcessor
from graph.graph_generator import GraphGenerator
from menu.const.main_menu_option import MainMenuOption

from graph.box_plot import BoxPlot
from graph.swarmplot import Swarmplot
from graph.violinplot import ViolinPlot

CURRENT_COLUMN = "against_dark"

menu_options = {
    "main": {
        "exit": 0,
        "file_analysis": 1,
        "column_value_counts": 2,
        "column_analysis": 3,
        "graph": 4,
    },
    "graph": {
        "exit": 0,
        "boxplot": 1,
        "swarmplot": 2,
        "violinplot": 3,
        "back_to_main_menu": 9,
    }
}


def main():
    load_dotenv(override=True)

    try:
        df = pandas.read_csv(os.getenv("CURRENT_FILE_PATH"))
        if not isinstance(df, pandas.core.frame.DataFrame):
            raise Exception("O arquivo informado não é um dataframe.")

        print(menu_options.get("main").get("exit"))

        show_initial_menu = True
        while (show_initial_menu):
            initial_menu_option = int(init_menu())

            if (initial_menu_option == menu_options.get("main").get("exit")):
                sys.exit()

            if (initial_menu_option == menu_options.get("main").get("file_analysis")):
                init_file_analysis(df=df)

            if (initial_menu_option == menu_options.get("main").get("column_value_counts")):
                init_column_analysis(df=df)

            if (initial_menu_option == menu_options.get("main").get("graph")):
                init_graph_generation(df=df)

        # if json.loads(os.getenv("ENABLE_DF_COLUMNS_STATS").lower()):
        #     file_processor = FileProcessor(
        #         dataframe=df, folder=CURRENT_COLUMN)
        #     file_processor.write_df_column_stats(column=CURRENT_COLUMN)

    except Exception as exception:
        print(exception)


def init_menu():
    print("\nMENU INICIAL")
    print("0-Sair")
    print("1-Gerar arquivo info() e describe()")
    print("2-Gerar arquivo value_counts()")
    print("3-Gerar arquivo describe() de uma coluna específica")
    print("4-Gerar gráfico para análise")

    return input("Escolha uma opção: ")


def init_graph_menu():
    print("\nMENU GRÁFICOS")
    print("0-Sair")
    print("1-Boxplot")
    print("2-Swarmplot")
    print("3-Violinplot")
    print("9-Voltar ao menu inicial")

    return input("Escolha uma opção: ")


def init_file_analysis(df):
    file_processor = FileProcessor(dataframe=df)

    print("Gerando arquivos...")
    file_processor.write_df_infos_file()
    file_processor.write_df_stats_file()
    print("Arquivos gerados com sucesso!")


def init_column_analysis(df):
    column_name = input("Informe uma coluna: ")

    if column_name in df:
        file_processor = FileProcessor(
            dataframe=df, column="against_bug")
        file_processor.write_df_column_value_counts()
    else:
        raise Exception("Coluna inexistente no dataframe")


def init_graph_generation(df):
    show_menu = True
    while (show_menu):
        menu_option = init_graph_menu()
        graph_generator = GraphGenerator()

        if (menu_option == "1"):
            analysis_type = input("Informe o tipo de análise a ser feita: ")
            if analysis_type == "univariada":
                column_name_y = input("Informe a coluna (y): ")
                graph_generator.draw_box_plot(
                    dataframe=df,
                    x=None,
                    y=column_name_y,
                    src=column_name_y
                )
            else:
                column_name_x = input("Informe a coluna (x): ")
                column_name_y = input("Informe a coluna (y): ")
                graph_generator.draw_box_plot(
                    dataframe=df,
                    x=column_name_x,
                    y=column_name_y,
                    src=f'{column_name_x}_{column_name_y}'
                )

        if (menu_option == "2"):
            column_name_y = input("Informe uma coluna: ")
            graph_generator.draw_swarmplot(
                dataframe=df,
                column=column_name_y
            )

        if (menu_option == "3"):
            column_name_y = input("Informe uma coluna: ")
            graph_generator.draw_violinplot(
                dataframe=df,
                column=column_name_y
            )

        if (menu_option == "9"):
            show_menu = False
            init_menu()

        if (menu_option == "0"):
            sys.exit()


main()
