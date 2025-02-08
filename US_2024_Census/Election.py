import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import time
import random
import math

# US 2024 Populations Record
States = [
    'California','Texas','Florida','New York','Pennsylvania','Illinois','Ohio','Georgia','North Carolina','Michigan','New Jersey','Virginia','Washington','Arizona','Tennessee','Massachusetts','Indiana','Missouri','Maryland','Wisconsin','Colorado','Minnesota','South Carolina','Alabama','Louisiana','Kentucky','Oregon','Oklahoma','Connecticut','Utah','Iowa','Nevada','Arkansas','Kansas','Mississippi','New Mexico','Idaho','Nebraska','West Virginia','Hawaii','New Hampshire','Maine','Montana','Rhode Island','Delaware','South Dakota','North Dakota','Alaska','Vermont','Wyoming'
]

Populations = [
    38889770,30976754,22975931,19469232,12951275,12516863,11812173,11145304,10975017,10041241,9320865,8752297,7841283,7497004,7204002,7020058,6892124,6215144,6196525,5931367,5914181,5761530,5464155,5464155,4559475,4540745,4227337,4088377,3625646,3454232,3214315,3210931,3089060,2944376,2940452,2115266,1990456,1988698,1766107,1430877,1405105,1402106,1142746,1098082,1044321,928767,788940,733536,647818,586485
]

Electoral = [
    54,40,30,28,19,19,17,16,16,15,14,13,12,11,11,11,11,10,10,10,10,10,9,9,8,8,8,7,7,6,6,6,6,6,6,5,4,5,4,4,4,4,4,4,3,3,3,3,3,3
]

def sum(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    return sum

P = []
for i in range(len(Populations)):
    P.append(Populations[i]/1000000)

plt.plot(States, P, marker='o')
plt.plot(States, Electoral, marker='o')
plt.title('US Population 2024')
plt.xlabel('US State')
plt.ylabel('Population (Millions)')
plt.legend()
plt.grid(True)
plt.show()