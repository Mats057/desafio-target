faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'OUTROS': 19849.53
}

soma = sum(faturamento.values())
print('Percentual de faturamento por estado:')
for estado, valor in faturamento.items():
    print(f"{estado}: {valor / soma:.2%}")