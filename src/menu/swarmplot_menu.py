from graph.graph import Graph


class SwarmplotMenu:

    def __init__(self, df):
        self.df = df

    def print_options(self):

        column = input("Informe a coluna a ser analisada: ")
        if column not in self.df.columns:
            print("Coluna não encontrada")
            return
        swarmplot = Graph(
            data=self.df,
            x=None,
            y=column,
            title=f'Swarmplot ({column})',
            src=column,
            type="swarmplot"
        )
        swarmplot.draw_swarmplot()
        swarmplot.save()
