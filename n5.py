string = input('Digite uma palavra para inverter: ')

for i in range(len(string)-1, -1, -1):
    print(string[i], end='')