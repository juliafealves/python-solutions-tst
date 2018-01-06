# coding: utf-8
# Activity: Construction Budget
# Author: Júlia Fernandes Alves <juliafealves@gmail.com>

import math

price = float(raw_input("Digite o preço da unidade do tijolo (Em reais): "))
brick_height = float(raw_input("Digite a altura do tijolo (Em metros): "))
brick_width = float(raw_input("Digite o comprimento do tijolo (Em metros): "))
wall_height = float(raw_input("Digite a altura das paredes (Em metros): "))
wall_width = float(raw_input("Digite o comprimento das paredes (Em metros): "))

number_brick_height = wall_height / brick_height
number_brick_width = wall_width / brick_width

brick_total = number_brick_height * number_brick_width

price_brick_total = math.ceil(brick_total) * price

print "O número total de tijolos é %.1f e o orçamento final é de R$ %.1f" % (brick_total, price_brick_total)

