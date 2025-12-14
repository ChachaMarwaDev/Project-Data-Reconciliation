Of course! Here is the data quality checklist, transformed into a clear, actionable checklist format.

You can copy and paste this into any document or checklist tool.

---

### **Data Quality Assurance Checklist**

#### **Stage 1: Discovery & Profiling**
- [ ] **Schema Detected:** Is a schema (structure) successfully detected from the raw data?
- [ ] **Data Types Inferred:** Are data types (e.g., integer, string, date) correctly inferred for each column?
- [ ] **Missing Values %:** Is the percentage of missing/null values calculated for each column?
- [ ] **High Cardinality Columns:** Are any columns with an extremely high number of unique values (like IDs or free-text) identified?
- [ ] **Outliers & Ranges:** Are outliers detected, and are the min/max ranges for numerical columns understood?

**Implementation Tools:** `pandas-profiling`, `Great Expectations`, or custom summary logic.

---

#### **Stage 2: Cleaning & Validation**
- [ ] **Remove Duplicates:** Are all duplicate rows identified and removed (or handled)?
- [ ] **Handle Nulls Consistently:** Are missing values handled (e.g., filled, imputed, or dropped) based on a consistent rule set?
- [ ] **Standardize Formats:** Are dates, phone numbers, and other formatted data standardized into a single format?
- [ ] **Standardize Casing & Naming:** Is text data (e.g., categories, names) converted to a consistent case (e.g., lower, upper, title)?
- [ ] **Normalize Categorical Values:** Are categorical values (e.g., "USA", "U.S.A", "United States") mapped to consistent, canonical values?

**Implementation Guideline:** Use rules defined in a config file (YAML/JSON), not hard-coded in scripts.

---

#### **Stage 3: Structuring & Enrichment**
- [ ] **Correct Column Order & Naming:** Are columns in the correct, desired order and named according to project standards?
- [ ] **Derived Columns Computed:** Are all new, calculated columns (e.g., `age` from `birth_date`, `total_price`) correctly computed?
- [ ] **External Mapping/Joins Applied:** Are lookups or joins with external datasets (e.g., adding region names from a region ID) successfully applied and validated?

**Implementation Guideline:** Use transformation functions with clear input/output signatures.

---

#### **Stage 4: Final Validation & QA**
- [ ] **Schema Matches Desired Format:** Does the final dataset's schema (column names, types, order) exactly match the expected target format?
- [ ] **Column-Level Expectations Passed:** Do all columns pass defined quality checks (e.g., values within a specific range, specific string format)?
- [ ] **Row Count Change Justified:** Is any significant change in the number of rows from input to output understood and justified?
- [ ] **Data Types Final Check:** Are all data types in their final, correct form (especially important for dates and numerical IDs)?

**Implementation Tools:** `Great Expectations`, `Cerberus`, or custom validation scripts.

---

#### **Stage 5: Delivery & Publishing**
- [ ] **File Format Correct:** Is the output file in the correct format (e.g., CSV, Parquet, JSON) with proper encoding?
- [ ] **Naming Versioned:** Is the output file named using a consistent versioning scheme (e.g., `dataset_v2_20231027.csv`)?
- [ ] **Access Permissions Set:** Are the correct read/write permissions set on the file or in the database?
- [ ] **Process Logged:** Has the entire process, including any errors or row counts, been logged for auditability?

**Implementation Guideline:** Use a controlled, standardized output function for all deliveries.

---

#### **Stage 6: Monitoring & Maintenance**
- [ ] **Log Anomalies:** Are any quality check failures or anomalies from this run logged for future review?
- [ ] **Re-check Incoming Data:** Is a plan in place to re-run profiling on the next batch of incoming data to detect drift?
- [ ] **Auto-Notify on Drift:** Are there automated alerts set up to notify the team if data quality drifts beyond a set threshold?

**Implementation Guideline:** If the data source is an API or regularly updated, schedule a re-validation routine.