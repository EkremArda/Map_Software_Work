import matplotlib.pyplot as plt
import numpy as np
import csv
def csv_to_list_of_XY_coordinates(file_path):
  XY_list = []
  with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            x, y = float(row[0]), float(row[1])
            XY_list.append((x, y))
  print("XY_list= " + str(XY_list))
  xler = [x[0] for x in XY_list]
  yler = [y[1] for y in XY_list]
  print("The  graph of XY-Coordinates: ") 
  plt.plot(xler, yler) 
csv_to_list_of_XY_coordinates(str(input("please enter the file path of .csv file: "))) 
