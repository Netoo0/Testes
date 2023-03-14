import json


with open('dados.json', 'r') as f:
    dados = json.load(f)
dias_com_faturamento = [dia['valor'] for dia in dados if dia['valor'] != 0]
menor_valor = min(dias_com_faturamento)
maior_valor = max(dia['valor'] for dia in dados)
dias_com_faturamento = [dia['valor'] for dia in dados if dia['valor'] != 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
dias_acima_da_media = len([dia for dia in dados if dia['valor'] > media_mensal])

print('Menor valor de faturamento diário:', menor_valor)
print('Maior valor de faturamento diário:', maior_valor)
print('Número de dias com faturamento acima da média mensal:', dias_acima_da_media)
