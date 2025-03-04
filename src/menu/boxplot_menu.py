from menu.analysis_type_menu import AnalysisTypeMenu
from const.analysis_type_option import AnalysisTypeOption
from graph.graph import Graph


class BoxplotMenu():

    def __init__(self, df):
        self.df = df
        self.analysis_type_menu = AnalysisTypeMenu()

    def print_options(self):
        analysis_type_menu = AnalysisTypeMenu()
        analysis_option = AnalysisTypeOption(
            analysis_type_menu.print_options())

        axis_x = input("Informe a coluna principal: ")
        if axis_x not in self.df.columns:
            print("Coluna não encontrada")
            return
        if analysis_option == AnalysisTypeOption.UNIVARIATE:
            box_plot = Graph(
                data=self.df,
                x=None,
                y=axis_x,
                title=f'Boxplot (bivariada) {axis_x}',
                src=axis_x,
                palette="viridis",
                type="boxplot"
            )
            box_plot.draw_boxplot()
            box_plot.save()
        elif analysis_option == AnalysisTypeOption.BIVARIATE:
            axis_y = input("Informe a coluna secundária: ")
            if axis_y not in self.df.columns:
                print("Coluna não encontrada")
                return
            box_plot = Graph(
                data=self.df,
                x=axis_x,
                y=axis_y,
                title=f'Boxplot (univariada) {axis_x}_{axis_y}',
                src=f'{axis_x}_{axis_y}',
                palette="viridis"
            )
            box_plot.draw_boxplot()
            box_plot.save()
        else:
            print("Tipo de análise inválido")
