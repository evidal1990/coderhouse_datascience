from graph.graph_generator import GraphGenerator
from menu.analysis_type_menu import AnalysisTypeMenu
from const.analysis_type_option import AnalysisTypeOption

UNIVARIATE = 0
BIVARIATE = 1
MULTIVARIATE = 2


class BoxplotMenu():

    def __init__(self, df):
        self.df = df
        self.graph_generator = GraphGenerator()
        self.analysis_type_menu = AnalysisTypeMenu()

    def print_options(self):
        analysis_type_menu = AnalysisTypeMenu(self.df)
        analysis_option = AnalysisTypeMenu(analysis_type_menu.print_options())

        axis_x = input("Informe a coluna principal: ")
        if axis_x not in self.df.columns:
            print("Coluna não encontrada")
            return
        if analysis_option == AnalysisTypeOption.UNIVARIATE:
            self.graph_generator.draw_box_plot(
                dataframe=self.df,
                x=None,
                y=axis_x,
                src=axis_x
            )
        elif analysis_option == AnalysisTypeOption.BIVARIATE:
            axis_y = input("Informe a coluna secundária: ")
            if axis_y not in self.df.columns:
                print("Coluna não encontrada")
                return
            self.graph_generator.draw_box_plot(
                dataframe=self.df,
                x=axis_x,
                y=axis_y,
                src=f'{axis_x}_{axis_y}'
            )
        else:
            print("Tipo de análise inválido")
