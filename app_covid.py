import requests
import locale

"""
Documentation at
https://documenter.getpostman.com/view/10808728/SzS8rjbc
"""

# 1. get the API data from the web server
# This API server does not require an API key
# 2. Convert the data into a useful python objects: usually a list or dictionaries
url = "https://api.covid19api.com/summary"

print("Total Deaths")
# Make API call and get response

response = requests.get(url)

# Convert response to dictionary object
data = response.json()
# print(type(data))
# Get global statistics from data dictionary
global_stats = data['Global']

# Extract total deaths and total cases from global statistics
deaths = global_stats['TotalDeaths']
cases = global_stats['TotalConfirmed']

# Calculate mortality rate
mortality_rate = deaths / cases

# Print output
# print("Total Deaths Worldwide: " + str(deaths))
# print("Total Confirmed Cases Worldwide: " + str(cases))
# print(f"Mortality Rate: {mortality_rate:.3f}")
print(
    f"Total Deaths: {deaths:n}. Total Confirmed cases: {cases:n}. Mortality Rate: {mortality_rate:.3f}.")
