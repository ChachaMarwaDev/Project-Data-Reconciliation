from src.extract import extract_csv 
from src.transform import transform_data
from src.reconcile import reconcile_data, generate_reconciliation_report

def main():
    try:
        raw_data = extract_csv(r"source_system.csv")
        source_data = extract_csv("source_system.csv")
        target_data = extract_csv("target_system.csv")
    except FileNotFoundError:
        print('Error: CSV file not found, check name or file path')
        return
    
    results = reconcile_data(
        source_data, 
        target_data,
        key_columns=['Order ID', 'Product ID']  # Composite key
    )

    for key, value in results['summary'].items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    # Generate reports
    generate_reconciliation_report(results)
    
    transformed = transform_data(raw_data)
    
    # print(f'Rows before transforming: {len(raw_data)}')
    # print(f'Rows after transforming: {len(transformed)}')

    # transformed.to_csv('data/target_system.csv' ,index=False)
    # print("clean data exported")

if __name__ == "__main__" :
    cleaned_df = main()
