import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

page = requests.get("https://weather.com/es-MX/tiempo/mensual/l/cda764f97030f6323bf8387c1bd40a83813d0e501df4ff3cff3b514b7407cfc6")
soup = BeautifulSoup(page.content, "html.parser")

## Temperatuas raw. Hi & low
all_temps = soup.find_all(class_="temp hi")
low_temps = soup.find_all(class_="temp low")

# Titulo de la localidad
locale_title = soup.find("span",class_="styles__locationName__2hkcY")

print(locale_title.text)

## <span classname="styles__locationName__2hkcY" class="styles__locationName__2hkcY">Gustavo A. Madero, Ciudad de México</span>
# Guardamos datos raw en formato string, eliminando el caracter ° para convertir a int
temp_data = []
temp_data_low = []

for tmp in all_temps:
    aux = tmp.text
    aux = aux[:-1]
    temp_data.append(aux)

for tmp in low_temps:
    aux = tmp.text
    aux = aux[:-1]
    temp_data_low.append(aux)


# Convertimos datos a int para graficar
raw_temps = []
raw_temps_low = []

for dat in temp_data:
    try:
        num = int(dat)
        raw_temps.append(num)
    except ValueError:
        pass


for dat in temp_data_low:
    num = 0
    try:
        num = int(dat)
        raw_temps_low.append(num)
    except ValueError :
        pass


## Actual plotting
size = len(raw_temps)
x = np.arange(size)

size_low = len(raw_temps_low)
x_low = np.arange(size_low)

# Colores aleatorios para marcadores
colors = np.random.rand(size)
colors_low = np.random.rand(size_low)

# Temp altas
plt.scatter(x,raw_temps, c=colors)
plt.plot(x,raw_temps,label="Maximas")

# Temps bajas
plt.scatter(x_low,raw_temps_low, c=colors_low)
plt.plot(x_low,raw_temps_low, label="Minimas",c="green")

# Ejes y titulos
plt.title("Temperaturas registradas en Metepec, Estado de México ")
plt.xlabel("Dia del mes")
plt.ylabel("Temparatura registrada")
plt.grid(True)

plt.legend()
plt.show()
