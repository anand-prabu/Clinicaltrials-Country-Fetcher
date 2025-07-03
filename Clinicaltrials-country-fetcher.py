import pandas as pd
from tqdm import tqdm
import requests

df = pd.read_csv ('/path/to/your/Obesity P3 Recruiting_3JUL25.csv') #Provide the actual path to the input CSV file

def get_all_countries_from_nct(nct_id):
    
    api_url = f"https://clinicaltrials.gov/api/v2/studies/{nct_id}"
    
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status() 
    
        data = response.json()
        locations = data.get('protocolSection', {}).get('contactsLocationsModule', {}).get('locations', [])
        
        if not locations:
            return []

        all_countries = [loc.get('country') for loc in locations if loc.get('country')]
        unique_countries = sorted(list(set(all_countries)))
        
        return unique_countries
            
    except requests.exceptions.RequestException:
        return []
    except Exception:
        return []

tqdm.pandas(desc="Fetching All Countries")

df['All_Countries'] = df['NCT Number'].progress_apply(
    lambda x: ", ".join(get_all_countries_from_nct(x))
)

print("DataFrame with the new 'All_Countries' column (string format):")
print(df[['NCT Number', 'Locations', 'All_Countries']].head(10))

df.to_excel ('Obesity_P3 w countries.xlsx')