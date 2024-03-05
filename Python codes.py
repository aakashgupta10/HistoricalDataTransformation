import pandas as pd
from datetime import datetime, timedelta
input_file = "C:\\Users\\msi1\\Downloads\\input.csv"
df = pd.read_csv(input_file)
df['Effective Date'] = df['Date of Joining']
df['End Date'] = df['Date of Exit'].fillna('2100-01-01')  # Fill missing exit dates with a far-future date

df.sort_values(['Employee Code', 'Effective Date'], inplace=True)
df.ffill(inplace=True)
date_columns = ['Compensation 1 date', 'Compensation 2 date', 'Review 1 date', 'Review 2 date', 'Engagement 1 date', 'Engagement 2 date']

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')
    df[col] = df.groupby('Employee Code')[col].ffill()

# ...

# Convert 'Effective Date' to datetime
df['Effective Date'] = pd.to_datetime(df['Effective Date'])

# Iterate through rows to create historical records with effective and end dates.
records = []
for _, row in df.iterrows():
    records.append(row.copy())  # Create a copy of the row to avoid modifying the original DataFrame
    end_date = row['Effective Date'] - timedelta(days=1)
    records[-1]['End Date'] = end_date

historical_df = pd.DataFrame(records)

# ...


historical_df.drop(columns=['Date of Joining', 'Date of Exit'], inplace=True)
historical_df = historical_df[['Employee Code', 'Manager Employee Code', 'Effective Date', 'End Date', 'Compensation', 'Compensation 1', 'Compensation 2', 'Review 1', 'Review 2', 'Engagement 1', 'Engagement 2']]

output_file = "C:\\Users\\msi1\\Downloads\\filess\\historical_data.csv"
historical_df.to_csv(output_file, index=False)
