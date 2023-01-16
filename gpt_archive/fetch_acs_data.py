import requests
import sys
import os

# Assign api_key from the command line argument
api_key = sys.argv[1]

# Years to collect the ACS data for
years_to_collect = [str(year) for year in range(2010, 2022)]

# Create directory to store data in
os.makedirs('data/acs5_housing_allegheny_county_by_tract', exist_ok=True)

# Iterate through each neighborhood
for year in years_to_collect:

    # Base URL for the Census API
    base_url = f'https://api.census.gov/data/{year}/acs/acs5'

    # Construct the API request URL
    url = f'{base_url}/profile?get=group(DP04)&for=tract:*&in=county:003+state:42&key={api_key}'
    print(url)

    # Send the request and get the response
    response = requests.get(url)

    # Remove the braces - this will leave it in csv format
    response_content = response.text.replace("[", "").replace("[", "")

    # Save the data to a file
    with open(f'data/acs5_housing_allegheny_county_by_tract/{year}.csv', 'w') as f:
        f.write(response_content)

