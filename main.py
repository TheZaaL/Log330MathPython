from Code.IOLib import read_file
from Code.MathLib import average, ecartType, variance, correlation, correlation_text, regression_b1, regression_b0, ecart_type_paire_donnes, intervalle_confiance, limite_superieure, limite_inferieure

test_data = read_file("Data/tp6_data.csv")

list_x = test_data[0]
list_y = test_data[1]

xk = 900

b1 = regression_b1(list_x, list_y)
b0 = regression_b0(list_x, list_y, b1)

yk = (xk * b1) + b0

ecart_type = ecart_type_paire_donnes(list_x, list_y, b1, b0)

interval = intervalle_confiance(list_x, xk, ecart_type)

lim_sup = limite_superieure(yk, interval)
lim_inf = limite_inferieure(yk, interval)

print("b1: %.5f" % b1 )
print("b0: %.5f" % b0 )
print("yk: %.5f" % yk )
print("Écart-type: %.5f" % ecart_type )
print("Intervalle à 90: %.5f" % interval )
print("Limite supérieure: %.5f" % lim_sup )
print("Limite inférieure: %.5f" % lim_inf )
