import json

# caminho completo para o arquivo JSON
arquivo_faturamento = 'C:/Users/gorfa/estagio/Estagio/Exercicos/faturamento.json'

def ler_faturamento(arquivo_json):
    try:
        with open(arquivo_json, 'r') as file:
            dados = json.load(file)
            return dados['faturamento_mensal']
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return []
    except KeyError:
        print("Erro: Chave 'faturamento_mensal' não encontrada no arquivo JSON.")
        return []

def calcular_faturamento(faturamento):
    dias_validos = [dia for dia in faturamento if dia > 0]
    menor_faturamento = min(dias_validos) if dias_validos else 0
    maior_faturamento = max(dias_validos) if dias_validos else 0
    media_faturamento = sum(dias_validos) / len(dias_validos) if dias_validos else 0
    dias_acima_media = len([dia for dia in dias_validos if dia > media_faturamento])

    return menor_faturamento, maior_faturamento, dias_acima_media

faturamento_mensal = ler_faturamento(arquivo_faturamento)

if faturamento_mensal:  # Apenas calcula se a lista não estiver vazia
    menor, maior, dias_acima_media = calcular_faturamento(faturamento_mensal)

    print(f"Menor faturamento: R${menor:.2f}")
    print(f"Maior faturamento: R${maior:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")
