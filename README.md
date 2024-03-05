# HistoricalDataTransformation
Assumptions:
1. Missing compensation, review, and engagement data is inherited from the most recent past record.
2. The 'End Date' is set to '2100-01-01' for the latest record of an employee.

Approach:
The transformation process involves iteratively parsing through employee data rows, deriving effective and end dates. Compensation, review, and engagement data are individually handled, with missing values inherited from the most recent past record. Each iteration builds a historical record, and the resulting records are stored in a list. The process ensures a row-based historical versioning system with proper date intervals, culminating in the creation of an output CSV file suitable for analysis in a data warehouse.
