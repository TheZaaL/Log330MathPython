from math import sqrt

def average(list):
  return (1 / len(list)) * sum(list)

def sum(list):
  output = 0

  for number in list:
    output += number

  return output

def product(list_1, list_2):
  output = []

  for i in range(0, len(list_1)):
    output.append(list_1[i] * list_2[i])
  
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

def correlation(list_x, list_y):
  if len(list_x) != len(list_y):
    raise TypeError("Lists are of different lenghts")

  n = len(list_x)

  list_xx = product(list_x, list_x)
  list_xy = product(list_x, list_y)
  list_yy = product(list_y, list_y)

  sum_x = sum(list_x)
  sum_y = sum(list_y)

  dividend = ( n * sum(list_xy) ) - ( sum_x * sum_y )

  divisor = ( (n * sum(list_xx)) - (sum_x * sum_x) ) * ( (n * sum(list_yy)) - (sum_y * sum_y) )
  divisor = sqrt(divisor)

  return dividend / divisor

def regression_b1(list_x, list_y):
  if len(list_x) != len(list_y):
    raise TypeError("Lists are of different lenghts")

  n = len(list_x)
  
  average_x = average(list_x)
  average_y = average(list_y)

  list_xy = product(list_x, list_y)
  list_xx = product(list_x, list_x)

  dividend = sum(list_xy) - (n * average_x * average_y)

  divisor = sum(list_xx) - (n * average_x * average_x)

  return dividend / divisor

def regression_b0 (list_x, list_y) :
  regression_y = regression_b1(list_x, list_y) * average(list_x)

  return average(list_y) - regression_y
