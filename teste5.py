string = 'invertendo tudo'

inverter = ''
for i in range(len(string)-1, -1, -1):
    inverter += string[i]

print(inverter)
