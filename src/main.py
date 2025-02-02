import os
import pandas as pandas

from dotenv import load_dotenv
from file.file_processor import FileProcessor
from graph.box_plot import BoxPlot


def main():
    load_dotenv()

    try:
        df = pandas.read_csv(os.getenv("CURRENT_FILE_PATH"))
        # print(df.head())

        if os.getenv("ENABLE_DF_INFOS"):
            FileProcessor().write_df_infos_file(dataframe=df)
        if os.getenv("ENABLE_DF_INFOS"):
            FileProcessor().write_df_stats_file(dataframe=df)
        if os.getenv("ENABLE_DF_INFOS"):
            FileProcessor().write_df_column_stats(dataframe=df)

        if os.getenv("ENABLE_BOX_PLOT_GRAPH"):
            box_plot = BoxPlot(
                data=df,
                y="against_bug",
                title="Gráfico de caixa (against_bug)",
            )
            box_plot.draw()

    except Exception as exception:
        print(exception)


main()
