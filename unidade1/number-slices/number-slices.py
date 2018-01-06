# coding: utf-8
# Activity: Number of Slices
# Author: Júlia Fernandes Alves <juliafealves@gmail.com>

# Description:
# Em uma festa foram compradas 32 fatias de pizza.
# Lê da entrada o número de convidados da festa e apresente duas
# formas de dividir as fatias para os convidados. Assuma que a
# festa tem pelo menos um convidado.
#
# Input:
# 10
#
# Output:
# Opção 1: 3 fatias cada, 2 de resto
# Opção 2: 3.20 fatias cada

slices = 32
guests = int(raw_input())

slices_guest_entire = slices / guests
over = slices % guests
slices_guest = slices / float(guests)

print "Opção 1: %i fatias cada, %i de resto" % (slices_guest_entire, over)
print "Opção 2: %.2f fatias cada" % slices_guest


