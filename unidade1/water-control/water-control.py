# coding: utf-8
# Activity: Water Control
# Author: Júlia Fernandes Alves <juliafealves@gmail.com>

import math

flow_velocity = float(raw_input())
pipe_diameter = float(raw_input())
time = int(raw_input())

section = (math.pi * pipe_diameter ** 2) / 4
flow = flow_velocity * section * 1000
amount_water = time * flow

print "Quantidade de água =", amount_water, "litros."
