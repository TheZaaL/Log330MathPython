from Code.IOLib import read_file
from Code.MathLib import average, ecartType, variance, correlation, regression_b1, regression_b0

test_data = read_file("Data/data_ecart_type.csv")

print('Moyenne : %.2f' % average(test_data[0]))

print('Variance : %.4f' % variance(test_data[0]))

print('Écart type : %.2f' % ecartType(test_data[0]))

test_data_correlation = read_file("Data/data_cor.csv")

cor = correlation(test_data_correlation[0], test_data_correlation[1])

print('Correlation : %.8f' % cor)

test_data_regression = read_file("Data/data_regression.csv")

b1 = regression_b1(test_data_regression[0], test_data_regression[1])

print("Regression b1 : %.4f" % b1)

b0 = regression_b0(test_data_regression[0], test_data_regression[1], b1)

print("Regression b0 : %.4f" % b0)
