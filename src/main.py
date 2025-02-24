import os
import sys
import pandas as pandas

from dotenv import load_dotenv
from file.file_processor import FileProcessor
from graph.graph_generator import GraphGenerator
from menu.main_menu import MainMenu

CURRENT_COLUMN = "against_dark"

menu_options = {
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

        main_menu = MainMenu(df=df)
        main_menu.print_options()

    except Exception as exception:
        print(exception)


def init_graph_menu():
    print("\nMENU GRÁFICOS")
    print("0-Sair")
    print("1-Boxplot")
    print("2-Swarmplot")
    print("3-Violinplot")
    print("9-Voltar ao menu inicial")

    return input("Escolha uma opção: ")


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
            pass

        if (menu_option == "0"):
            sys.exit()


main()
