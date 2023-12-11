# !/usr/bin/env python
# coding: utf-8

# import packages
# Note: You cannot import any other packages!
import numpy as np
import matplotlib.pyplot as plt
import csv
import math
import random



# Global attributes
# Do not change anything here except TODO 1 
StudentID = '108062135' # TODO 1 : Fill your student ID here
input_dataroot = 'input.csv' # Please name your input csv file as 'input.csv'
input_bonus1 = 'bonus_data1.csv'
input_bonus2 = 'bonus_data2.csv'
input_dataroot = ''
output_dataroot = '108062135' + '_basic_prediction.csv' # Output file will be named as '[StudentID]_basic_prediction.csv'

input_datalist =  [] # Initial datalist, saved as numpy array
output_datalist =  [] # Your prediction, should be 20 * 2 matrix and saved as numpy array
                      # The format of each row should be [Date, TSMC_Price_Prediction] 
                      # e.g. ['2021/10/15', 512]
bonus_datalist1 = []
bonus_datalist2 = []
# You can add your own global attributes here
training_dataX = []
training_dataY = []
testing_dataX = []
testing_dataY = []
date = []
# Read input csv to datalist
with open(input_dataroot, newline='') as csvfile:
  input_datalist = np.array(list(csv.reader(csvfile)))
with open(input_bonus1, newline='') as csvfile:
  bonus_datalist1 = np.array(csv.reader(csvfile))
with open(input_bonus1, newline='') as csvfile:
  bonus_datalist1 = np.array(csv.reader(csvfile))
# From TODO 2 to TODO 6, you can declare your own input parameters, local attributes and return parameters


def ProcessData():
#   tmp_datalist = np.delete(input_datalist, 0, axis = 0)
  global date
  global training_dataX 
  global training_dataY
  global testing_dataX
  global testing_dataY
  for x in input_datalist:
    tmp_date = x[0]
    tmp = np.append([], np.char.split(x[0], '/'))

    if(len(tmp[0][1])<2):
        tmp[0][1] = '0'+ tmp[0][1]
    if(len(tmp[0][2])<2):
        tmp[0][2] = '0'+ tmp[0][2] 
    x[0] = tmp[0][0] + tmp[0][1] + tmp[0][2] 
    if(int(x[0])>=20211015):
        date = np.append(date, tmp_date)
        testing_dataX = np.append(testing_dataX, x[1].replace(',',''))    
    else:
        training_dataX = np.append(training_dataX,x[1].replace(',',''))
        training_dataY = np.append(training_dataY,x[2].replace(',',''))
       
  testing_dataX = testing_dataX.astype(float)    
  training_dataX = training_dataX.astype(float)
  training_dataY = training_dataY.astype(float) 
  return()
 
def Regression(X,Y, learning_rate, iterations):
  alpha = learning_rate
  m = len(Y)
  cost_list = []
  theta = np.zeros(2)
  for i in range(iterations):
    hx = np.dot(X, theta)
    cost = (1/(2*m))*np.sum(np.square((hx-Y)))
    d_theta = (1/m)*np.dot(X.T, hx-Y)
    theta = theta - alpha*d_theta
    cost_list.append(cost)
  return theta, cost_list

def predictprice(theta):
  global testing_dataY
  global output_datalist
  global date
  for i in range(len(testing_dataX)):
    predict = theta[1]*testing_dataX[i]+theta[0]
    output_datalist = np.append(output_datalist, [date[i], predict])
    print(type(predict))
  print(type(date[3]))
  return 

# def valid(theta):
#   global testing_dataY
#   for data in valid_dataX:
#     predict = theta[1]*data+theta[0]
#     testing_dataY = np.append(testing_dataY, predict)
#   return

ProcessData()
ones = np.ones(len(training_dataX))
X = np.c_[ones, training_dataX]
theta, cost_list = Regression(X, training_dataY, 0.0000005, 100000)
predictprice(theta)
output_datalist = np.reshape(output_datalist,(-1,2))
#valid(theta)
# plt.scatter(valid_dataY,testing_dataY)
# Write prediction to output csv
with open(output_dataroot, 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date', 'TSMC Price'])
    for row in output_datalist:
        writer.writerow(row)


