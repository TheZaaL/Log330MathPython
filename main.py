from Code.IOLib import read_file
from Code.MathLib import average, ecartType, variance, correlation, correlation_text, regression_b1, regression_b0

test_data = read_file("Data/tp5_data.csv")

cor_semaine_1 = correlation(test_data[1], test_data[7])
cor_semaine_2 = correlation(test_data[2], test_data[7])
cor_semaine_3 = correlation(test_data[3], test_data[7])
cor_semaine_4 = correlation(test_data[4], test_data[7])
cor_semaine_5 = correlation(test_data[5], test_data[7])
cor_semaine_6 = correlation(test_data[6], test_data[7])

print("Week 1: this week has a " + correlation_text(cor_semaine_1) + " with a correlation of %.2f" % cor_semaine_1)
print("Week 2: this week has a " + correlation_text(cor_semaine_2) + " with a correlation of %.2f" % cor_semaine_2)
print("Week 3: this week has a " + correlation_text(cor_semaine_3) + " with a correlation of %.2f" % cor_semaine_3)
print("Week 4: this week has a " + correlation_text(cor_semaine_4) + " with a correlation of %.2f" % cor_semaine_4)
print("Week 5: this week has a " + correlation_text(cor_semaine_5) + " with a correlation of %.2f" % cor_semaine_5)
print("Week 6: this week has a " + correlation_text(cor_semaine_6) + " with a correlation of %.2f" % cor_semaine_6)