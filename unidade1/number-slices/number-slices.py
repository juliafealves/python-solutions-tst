# coding: utf-8
# Activity: Number of Slices
# Author: Júlia Fernandes Alves <juliafealves@gmail.com>

slices = 32
guests = int(raw_input())

slices_guest_entire = slices / guests
over = slices % guests
slices_guest = slices / float(guests)

print "Opção 1: %i fatias cada, %i de resto" % (slices_guest_entire, over)
print "Opção 2: %.2f fatias cada" % slices_guest
