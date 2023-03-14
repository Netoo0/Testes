num = int(input("Digite um número: "))

fib = [0, 1]

while fib[-1] < num:
    fib.append(fib[-1] + fib[-2])

if num in fib:
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")

