import pandas as pd

class DataFrameHandler:
    @staticmethod
    def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
        """
        Realizamos limpieza básica de datos.
        """
        df.dropna(inplace=True)
        return df
