from graph.swarmplot import Swarmplot


class SwarmplotMenu:

    def __init__(self, df):
        self.df = df

    def print_options(self):

        column = input("Informe a coluna a ser analisada: ")
        if column not in self.df.columns:
            print("Coluna não encontrada")
            return
        swarmplot = Swarmplot(
            data=self.df,
            y=column,
            title=f'Swarmplot ({column})',
            src=column
        )
        swarmplot.draw()
        swarmplot.save()
