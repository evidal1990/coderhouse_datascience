import sys
from graph.graph_generator import GraphGenerator
from menu.boxplot_menu import BoxplotMenu

OPTION_EXIT = 0
OPTION_BOXPLOT = 1
OPTION_SWARMPLOT = 2
OPTION_VIOLINPLOT = 3
OPTION_BACK = 9

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

        option = int(input("Escolha uma opção: "))

        if option == OPTION_EXIT:
            sys.exit()
        elif option == OPTION_BOXPLOT:
            self.boxplot_menu = BoxplotMenu(df=self.df)
            self.boxplot_menu.print_options()
        else:
            pass
