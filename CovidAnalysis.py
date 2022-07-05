import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)

covid = pd.read_excel('Covid.xlsx')

# 1. Write a Python program to display first 5 rows from COVID-19 dataset. Also print the dataset information and check the missing values
# print('First 5 rows:')
# print(covid.head(5))
# print('\nDataset information:')
# print(covid.info())
# print("\nMissing data information:")
# print(covid.isna().sum())

# 2. Write a Python program to get the latest number of confirmed, deaths, recovered and active cases of Novel Coronavirus (COVID-19) Country wise.
# covid['Active'] = covid['Confirmed'] - covid['Deaths'] - covid['Recovered']
# result = covid.groupby('Country_Region')[['Confirmed', 'Deaths', 'Recovered', 'Active']].sum().reset_index()
# print(result)

# 3. Write a Python program to get the latest number of confirmed deaths and recovered people of Novel Coronavirus (COVID-19) cases Country/Region - Province/State wise.
# result = covid.groupby(['Country_Region', 'Province_State'])[['Deaths', 'Recovered']].sum()
# print(result)

# 4. Write a Python program to get the Chinese province wise cases of confirmed, deaths and recovered cases of Novel Coronavirus (COVID-19)
# data = covid[covid['Country_Region'] == 'China']
# data = data[['Province_State', 'Confirmed', 'Deaths', 'Recovered']]
# result = data.sort_values(by='Confirmed', ascending=False).reset_index(drop=True)
# print(result)

# 5. Write a Python program to get the latest country wise deaths cases of Novel Coronavirus (COVID-19).
# result = covid.groupby('Country_Region')['Deaths'].sum()
# print(result)

# 6. Write a Python program to list countries with no cases of Novel Coronavirus (COVID-19) recovered
# data = covid.groupby('Country_Region')['Recovered'].sum().reset_index()
# result = data[data['Recovered'] == 0][['Country_Region', 'Recovered']].reset_index(drop=True)
# print(result)

# 7. Write a Python program to list countries with all cases of Novel Coronavirus (COVID-19) died
# data = covid.groupby('Country_Region')[['Confirmed', 'Deaths']].sum()
# result = data[data['Confirmed'] == data['Deaths']].reset_index()
# print(result)

# 8. Write a Python program to list countries with all cases of Novel Coronavirus (COVID-19) recovered.
# data = covid.groupby('Country_Region')[['Confirmed', 'Recovered']].sum()
# result = data[data['Confirmed'] == data['Recovered']]
# result = result[result['Confirmed'] > 0].reset_index()
# print(result)

# 9. Write a Python program to get the top 10 countries data (Last Update, Country/Region, Confirmed, Deaths, Recovered) of Novel Coronavirus (COVID-19).
# result = covid.groupby('Country_Region')[['Confirmed', 'Recovered', 'Deaths']].sum().sort_values(by='Confirmed', ascending=False)[:10]
# print(result)

# 10. Write a Python program to create a plot (lines) of total deaths, confirmed, recovered and active cases Country wise where deaths greater than 150.
# covid['Active'] = covid['Confirmed'] - covid['Deaths'] - covid['Recovered']
# data = covid.groupby(["Country_Region"])[["Deaths", "Confirmed", "Recovered", "Active"]].sum().reset_index()
# data = data.sort_values(by='Deaths', ascending=False)
# data = data[data['Deaths'] > 50]
# plt.figure(figsize=(15, 5))
# plt.plot(data['Country_Region'], data['Deaths'], color='red')
# plt.plot(data['Country_Region'], data['Confirmed'], color='green')
# plt.plot(data['Country_Region'], data['Recovered'], color='blue')
# plt.plot(data['Country_Region'], data['Active'], color='black')
#
# plt.title('Total Deaths(>150), Confirmed, Recovered and Active Cases by Country')
# plt.show()
