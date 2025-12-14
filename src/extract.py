from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")

def extract_csv(filename: str) -> pd.DataFrame:

    file_path = DATA_DIR / filename
    print('loading', file_path.resolve())

    df = pd.read_csv(file_path, dtype_backend ='pyarrow', engine='pyarrow')
    return df