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


    # removed missing values
    df = df[df['Postal Code'].notna()]

    # starndadized formats in my csv
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')
    df['Postal Code'] = df['Postal Code'].astype("string[pyarrow]")
    df['Product Name'] = df['Product Name'].str.lower()

    profile = {
        "num_rows": df.shape[0],
        "num_columns": df.shape[1],
        "columns": df.columns.tolist(),
        "null_values" : df.isnull().sum().to_dict(),
        "duplicates": int(df.duplicated().sum()),
        "datatypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        # 'summary_statistics': df.describe(include='all').to_dict()
    }

    import json
    with open('reports/profile_afterCleaning.json', 'w') as f:
        json.dump(profile, f, indent=4)
    
    return df