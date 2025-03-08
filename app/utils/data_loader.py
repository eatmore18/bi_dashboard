import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Function to load data from CSV file.
    """
    return pd.read_csv(file_path)
