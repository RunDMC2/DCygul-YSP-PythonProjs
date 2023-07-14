import matplotlib.pyplot as pt
import pandas as pd

spamreader = pd.read_csv('world_pop.csv', index_col = 'Country Name')

world_pop = spamreader.loc['World'].values.tolist()
world_pop = world_pop[3:-1]

years = []
for i in range(1960, 2023):
    years.append(i)

pt.plot(years, world_pop)
pt.title("World Population From 1960-2022")
pt.xlabel("Year")
pt.ylabel("World Population (in billions)")

pt.show()

spamreader2 = pd.read_csv('Untitled spreadsheet - Sheet1.csv', index_col='Year')
avg_apple_price = spamreader2['Average Price'].tolist()

years2 = []
for i in range(1980, 2018):
    years2.append(i)

pt.plot(years2, avg_apple_price)
pt.title("Average Apple (Red Delicious) Price per Pound From 1980-2017")
pt.xlabel("Year")
pt.ylabel("Average Apple Price per Pound (in USD)")

pt.show()
