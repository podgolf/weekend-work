
basecapturerate = 0.33
cpmultiplier = 0.75
ball, curve, berry, throw, medal = 1, 1, 1, 1, 1
baserate = (1 - (basecapturerate / (2 * cpmultiplier)))
multipliers = ball * curve * berry * throw * medal
probability = 1 - baserate ** multipliers
print(round(probability, 2))

x = 5
print(x >= 2)
