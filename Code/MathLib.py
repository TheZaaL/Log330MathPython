from math import sqrt

null_correlation_text = "Null to weak correlation"
weak_correlation_text = "Weak to medium correlation"
medium_correlation_text = "Medium to strong correlation"
strong_correlation_text = "Strong to very strong correlation"
perfect_correlation_text = "Very strong to perfect correlation"
error_correlation_text = "Invalid correlation"


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

def correlation_text(corr):
  if (corr < 0.2 and corr > -0.2):
    return null_correlation_text
  
  elif (corr < 0.4 and corr > -0.4):
    return weak_correlation_text
  
  elif (corr < 0.6 and corr > -0.6):
    return medium_correlation_text
  
  elif (corr < 0.8 and corr > -0.8):
    return strong_correlation_text
  
  elif (corr <= 1 and corr >= -1):
    return perfect_correlation_text
  
  else:
    return error_correlation_text

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

def regression_b0 (list_x, list_y, b1):
  if len(list_x) != len(list_y):
    raise TypeError("Lists are of different lenghts")

  regression_y = b1 * average(list_x)

  return average(list_y) - regression_y

def ecart_type_paire_donnes(list_x, list_y, b1, b0):
  n = len(list_x)
  sum_difference = 0

  for i in range(0, n):
    diff = list_y[i] - ((b1 * list_x[i]) + b0)
    sum_difference += diff * diff

  ecart_type = sqrt(sum_difference * (1 / (n - 1)))

  return ecart_type

def intervalle_confiance (list_x, xk, ecart_type):
  n = len(list_x)
  t = 1.860 # 90% confidance on 10 entries
  average_x = average(list_x)

  dividend = (xk - average_x) * (xk - average_x)

  divisor = 0
  
  for i in range(0, n):
    divisor += (list_x[i] - average_x) * (list_x[i] - average_x)
  
  root = sqrt(1 + (1/n) + (dividend / divisor))

  return t * ecart_type * root

def limite_superieure(yk, interval):
  return yk + interval

def limite_inferieure(yk, interval):
  return yk + interval
