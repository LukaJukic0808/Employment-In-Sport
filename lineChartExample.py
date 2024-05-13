import json
import matplotlib.pyplot as plt

with open('sport.json', 'r') as file:
    data = json.load(file)

years = list(data["AT"].keys())
years.remove("name")
percentages = [data["AT"][year]["youngPR"] for year in years]

plt.figure(figsize=(10, 6))

plt.plot(years, percentages)

plt.title('Percentage over Years in Austria, [15-29]')
plt.xlabel('Years')
plt.ylabel('Percentage(%)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()