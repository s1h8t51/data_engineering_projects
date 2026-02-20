import pandas as pd
import numpy as np
import datetime as dt

### Chapter 1: Common Data Problems
### Fix structural issues like data types, impossible ranges, and duplicates.

import pandas as pd
import numpy as np
import datetime as dt

# 1. SETUP: Create a messy DataFrame that has ALL necessary columns
data = {
    'ride_id': [101, 101, 102, 103, 104],
    'user_id': [1, 1, 2, 3, 4],
    'duration': ['15 min', '15 min', '22 min', '4000 min', '30 min'],
    'user_birth_year': [1990, 1990, 1985, 2027, 1992],
    'price': ['$10', '$10', '$15', '$20', '$12'],
    'date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'rating': [5, 5, 4, 10, 3], # 10 is an out-of-range error
    'fund_A': [100, 100, 150, 200, 50],
    'fund_B': [50, 50, 50, 100, 50],
    'inv_amount': [150, 150, 200, 400, 100]
}

df = pd.DataFrame(data)

# --- SECTION 1: DATA TYPE CONSTRAINTS ---

# Convert 'duration' from string "15 min" to integer 15
df['duration'] = df['duration'].str.strip(' min').astype('int')

# Convert 'price' from string "$10" to integer 10
df['price'] = df['price'].str.strip('$').astype('int')

# Convert 'date' string to datetime objects
df['date'] = pd.to_datetime(df['date'])

# --- SECTION 2: DATA RANGE CONSTRAINTS ---

# Fix future years: Cap birth year at the current year (2026)
df.loc[df['user_birth_year'] > 2026, 'user_birth_year'] = 2026

# Fix ratings: Cap values above 5 at 5
df.loc[df['rating'] > 5, 'rating'] = 5

# --- SECTION 3: UNIQUENESS CONSTRAINTS (DUPLICATES) ---

# Drop identical rows (Rows 0 and 1 are identical)
df = df.drop_duplicates()

# Collapse with .groupby() 
# (In case there are multiple entries for one ride_id with different durations)
summaries = {'duration': 'mean', 'user_id': 'first', 'price': 'sum'}
df_unique = df.groupby('ride_id').agg(summaries).reset_index()

# --- SECTION 4: CROSS-FIELD VALIDATION ---

# Find rows where the sum of funds equals the investment amount
# This creates a boolean mask
inv_equ = (df['fund_A'] + df['fund_B']) == df['inv_amount']
consistent_data = df[inv_equ]

# --- FINAL RESULTS ---
print("--- Cleaned DataFrame ---")
print(df_unique)
print("\n--- Data Types ---")
print(df_unique.dtypes)



from thefuzz import process

# 1. SETUP: Messy Categorical Data
categories_list = ['italian', 'american', 'asian']
restaurants = pd.DataFrame({
    'rest_name': ['Pizzazzia', 'Burger King ', 'Italain Bistro', 'Sushi Zen'],
    'cuisine_type': ['italian', 'american', 'italain', 'asian'], # Typo: italain
    'city': ['New York', 'new york', 'NEW YORK ', 'Seattle']     # Inconsistent case/space
})

# 2. CLEANING: Case and Whitespace
restaurants['city'] = restaurants['city'].str.lower().str.strip()

# 3. CLEANING: Fuzzy Matching for Typos
# Find matches for 'italian' in the cuisine_type column
matches = process.extract('italian', restaurants['cuisine_type'], limit=len(restaurants))

for match in matches:
    # If similarity score is >= 80, replace with the correct string
    if match[1] >= 80:
        restaurants.loc[restaurants['cuisine_type'] == match[0], 'cuisine_type'] = 'italian'

print("Chapter 2 Result:\n", restaurants[['cuisine_type', 'city']])








import missingno as msno
import matplotlib.pyplot as plt

# 1. SETUP: Uniformity & Missing Values
banking = pd.DataFrame({
    'cust_id': [1, 2, 3, 4],
    'acct_amount': [1000, 1500, np.nan, 2000], # Missing value
    'acct_cur': ['dollar', 'euro', 'dollar', 'dollar'],
    'birth_date': pd.to_datetime(['1990-05-10', '1985-12-01', '1992-07-20', '1980-01-01']),
    'age': [36, 41, 34, 55], # Let's assume some are mathematically incorrect
    'inv_amount': [800, 1200, 500, 1600]
})

# 2. CLEANING: Uniformity (Currency conversion)
acct_eu = banking['acct_cur'] == 'euro'
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1
banking.loc[acct_eu, 'acct_cur'] = 'dollar'

# 3. CLEANING: Cross-Field Validation (Age Check)
today = dt.date.today()
# Calculate age manually from birth_date
ages_manual = today.year - banking['birth_date'].dt.year
age_equ = banking['age'] == ages_manual
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]

# 4. CLEANING: Imputing Missing Values
# Fill missing acct_amount with a calculated value (e.g., inv_amount * 1.2)
banking['acct_amount'] = banking['acct_amount'].fillna(banking['inv_amount'] * 1.2)

print("\nChapter 3 Result (Missing Values Handled):\n", banking[['acct_amount', 'acct_cur']])



import recordlinkage

# 1. SETUP: Two DataFrames to Link
df_a = pd.DataFrame({
    'rest_name': ['Mikes Pizza', 'Hot Burgers'],
    'city': ['Chicago', 'Boston'],
    'cuisine': ['italian', 'american']
}, index=[0, 1])

df_b = pd.DataFrame({
    'rest_name': ['Mikes Pizzeria', 'Burgers Hot'],
    'city': ['Chicago', 'Boston'],
    'cuisine': ['italiano', 'american']
}, index=[10, 11])

# 2. LINKING: Generating Pairs (Blocking)
indexer = recordlinkage.Index()
indexer.block('city')
pairs = indexer.index(df_a, df_b)

# 3. LINKING: Comparison Logic
compare_cl = recordlinkage.Compare()
compare_cl.exact('city', 'city', label='city')
compare_cl.string('rest_name', 'rest_name', method='jarowinkler', threshold=0.8, label='name')

# 4. LINKING: Computing and Finding Matches

features = compare_cl.compute(pairs, df_a, df_b)
# Potential matches must meet at least 2 criteria
matches = features[features.sum(axis=1) >= 2]

print("\nChapter 4 Result (Linked Pairs Found):\n", matches)

def main():
    # Place your data cleaning code here
    print("Running the cleaning pipeline...")
    # df = clean_data(df)

if __name__ == "__main__":
    main()