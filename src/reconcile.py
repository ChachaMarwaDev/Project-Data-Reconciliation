# src/reconcile.py
import pandas as pd
from pathlib import Path

def reconcile_data(source_df: pd.DataFrame, target_df: pd.DataFrame, 
                   key_columns: list = ['Order ID', 'Product ID']) -> dict:
    """
    Compare source and target datasets to find discrepancies.
    
    Args:
        source_df: Source system data
        target_df: Target system data  
        key_columns: Column(s) that uniquely identify records
    
    Returns:
        Dictionary with reconciliation results
    """
    
    # Create composite key for easier comparison
    source_df = source_df.copy()
    target_df = target_df.copy()
    
    source_df['_key'] = source_df[key_columns].astype(str).agg('-'.join, axis=1)
    target_df['_key'] = target_df[key_columns].astype(str).agg('-'.join, axis=1)
    
    # Find records only in source (missing from target)
    missing_in_target = source_df[~source_df['_key'].isin(target_df['_key'])]
    
    # Find records only in target (extra/unexpected)
    extra_in_target = target_df[~target_df['_key'].isin(source_df['_key'])]
    
    # Find matching records for value comparison
    matched_keys = set(source_df['_key']) & set(target_df['_key'])
    
    # Compare values for matched records
    mismatches = []
    value_columns = ['Sales', 'Customer Name', 'Ship Mode', 'Category', 
                     'Sub-Category', 'Product Name', 'Postal Code']
    
    for key in matched_keys:
        source_row = source_df[source_df['_key'] == key].iloc[0]
        target_row = target_df[target_df['_key'] == key].iloc[0]
        
        differences = {}
        for col in value_columns:
            if col in source_df.columns and col in target_df.columns:
                if source_row[col] != target_row[col]:
                    differences[col] = {
                        'source_value': source_row[col],
                        'target_value': target_row[col]
                    }
        
        if differences:
            mismatches.append({
                'key': key,
                'order_id': source_row['Order ID'],
                'product_id': source_row['Product ID'],
                'differences': differences
            })
    
    # Generate summary
    summary = {
        'total_source_records': len(source_df),
        'total_target_records': len(target_df),
        'missing_in_target': len(missing_in_target),
        'extra_in_target': len(extra_in_target),
        'matched_records': len(matched_keys),
        'mismatched_values': len(mismatches),
        'reconciliation_rate': f"{(len(matched_keys) / len(source_df) * 100):.2f}%"
    }
    
    return {
        'summary': summary,
        'missing_in_target': missing_in_target.drop('_key', axis=1),
        'extra_in_target': extra_in_target.drop('_key', axis=1),
        'mismatches': pd.DataFrame(mismatches) if mismatches else pd.DataFrame()
    }


def generate_reconciliation_report(results: dict, output_dir: Path = Path('reports')):
    """Generate CSV reports from reconciliation results."""
    
    output_dir.mkdir(exist_ok=True)
    
    # Summary report
    summary_df = pd.DataFrame([results['summary']])
    summary_df.to_csv(output_dir / 'reconciliation_summary.csv', index=False)
    
    # Missing records report
    if not results['missing_in_target'].empty:
        results['missing_in_target'].to_csv(
            output_dir / 'missing_in_target.csv', index=False
        )
    
    # Extra records report  
    if not results['extra_in_target'].empty:
        results['extra_in_target'].to_csv(
            output_dir / 'extra_in_target.csv', index=False
        )
    
    # Mismatches report
    if not results['mismatches'].empty:
        results['mismatches'].to_csv(
            output_dir / 'value_mismatches.csv', index=False
        )
    
