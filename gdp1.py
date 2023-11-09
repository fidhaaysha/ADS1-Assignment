import pandas as pd
import matplotlib.pyplot as plt

# Function to create a line plot for selected countries

"""
Function to plot a line graph for the GDP trends of the selected countries
over the years. X-axis is defined as the time period (Year) 
and in the Y-axis, the GDP value of the countries is given which is indicated in GDP
in Billion US Dollars....
"""
def selected_countries_gdp(gdp_data, countries):
    selected_countries = gdp_data[gdp_data['Country Name'].isin(countries)]

    plt.figure(figsize=(10, 6))

    for country in countries:
        country_data = selected_countries[selected_countries['Country Name'] == country]
        plt.plot(country_data['Year'], country_data['Value'], label=country)

    plt.xlabel('Year')
    plt.ylabel('GDP Value')
    plt.title('GDP Trends for Selected Countries')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to create a scatter plot for a specific country

"""
Function to plot a scatter plot for the GDP trends of the United States.X-axis is defined 
as the time period (Year) and in the Y-axis, the GDP value of the US is given which
is indicated in GDP in Billion US Dollars....
"""
def country_gdp(gdp_data, country_name):
    plt.figure(figsize=(10, 6))

    data = gdp_data[gdp_data['Country Name'] == country_name]

    plt.scatter(data['Year'], data['Value'], label=country_name, color='red')

    plt.xlabel('Year')
    plt.ylabel('GDP Value')
    plt.title(f'GDP Trends for {country_name}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to create a pie chart of country income group distribution

"""
Function to plot a pie chart shows the distribution of income groups based on 
the 'income_group' column from the 'country_codes.csv' dataset for the GDP trends of the 
selected countries.....
"""
def income_group(data):
    plt.figure(figsize=(8, 8))
    income_group_counts = data['income_group'].value_counts()
    plt.pie(income_group_counts, labels=income_group_counts.index,
            autopct='%1.1f%%', startangle=140)
    plt.title('Income Group Distribution')
    plt.show()


# Loading GDP dataset and country code dataset
gdp_data = pd.read_csv('gdp_data.csv')
country_codes_data = pd.read_csv('country_codes.csv')

# Selecting specific countries for line plot
countries = ['United States', 'China', 'India', 'Japan', 'Germany']

# Function calls
selected_countries_gdp(gdp_data, countries)
country_gdp(gdp_data, 'United States')
income_group(country_codes_data)
