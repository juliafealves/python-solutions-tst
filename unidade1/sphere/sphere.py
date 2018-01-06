# coding: utf-8
# Activity: Sphere
# Author: Júlia Fernandes Alves <juliafealves@gmail.com>

# Description:
# Escreva um programa que recebe o raio de uma esfera e
# calcula e imprime com duas casas decimais o volume desta esfera.
#
# Input:
# O valor do raio é lido da entrada padrão.
#
# Output:
# Deve imprimir em ponto flutuante (2 casas decimais) o valor do volume da esfera.

# Example:
# 1
# 4.19

import math

radius = float(raw_input())
volume = (4.0 / 3.0) * math.pi * radius ** 3.0

print "%.2f" % volume
