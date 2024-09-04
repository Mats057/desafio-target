import json
with open("dados.json") as f:
    data = json.load(f)

    
def maior(data):
    return max(data, key=lambda i: i['valor'])['valor']

def menor(data):
    return min(data, key=lambda i: i['valor'])['valor']

def media(data):
    soma = sum(i['valor'] for i in data if i['valor'] > 0)
    return soma / len(data)


print(f"O maior valor é {maior(data)}")
print(f"O menor valor é {menor(data)}")
print(f"A média dos valores sem os dias com faturamento zerado é {media(data)}")