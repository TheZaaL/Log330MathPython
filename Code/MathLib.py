from math import sqrt

def average(list):
  return (1 / len(list)) * sum(list)

def sum(list):
  output = 0

  for number in list:
    output += number

  return output

def sum_distance_squared(list):
  sum_distance = 0
  average_list = average(list)

  for number in list:
    sum_distance += (number - average_list) * (number - average_list)
  
  return sum_distance

def variance(list):
  return (1/(len(list) - 1)) * sum_distance_squared(list)

def ecartType(list):
  return sqrt(variance(list))
