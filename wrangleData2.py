import pandas as pd

# Load the Excel file
df = pd.read_excel('CountryEconomics.xlsx')

# Clean population data: convert from millions to actual count
# Replace commas with periods, convert to float, multiply by 1,000,000
df['Population'] = df['Population'].astype(str).str.replace(',', '.').astype(float) * 1_000_000

# Save back to the Excel file
df.to_excel('CountryEconomics.xlsx', index=False)

print("Successfully converted Population to numeric (actual count)")
print(f"Sample populations:\n{df[['Country', 'Population']].head(10)}")
