import requests
from bs4 import BeautifulSoup

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
                trainee_data[col_text] = []


i = 0
for row in rows:
    cols = row.find_all('td')
    reps = []

    for col in cols:
        col_text = col.text.rstrip('\n')
        print(col_text)
        if not col_text.isdigit():
            reps.append(col_text)
            print("Agregando a reps: " + col_text)
            trainee_data.get(col_text).append(i)

    print("Lista de reps" + str(reps))
    print("Lista completa" + str(trainee_data.keys()))
    prospects = list(set(reps) - set(trainee_data.keys()))
    print(prospects)
    for item in prospects:
        trainee_data.get(item).append(0)


print(trainee_data)



# Plotting
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']


i=0
for girl in trainee_data.keys():
    clr = str(colors[i])
    num_scores = len(trainee_data[girl])
    scores = list(reversed(trainee_data.get(girl)))

    x = np.arange(num_scores)
    plt.scatter(x,scores,c=clr)
    plt.plot(x,scores, c=clr)

    i += 1

# plt.ylim(12,)
#plt.show()
