import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Discovery and profiling
    # profile = {
    #     "num_rows": df.shape[0],
    #     "num_columns": df.shape[1],
    #     "columns": df.columns.tolist(),
    #     "null_values" : df.isnull().sum().to_dict(),
    #     "duplicates": int(df.duplicated().sum()),
    #     "datatypes": df.dtypes.astype(str).to_dict(),
    #     "missing_values": df.isnull().sum().to_dict(),
    #     'summary_statistics': df.describe(include='all').to_dict()
    # }

    # import json
    # with open('reports/profile_beforeCleaning.json', 'w') as f:
    #     json.dump(profile, f, indent=4)


    df = df['Postal Code'].dropna()

    
    return df