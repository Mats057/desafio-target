fibo = 0
fibo1 = 1

fibonacci = [fibo, fibo1]

n = int(input("Digite um número: "))

for i in range(1, n):
    fibonacci.append(fibo + fibo1)
    fibo, fibo1 = fibo1, fibo + fibo1
    
for i in range(len(fibonacci)):
    if n == fibonacci[i]:
        print(f'{n} é um número de Fibonacci')
        break
    elif i == len(fibonacci)-1:
        print(f'{n} não é um número de Fibonacci')
        


