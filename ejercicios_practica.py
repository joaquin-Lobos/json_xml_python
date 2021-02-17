#!/usr/bin/env python
'''
JSON XML [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.axes

def ej1():
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    json_data = {
                "nombre": "Joaquin",
                "apellido": "Lobos",
                "DNI": "12345678",
                "vestimentas": [
                    {
                        "prenda": "remeras",
                        "cantidad": 7
                    },
                    {
                        "prenda": "pantalones",
                        "cantidad": 5
                    },
                    {
                        "prenda": "zapatillas",
                        "cantidad": 4
                    },
                    {
                        "prenda": "camisas",
                        "cantidad": 3
                    }
                    ]
                }

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina
    with open('mi_json.json', 'w') as jsonfile:
        data = [json_data]
        json.dump(data, jsonfile, indent=4)

    # Observe el archivo y verifique que se almaceno lo deseado
    pass


def ej2():
    # JSON Deserialize
    # Basado en el ejercicio anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()
    with open('mi_json.json', 'r') as jsonfile:
        current_data = json.load(jsonfile)
    
    print(json.dumps(current_data, indent=4))
    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en el ej1
    pass


def ej3():
    # Ejercicio de XML
    # Basado en la estructura de datos del ejercicio 1,
    # crear a mano un archivo ".xml" y generar una estructura
    # lo más parecida al ejercicio 1.
    # El objectivo es que armen un archivo XML al menos
    # una vez para que entiendan como funciona.

    pass


def ej4():
    # XML Parser
    # Tomar el archivo realizado en el punto anterior
    # e iterar todas las tags del archivo e imprimirlas
    # en pantalla tal como se realizó en el ejemplo de clase.
    # El objectivo es que comprueben que el archivo se realizó
    # correctamente, si la momento de llamar al ElementTree
    # Python lanza algún error, es porque hay problemas en el archivo.
    # Preseten atención al número de fila y al mensaje de error
    # para entender que puede estar mal en el archivo.

    tree = ET.parse('info_personal.xml')
    root = tree.getroot()

    for child in root:
        print('tag:', child.tag, 'attr:', child.attrib, 'text:', child.text)
        for child2 in child:
            print('tag:', child2.tag, 'attr:', child2.attrib, 'text:', child2.text)

    pass


def ej5():
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    dataset = response.json()

    filter_data1 = [x.get("userId") for x in dataset if x.get("completed") is True]

    user_1 = len([x for x in filter_data1 if x == 1])
    user_2 = len([x for x in filter_data1 if x == 2])
    user_3 = len([x for x in filter_data1 if x == 3])
    user_4 = len([x for x in filter_data1 if x == 4])
    user_5 = len([x for x in filter_data1 if x == 5])
    user_6 = len([x for x in filter_data1 if x == 6])
    user_7 = len([x for x in filter_data1 if x == 7])
    user_8 = len([x for x in filter_data1 if x == 8])
    user_9 = len([x for x in filter_data1 if x == 9])
    user_10 = len([x for x in filter_data1 if x == 10])

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general.
    # Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    # De cada usuario en el total de las 200 entradas contar cuantos títulos
    # completó cada usuario (de los 10 posibles) y armar
    # un gráfico de torta resumiendo la información.

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de torta.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    completed = [user_1, user_2, user_3, user_4, user_5, user_6, user_7, user_8, user_9, user_10]

    labels = ['user 1', 'user 2', 'user 3', 'user 4', 'user 5', 'user 6', 'user 7', 'user 8', 'user 9', 'user 10']

    fig, ax = plt.subplots()
    fig.suptitle('Porcentaje aprobado por Alumno')

    ax.pie(completed, labels = labels, autopct='%1.1f%%', startangle=180)
    ax.axis('equal') 

    plt.show()



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
