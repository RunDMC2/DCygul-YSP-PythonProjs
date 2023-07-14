import matplotlib.pyplot as pt

spamreader = pd.read_csv('world_pop.csv', index_col = 'Country Name')

world_pop = spamreader.loc['World'].values.tolist()
world_pop = world_pop[3:-1]

print(world_pop)

years = []
for i in range(1960, 2023):
    years.append(i)
  
print(years)
print(len(world_pop))
print(len(years))

pt.plot(years, world_pop)
pt.title("World Population From 1960-2022")
pt.xlabel("Year")
pt.ylabel("World Population (in billions)")

pt.show()
