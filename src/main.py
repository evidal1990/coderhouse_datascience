import os
import pandas as pandas

from dotenv import load_dotenv
from file.file_processor import FileProcessor


def main():
    load_dotenv()

    try:
        df = pandas.read_csv(os.getenv("CURRENT_FILE_PATH"))
        df.head()

        FileProcessor().write_df_info_file(dataframe=df)
        FileProcessor().write_df_description_file(dataframe=df)

    except Exception as exception:
        print(exception)


main()
