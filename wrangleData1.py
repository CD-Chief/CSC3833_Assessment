import pandas as pd
import pycountry

# Load the Excel file
df = pd.read_excel('CountryEconomics.xlsx')

# Function to convert 2-letter to 3-letter abbreviations
def alpha2_to_alpha3(alpha2):
    if pd.isna(alpha2):
        return None
    try:
        country = pycountry.countries.get(alpha_2=alpha2)
        return country.alpha_3 if country else None
    except (AttributeError, LookupError, KeyError):
        return None

# Create the new column
df['Abbreviation_3'] = df['Abbreviation'].apply(alpha2_to_alpha3)

# Save back to the Excel file
df.to_excel('CountryEconomics.xlsx', index=False)

print("Successfully added 'Abbreviation_3' column to CountryEconomics.xlsx")
print(f"Converted {df['Abbreviation_3'].notna().sum()} out of {len(df)} countries")
