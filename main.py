from src.extract import extract_csv 
from src.transform import transform_data

def main():
    try:
        raw_data = extract_csv(r"source_system.csv")
    except FileNotFoundError:
        print('Error: CSV file not found, check name or file path')
        return
    
    transformed = transform_data(raw_data)
    
    print(f'Rows before transforming: {len(raw_data)}')
    print(f'Rows after transforming: {len(transformed)}')



if __name__ == "__main__" :
    cleaned_df = main()
