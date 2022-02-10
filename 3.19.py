#Johnny La
#PSID: 1875393

import math

height = float(input("Enter wall height (feet):\n"))
width = float(input("Enter wall width (feet):\n"))

area = height * width
needed = area / 350
print('Wall area: ' + str(int(round(area))) + ' square feet')

cans = int(round(needed))

print('Paint needed: %.2f gallons' % needed)
up = math.ceil(needed)
print("Cans needed: {} can(s)".format(up))

color = input("\nChoose a color to paint the wall:\n")
if color == "red":
    cost = 35 * cans
elif color == "blue":
    cost = 25 * cans
elif color == "green":
    cost = 23 * cans
else:
    cost = 0
print('Cost of purchasing ' + color + ' paint: $' + str(cost))