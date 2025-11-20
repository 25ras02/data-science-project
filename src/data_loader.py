import pandas as pd
from pathlib import Path

def load_data():
    data_path = Path(__file__).parent.parent / "data" / "sample_data.csv"
    df = pd.read_csv(data_path)
    return df