import json
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.axes




def fetch():
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'
    response = requests.get(url)
    dataset = response.json()

    filter_data1 = [{"price":x["price"], "condition":x["condition"]} for x in dataset["results"] if x.get("currency_id") == "ARS"]
    return filter_data1

def transform(dataset, min, max):
    filter_min = [x for x in dataset if x.get("price") < min]
    filter_min_max = [x for x in dataset if x.get("price") > min and x.get("price") < max]
    filter_max = [x for x in dataset if x.get("price") > max]

    min_count = len(filter_min)
    min_max_count = len(filter_min_max)
    max_count = len(filter_max)

    return [min_count, min_max_count, max_count]

def report(data, min, max):
    fig, ax = plt.subplots()
    fig.suptitle('ALQUILERES POR RANGO DE PRECIO ESTABLECIDO')

    
    labels = ["Menores a ${} \nCantidad: {}".format(min, data[0]),
              "Entre ${} y ${} \nCantidad: {}".format(min, max, data[1]),
              "Mayores a ${} \nCantidad: {}".format(max, data[2])]
              
    
    ax.pie(data, labels = labels, autopct='%1.1f%%', shadow=True, startangle=180)
    ax.axis('equal') 

    plt.show()




if __name__ == "__main__":


    min = 5000
    max = 10000
    
    dataset = fetch()
    print(json.dumps(dataset, indent=4))
    data = transform(dataset, min, max)
    report(data, min, max)