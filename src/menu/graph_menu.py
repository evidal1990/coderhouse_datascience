import sys
from const.graph_menu_option import GraphMenuOption
from graph.graph_generator import GraphGenerator
from menu.boxplot_menu import BoxplotMenu


class GraphMenu():

    def __init__(self, df):
        self.df = df
        self.graph_generator = GraphGenerator()

    def print_options(self):
        print("\nMENU GRÁFICOS")
        print("0-Sair")
        print("1-Boxplot")
        print("2-Swarmplot")
        print("3-Violinplot")
        print("9-Voltar ao menu inicial")

        option = GraphMenuOption(input("Escolha uma opção: "))

        if option == GraphMenuOption.EXIT:
            sys.exit()
        elif option == GraphMenuOption.BOXPLOT:
            self.boxplot_menu = BoxplotMenu(df=self.df)
            self.boxplot_menu.print_options()
        elif option == GraphMenuOption.SWARMPLOT:
            pass
        elif option == GraphMenuOption.VIOLINPLOT:
            pass
        elif option == GraphMenuOption.BACK:
            pass
        else:
            pass
