from Code.IOLib import read_file
from Code.MathLib import average, ecartType, variance, correlation

test_data = read_file("Data/data_ecart_type.csv")

print('Moyenne : %.2f' % average(test_data[0]))

print('Variance : %.4f' % variance(test_data[0]))

print('Écart type : %.2f' % ecartType(test_data[0]))

test_data_correlation = read_file("Data/data_cor.csv")

cor = correlation(test_data_correlation[0], test_data_correlation[1])

print('Correlation : %.8f' % cor)
