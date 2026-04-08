import pandas as pd

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df = df.dropna()
    df.columns = [col.strip().lower() for col in df.columns]
    return df
