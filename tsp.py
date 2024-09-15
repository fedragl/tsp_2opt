import math
import pandas as pd
import numpy as np
import random

#read file
def read_file(file_name):
    # Open input file
    cities = [] #create array to store cities
    path=file_name
    file = open(path, 'r') #read file
    lines = file.readlines() #read lines
    for line in (lines[7:]): #loop over lines //side note: each .tsp has "EOF" at the end, use that as break point, currently i treat each file
        # Assumes the file format: <CityIndex> <X> <Y>
        city_index, x, y = map(float, line.strip().split()) #separate elements by blank space
        cities.append((city_index, x, y)) #creates a list with al the elements city, x, yex, x, y)) #creates a list with al the elements city, x, y
    return (cities)

#calcular distancia euclidiana
def distance_func(city_i,city_j): #city i is current city while city j is the next city
    x1=cities[city_i][1] #identify x1 coordinate
    x2=cities[city_j][1] #identify x2 coordinate
    y1=cities[city_i][2] #identify y1 coordinate
    y2=cities[city_j][2] #identify y2 coordinate
    d=math.sqrt(((x2-x1)**2)+((y2-y1)**2)) ##apply formula for the distance between two points
    return(d)

#calcular la distancia
def total_func(ruta):
    total=0
    for i in range(len(ruta) - 1):
        city_i=ruta[i]
        city_j=ruta[i+1]
        total += distance_func(city_i, city_j)
    return total

#búsqueda local
def local_search():
    run=0
    #vector cn aleatorio
    n=len(cities) #vertices
    ruta=list(range(n))
    random.shuffle(ruta) #crear primer ruta aleatoria
    mejor_ruta=ruta.copy()
    mejor_distancia=total_func(mejor_ruta)

    improved=True
    while improved:
        #hacer un cambio en la ruta random change maybe generate two random positions? and switch those 
        pos_1=random.randint(0, n-1)
        pos_2=random.randint(0, n-1)
        new_route=mejor_ruta.copy()
        flag=ruta[pos_1]
        new_route[pos_1]=ruta[pos_2]
        new_route[pos_2]=flag
        distancia=total_func(new_route)
        if(distancia<mejor_distancia):
            mejor_ruta=new_route.copy()
            mejor_distancia=distancia
        else:
            new_route=mejor_ruta.copy()
            improved=False
        run+=1
    
    return(mejor_ruta,mejor_distancia,run)


#matrixes declaration
#file_names= ('dj38.txt','lu980.txt','uy734.txt','zi929.txt','rw1621.txt') #data from: https://www.math.uwaterloo.ca/tsp/world/countries.html
#cities=[read_file(i) for i in file_names]
#print(local_search([cities[k] for k in range(len(cities))]))
file_names= ('lu980.txt')
cities=read_file(file_names)
print(local_search())


#distances = np.array([np.array([distance_func(i,j) for i in range(len(cities))]) for j in range(len(cities))])

