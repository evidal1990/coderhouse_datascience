import os
import pandas as pandas

from dotenv import load_dotenv
from file.file_processor import FileProcessor


def main():
    load_dotenv()

    try:
        df = pandas.read_csv(os.getenv("CURRENT_FILE_PATH"))
        print(df.head())

        FileProcessor().write_df_infos_file(dataframe=df)
        FileProcessor().write_df_stats_file(dataframe=df)

    except Exception as exception:
        print(exception)


main()
