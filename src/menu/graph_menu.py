import sys
from const.graph_menu_option import GraphMenuOption
from menu.boxplot_menu import BoxplotMenu
from menu.swarmplot_menu import SwarmplotMenu


class GraphMenu():

    def __init__(self, df):
        self.df = df

    def print_options(self):
        print("\nMENU GRÁFICOS")
        print("0-Sair")
        print("1-Boxplot")
        print("2-Swarmplot")
        print("3-Violinplot")
        print("9-Voltar ao menu inicial")

        option = GraphMenuOption(input("Escolha uma opção: "))
        print(option)

        if option == GraphMenuOption.EXIT:
            sys.exit()
        elif option == GraphMenuOption.BOXPLOT:
            boxplot_menu = BoxplotMenu(df=self.df)
            boxplot_menu.print_options()
        elif option == GraphMenuOption.SWARMPLOT:
            swarmplot_menu = SwarmplotMenu(df=self.df)
            swarmplot_menu.print_options()
        elif option == GraphMenuOption.VIOLINPLOT:
            pass
        elif option == GraphMenuOption.BACK:
            pass
        else:
            pass
