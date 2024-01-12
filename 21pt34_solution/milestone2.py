import csv
import sympy as sp

def check_inside(x_axis_coordinate,y_axis_coordinate,circle_eq,wafer_radius):
    circle_eq=circle_eq.subs(x,x_axis_coordinate)
    circle_eq=circle_eq.subs(y,y_axis_coordinate)
    if circle_eq<=(wafer_radius)**2:
        return 1
    else:
        return 0

file=open("Workshop2024\\Milestone2\\Input\\Testcase1.txt")
lines=file.read().splitlines()
x,y=sp.symbols(('x','y'))
for words in lines:
    word=words.split(":")
    if word[0]=='WaferDiameter':
        wafer_diameter=int(word[1])
    if word[0]=='DieSize':
        size_list=(word[1].split('x'))
        for i in range(len(size_list)):
            size_list[i]=int(size_list[i])
    if word[0]=='DieShiftVector':
        shift_vector=eval(word[1])
    if word[0]=="ReferenceDie":
        reference_point=eval(word[1])

die_coordinates=[]
die_no=[]
die_starting_coordinate=(0+shift_vector[0],0+shift_vector[1])
list_output=dict()
circle_eq=((x-0)**2+(y-0)**2)
covered_y_positive=0
y_axis_no=0
y_axis_coordinate=die_starting_coordinate[1]
x_axis_coordinate=die_starting_coordinate[0]

while covered_y_positive<(wafer_diameter/2) :
    covered_x_positive=0
    x_axis_no=0
    x_axis_coordinate=die_starting_coordinate[0]
    while covered_x_positive<=(wafer_diameter/2) and check_inside(x_axis_coordinate,y_axis_coordinate,circle_eq,wafer_diameter/2):
        last_die_x=x_axis_coordinate
        last_die_y=y_axis_coordinate
        die_coordinates.append((last_die_x,last_die_y))
        die_no_x=x_axis_no
        die_no_y=y_axis_no
        die_no.append((die_no_x,die_no_y))
        list_output[(die_no_x,die_no_y)]=die_coordinates[-1]
        covered_x_positive+=size_list[0]
        x_axis_no+=1
        x_axis_coordinate+=size_list[0]

    covered_x_negative=0
    x_axis_no=-1
    x_axis_coordinate=die_starting_coordinate[0]-size_list[0]
    while covered_x_negative<=(wafer_diameter/2) and check_inside(x_axis_coordinate,y_axis_coordinate,circle_eq,wafer_diameter/2):
        last_die_x=x_axis_coordinate
        last_die_y=y_axis_coordinate
        die_coordinates.append((last_die_x,last_die_y))
        die_no_x=x_axis_no
        die_no_y=y_axis_no
        die_no.append((die_no_x,die_no_y))
        covered_x_negative+=size_list[0]
        list_output[(die_no_x,die_no_y)]=die_coordinates[-1]
        x_axis_no-=1
        x_axis_coordinate-=size_list[0]
    if -(x_axis_coordinate+(wafer_diameter/2))<size_list[0]:
        last_die_x=x_axis_coordinate
        last_die_y=y_axis_coordinate
        die_coordinates.append((last_die_x,last_die_y))
        die_no_x=x_axis_no
        die_no_y=y_axis_no
        die_no.append((die_no_x,die_no_y))
        list_output[(die_no_x,die_no_y)]=die_coordinates[-1]
    y_axis_no+=1
    covered_y_positive+=size_list[1]
    y_axis_coordinate+=size_list[1]
    x_axis_coordinate=die_starting_coordinate[0]
y_axis_no=-1
covered_y_negative=0
x_axis_coordinate=die_starting_coordinate[0]
y_axis_coordinate=die_starting_coordinate[1]-size_list[1]
while covered_y_negative<((wafer_diameter/2)):
    covered_x_positive=0
    x_axis_no=0
    x_axis_coordinate=die_starting_coordinate[0]
    while covered_x_positive<=(wafer_diameter/2) and check_inside(x_axis_coordinate,y_axis_coordinate,circle_eq,wafer_diameter/2):
        last_die_x=x_axis_coordinate
        last_die_y=y_axis_coordinate
        die_coordinates.append((last_die_x,last_die_y))
        die_no_x=x_axis_no
        die_no_y=y_axis_no
        die_no.append((die_no_x,die_no_y))
        covered_x_positive+=size_list[0]
        list_output[(die_no_x,die_no_y)]=die_coordinates[-1]
        x_axis_no+=1
        x_axis_coordinate+=size_list[0]
    covered_x_negative=0
    x_axis_no=-1
    x_axis_coordinate=die_starting_coordinate[0]-size_list[0]
    while covered_x_negative<=(wafer_diameter/2 )and check_inside(x_axis_coordinate,y_axis_coordinate,circle_eq,wafer_diameter/2):
        last_die_x=x_axis_coordinate
        last_die_y=y_axis_coordinate
        die_coordinates.append((last_die_x,last_die_y))
        die_no_x=x_axis_no
        die_no_y=y_axis_no
        die_no.append((die_no_x,die_no_y))
        covered_x_negative+=size_list[0]
        list_output[(die_no_x,die_no_y)]=die_coordinates[-1]
        x_axis_no-=1
        x_axis_coordinate-=size_list[0]
    if -(x_axis_coordinate+(wafer_diameter/2))<size_list[0]:
        print(x_axis_coordinate)
        last_die_x=x_axis_coordinate
        last_die_y=y_axis_coordinate
        die_coordinates.append((last_die_x,last_die_y))
        die_no_x=x_axis_no
        die_no_y=y_axis_no
        die_no.append((die_no_x,die_no_y))
        list_output[(die_no_x,die_no_y)]=die_coordinates[-1]
    y_axis_no-=1
    covered_y_negative+=size_list[1]
    y_axis_coordinate-=size_list[1]
    x_axis_coordinate=die_starting_coordinate[0]

print(die_coordinates)
print(die_no)
f = open('21pt34_solution\\milestone2testcase1.txt', "w")
for i in range(len(die_coordinates)):
    f.write(",".join([str(j) for j in die_no[i]]))
    f.write(":")
    f.write(",".join([str(j) for j in die_coordinates[i]]))
    f.write("\n")
f.close()
