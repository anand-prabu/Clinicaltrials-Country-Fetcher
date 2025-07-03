# Clinicaltrials-Country-Fetcher

This Python script fetches and appends **all unique country names** for each clinical trial in your dataset using the [clinicaltrials.gov API](https://clinicaltrials.gov/), and saves the results to an Excel file.  

Why this is needed:
The CT.gov posting lists the country info in the Locations field of the extract and it is cumbersome to enlist the countries. Especially for P3 trial which run acrosss multiple sites within a country and in many different countries.

This code is aimed at helping researchers and analysts enrich their trial data with geographic information.

Here is an example using Phase 3 trials of Obesity that are recruiting. 

Search query at CTG: https://clinicaltrials.gov/search?cond=Obesity&aggFilters=phase:3,status:rec
Data retrieved on: 3 Jul 2025

The code pulled the country details for 60 trials neatly in a separate column in just 23 seconds! 

## Features

- Reads a CSV file containing clinical trial NCT Numbers.
- For each trial, retrieves all associated countries from clinicaltrials.gov. (unique countries)
- Adds a new column with the list of countries.
- Shows progress with a progress bar.
- Exports the updated DataFrame to Excel.

## Requirements

- Python 3.x
- [pandas](https://pandas.pydata.org/)
- [tqdm](https://tqdm.github.io/)
- [requests](https://requests.readthedocs.io/)

Install dependencies with:

pip install pandas tqdm requests


## Usage

1. **Edit the CSV path:**  
   Update the CSV file path in the script to match your file location:
df = pd.read_csv('/path/to/your/input.csv')


2. **Run the script:**  
Execute the script in your terminal:
python fetch_countries.py


3. **Output:**  
After running, you’ll get a new Excel file (`Obesity_P3 w countries.xlsx`) with an added column `All_Countries` listing all unique countries for each trial.

## Example

| NCT Number | Locations | All_Countries        |
|------------|-----------|----------------------|
| NCT0123456 | ...       | United States, India |
| NCT0987654 | ...       | Germany              |

## Notes

- The script handles API/network errors and will leave the country list empty if data is unavailable.
- Make sure your input CSV has a column named `NCT Number`. Here the file used is a direct download from Clinicaltrials.gov and hence the column name. Ensure to use the same column name or adjust the reference in the code to NCT IDs as needed.
- Used the file as is from CTG and hence the CSV format for input. Excel or Text files can be used too with appropriate edits to the code.

## License

This project is open-source and free to use for educational and research purposes.
