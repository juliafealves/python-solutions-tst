# coding: utf-8
# Activity: Grade in the Final
# Author: Júlia Fernandes Alves <juliafealves@gmail.com>

print "== Estágio 1 =="
weight1 = float(raw_input("Peso? "))
grade1 = float(raw_input("Nota? "))

print "== Estágio 2 =="
weight2 = float(raw_input("Peso? "))
grade2 = float(raw_input("Nota? "))

print "== Estágio 3 =="
weight3 = float(raw_input("Peso? "))
grade3 = float(raw_input("Nota? "))

partial_average = weight1 * grade1 + weight2 * grade2 + weight3 * grade3

average5 = (5.0 - partial_average * 0.6) / 0.4
average7 = (7.0 - partial_average * 0.6) / 0.4

print "== Resultados =="
print "Média parcial: %.1f" % partial_average
print "Nota na final, pra média 5.0 = %.1f" % average5
print "Nota na final, pra média 7.0 = %.1f" % average7