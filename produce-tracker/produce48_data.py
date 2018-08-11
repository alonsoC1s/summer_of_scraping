from selenium import webdriver
from bs4 import BeautifulSoup
from googletrans import Translator
import json
import numpy as np
import matplotlib.pyplot as plt

url = "http://produce48.mnet.com/pc/rank/1"

# TODO: Download the images

# Translator instance
translator = Translator()

def extract_name(raw_name):
    translated_name = translator.translate(raw_name).text

    result = ''.join([i for i in translated_name if not i.isdigit() ])
    return result.strip()


def query_website():
    # Going headless
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # Starting driver and accessing page
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(url)

    # Getting the final html
    innerHTML = browser.execute_script("return document.body.innerHTML")

    browser.close()

    soup = BeautifulSoup(innerHTML, "html.parser")

    rank = soup.find_all(class_="name")

    # Getting all trainees and placing the in order
    trainees_all = []

    for grl in rank:
        trainees_all.append(extract_name(grl.text))

    return trainees_all

def create_data():
    trainees_all = query_website()
    # Creating dictionary from scratch
    data = {}
    data["trainees"] = []

    # Creating all data for the trainees along with current ranking
    i = 1
    for girl in trainees_all:
        data["trainees"].append({
            "name": girl,
            "ranking": [i]
        })
        i += 1

    print(data)

    # Storing dictionary in json format
    with open("trainee_data.txt", "w") as outfile:
        json.dump(data, outfile, indent=4)

    outfile.close()


def update_data():
    # Obtaining previously existing dict
    with open("trainee_data.txt", "r") as infile:
        data = json.load(infile)



with open("trainee_data.txt", "r") as datafile:
    my_data = json.load(datafile)

    datafile.close()

train_girls = my_data["trainees"]

x = np.arange(len(train_girls))

for i in x:
    specific_girl = train_girls[i]
    new_x = np.arange(len(specific_girl.get("ranking")))

    plt.scatter(new_x,specific_girl.get("ranking"))
    plt.plot(new_x,specific_girl.get("ranking"))
    #plt.annotate("hola", xy=(i,int(a_number)))

plt.show()
