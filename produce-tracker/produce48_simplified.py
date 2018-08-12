import requests
from bs4 import BeautifulSoup
import json

import numpy as np
import matplotlib.pyplot as plt

page = requests.get("https://en.wikipedia.org/wiki/Produce_48")
soup = BeautifulSoup(page.content, "html.parser")

data=[]
table = soup.find("table", class_="wikitable sortable")
table_body = table.find('tbody')

trainee_data = {}

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    for col in cols:
        col_text = col.text.rstrip('\n')

        if not col_text.isdigit():
            if not col_text in trainee_data.keys():
                trainee_data[col_text] = [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]


i = 0
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')

    j = -1
    for col in cols:
        col_text = col.text.rstrip('\n')

        # print(str(i) + " - " + str(j) + ":" , end="")
        if not col_text.isdigit():
            print(j)
            aux = trainee_data[col_text]
            aux[j] = i


        j += 1
    i += 1


print(trainee_data)

print(json.dumps(trainee_data, indent=3))



# Plotting
colors = [ "#071826", "#3B568C", "#ECA414", "#D91A1A", "#DB86A9", "#BBD9C8",
"#D93240", "#8C2B3D", "#2A3140", "#6B7363", "#286B47", "#F2727F", "#42253D",
"#D70B31", "#FFB482", "#FF96DC", "#C8FFFF", "#B4FFb4", "#FFFF64", "#DDDDDD",
"#F6D680", "#42674E", "#DF6045", "#3E7E8C", "#A3A64E", "#F2B591", "#D96B43",
"#F2B500", "#F59900", "#BAA43E", "#00524B", "#288189", "#263446", "#3D3D3B" ]


i=0
for girl in trainee_data.keys():
    clr = str(colors[i])
    num_scores = len(trainee_data[girl])
    scores = trainee_data.get(girl)

    x = np.arange(num_scores)

    plt.scatter(x,scores,c=clr)
    plt.plot(x,scores, c=clr, label=girl)

    if not scores[-1] == 0:
        plt.annotate(girl, xy=(x[-1],scores[-1]), xytext=(+33, +0), textcoords="offset points", color=clr)

    i += 1

plt.xlabel("Semanas")
plt.ylabel("Ranking")
plt.title("Grafica de tendencias del top 12 - Produce 48")
plt.ylim(12,1)
plt.grid(True)
plt.legend()

plt.show()
