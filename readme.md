# Data Reconciliation Project

A Python-based data reconciliation system that compares datasets from source and target systems to identify discrepancies, missing records, and data quality issues.

## Purpose

This tool automates the process of reconciling data between two systems by:
- Identifying records present in source but missing in target
- Detecting unexpected records in target that don't exist in source
- Finding value mismatches in matching records
- Generating detailed reconciliation reports for data validation

## Features

- **Automated Comparison**: Compare large datasets efficiently using composite keys
- **Comprehensive Reports**: Generate CSV reports for missing records, extra records, and value mismatches
- **Data Profiling**: Track data quality metrics before and after transformations
- **Modular Design**: Separate modules for extraction, transformation, and reconciliation
- **Flexible Key Matching**: Support for single or composite key columns
- **Performance Optimized**: Uses PyArrow backend for faster data processing

## Requirements

- Python 3.8+
- pandas
- pyarrow

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ChachaMarwaDev/Project-Data-Reconciliation.git
cd Project-Data-Reconciliation
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install pandas pyarrow
```

## Project Structure

```
data-reconciliation-project/
│
├── data/                          # Data directory
│   ├── source_system.csv         # Source system data (input)
│   ├── target_system.csv         # Target system data (input)
│
├── src/                           # Source code modules
│   ├── extract.py                # Data extraction functions
│   ├── transform.py              # Data cleaning and transformation
│   ├── reconcile.py              # Reconciliation logic
│
├── reports/                       # Generated reports
│   ├── reconciliation_summary.csv        # High-level summary statistics
│   ├── missing_in_target.csv            # Records in source but not target
│   ├── extra_in_target.csv              # Records in target but not source
│   ├── value_mismatches.csv             # Matching records with different values
│   ├── profile_afterCleaning.json       # Data quality metrics
│
├── logs/                          # Log files
│   └── reconciliation.log        # Process logs
│
├── main.py                        # Main entry point
├── .gitignore                     # Git ignore file
├── checklist.md                   # Project requirements checklist
└── README.md                      # This file
```

## Usage

### Basic Reconciliation

1. Place your CSV files in the `data/` directory:
   - `source_system.csv` - Your source data
   - `target_system.csv` - Your target data

2. Run the reconciliation:
```bash
python main.py
```

3. Check the `reports/` directory for generated reconciliation reports

### Expected Data Format

Your CSV files should contain these columns (or similar):
- `Row ID` - Unique row identifier
- `Order ID` - Order identifier
- `Product ID` - Product identifier
- `Customer ID`, `Customer Name` - Customer information
- `Order Date`, `Ship Date` - Date fields
- `Sales`, `Category`, `Product Name` - Transaction details
- Other relevant business fields

### Key Column Configuration

By default, the reconciliation uses `Order ID` + `Product ID` as composite keys. To change this, modify `main.py`:

```python
results = reconcile_data(
    source_data, 
    target_data,
    key_columns=['Order ID', 'Product ID']  # Change these
)
```

## Output Reports

### 1. Reconciliation Summary (`reconciliation_summary.csv`)
High-level statistics about the reconciliation:
- Total records in source and target
- Count of missing records
- Count of extra records
- Count of matched records
- Count of value mismatches
- Reconciliation rate percentage

### 2. Missing in Target (`missing_in_target.csv`)
Records that exist in source but are absent from target. These may indicate:
- Data not synced yet
- Failed transfers
- Data loss issues

### 3. Extra in Target (`extra_in_target.csv`)
Records in target that don't exist in source. These may indicate:
- Duplicate records
- Manual data entry
- Data migration issues

### 4. Value Mismatches (`value_mismatches.csv`)
Records with matching keys but different values. Shows:
- Which fields differ
- Source value vs Target value
- Helps identify transformation issues

### 5. Data Profile (`profile_afterCleaning.json`)
JSON report containing:
- Row and column counts
- Data types
- Null value counts
- Duplicate record counts

## Module Details

### `extract.py`
- Loads CSV files from the data directory
- Uses PyArrow backend for performance
- Returns pandas DataFrames

### `transform.py`
- Removes records with missing postal codes
- Standardizes date formats
- Normalizes product names to lowercase
- Generates data quality profiles

### `reconcile.py`
- Compares datasets using specified key columns
- Identifies missing, extra, and mismatched records
- Generates detailed reconciliation reports
- Calculates reconciliation metrics

## Customization

### Adding Custom Transformations

Edit `src/transform.py` to add your own data cleaning rules:

```python
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    # Add your custom transformations here
    df['Email'] = df['Email'].str.lower()
    df['Phone'] = df['Phone'].str.replace('-', '')
    
    return df
```

### Changing Comparison Columns

Edit the `value_columns` list in `src/reconcile.py`:

```python
value_columns = ['Sales', 'Customer Name', 'Ship Mode', 
                 'Your_Custom_Column']
```

## Performance Considerations

- Uses PyArrow backend for 2-5x faster CSV reading
- Efficient set operations for key matching
- Recommended for datasets up to 10M records
- For larger datasets, consider chunking or Dask

## Troubleshooting

**Issue**: `FileNotFoundError`
- **Solution**: Ensure CSV files are in the `data/` directory with correct names

**Issue**: `KeyError` on columns
- **Solution**: Verify your CSV has the expected column names

**Issue**: Memory errors with large files
- **Solution**: Process data in chunks or increase available RAM

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Future Enhancements

- [ ] Add logging functionality
- [ ] Support for Excel and database sources
- [ ] Web-based dashboard for viewing reports
- [ ] Automated email notifications
- [ ] Fuzzy matching for near-duplicates
- [ ] Statistical tolerance thresholds for numeric fields
- [ ] Schedule reconciliation jobs

## License

This project is open source and available under the MIT License.

## Author

**Chacha Marwa**
- GitHub: [@ChachaMarwaDev](https://github.com/ChachaMarwaDev)

## Acknowledgments

- Built with pandas and PyArrow
- Inspired by financial reconciliation processes
- Designed for data quality assurance workflows

---

**Last Updated**: December 2025
