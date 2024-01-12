import numpy as np
import sympy as sp
from math import*
import csv

x1,y1,x2,y2=sp.symbols(('x1','y1','x2','y2'))

file=open("Workshop2024\\Milestone1\\Input\\Testcase1.txt","r")
details_wafer=dict()

lines=file.read().splitlines()
for words in lines:
    word=words.split(":")
    details_wafer[word[0]]=int(word[1])

interval=details_wafer["WaferDiameter"]/(details_wafer["NumberOfPoints"]-1)
slope_1=np.tan(details_wafer["Angle"])
print(slope_1)

start_x=0
start_y=0

constant_1=start_y-(slope_1*start_x)

eq1=sp.Eq(slope_1*x1+constant_1-y1,0)
eq2=sp.Eq((x1-start_x)**2+(y1-start_y)**2-(details_wafer["WaferDiameter"]//2)**2,0)
coordinates=sp.solve((eq1,eq2),(x1,y1))
diameter_x1=coordinates[0][0]
diameter_y1=coordinates[0][1]
diameter_x2=coordinates[1][0]
diameter_y2=coordinates[1][1]
list_points=[]
list_points.append(coordinates[0])
for i in range(details_wafer["NumberOfPoints"]-2):
    eq2=sp.Eq((x1-diameter_x1)**2+(y1-diameter_y1)**2-(interval)**2,0)
    eq2=sp.Eq((x1-diameter_x2)**2+(y1-diameter_y2)**2-(details_wafer["WaferDiameter"]-((i+1)*interval))**2,0)
    list_points.append(sp.solve((eq1,eq2),(x1,y1))[0])

print(coordinates)
list_points.append(coordinates[1])
print(list_points)
with open('21pt34_solution\\milestone1testcase1.txt','w',newline='') as file1:
    writer=csv.writer(file1)
    for points in list_points:
        writer.writerow(points)