import csv
import re
import time

print("Lendo lista de CNPJs.")
time.sleep(0.5)
# Definir lista de CNPJs a serem verificados
cnpj_list = ["00.000.000/0000-00","00.000.000/0000-00"]

# Ler arquivo CSV e armazenar informações em uma lista de dicionários
with open('lista.csv', 'r', newline='', encoding='iso-8859-1') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    headers = []
    data = []
    for row in csv_reader:
        if len(row) >= 3:  # Verificar se a linha tem pelo menos 3 campos
            protocolo = row[0].replace('"','')
            tipo = row[1].replace('"','')
            cnpj = row[2].replace('"','')
            data.append({"protocolo": protocolo, "tipo": tipo, "cnpj": cnpj})

print("Verificando protocolos repetidos.")
time.sleep(0.5)
# Verificar protocolos repetidos
protocolos_vistos = []
protocolos_repetidos = []
for d in data:
    if d['protocolo'] in protocolos_vistos:
        protocolos_repetidos.append(d['protocolo'])
    else:
        protocolos_vistos.append(d['protocolo'])

print("Verificando títulos para fins falimentares.")
time.sleep(0.5)
# Verificar protocolos com tipo "Falimentar"
falimentares = []
for d in data:
    if d['tipo'] == "Falimentar":
        falimentares.append(d['protocolo'])

print("Verificando CNPJ de títulos para retirar da lista.")
time.sleep(0.5)
# Verificar protocolos com CNPJ da lista definida anteriormente
cnpj_protocolos = []
for d in data:
    if d['cnpj'] in cnpj_list:
        cnpj_protocolos.append(d['protocolo'])

print("Gerando arquivo de resultados.")
time.sleep(0.5)
# Gerar arquivo de resultados
with open('resultados.txt', 'w') as f:
    if len(falimentares) > 0:
        f.write("Intimações do tipo 'Falimentar':\n")
        for p in falimentares:
            f.write(p + "\n")
        f.write("\n")
    else:
        f.write("Não foram encontrados protocolos com tipo 'Falimentar'.\n\n")

    if len(cnpj_protocolos) > 0:
        f.write("Intimações para retirar:\n")
        for p in cnpj_protocolos:
            f.write(p + "\n")
        f.write("\n")
    else:
        f.write("Não foram encontradas intimações para retirar.\n\n")

    if len(protocolos_repetidos) > 0:
        f.write("Intimações com mais de um devedor:\n")
        for p in protocolos_repetidos:
            match = re.search(r'\b\d{7}\b', p)
            if match:
                f.write(match.group() + "\n")
    else:
        f.write("Não foram encontrados títulos com mais de um devedor.\n")

time.sleep(0.5)
print("Arquivo de resultados gerado com sucesso.")
input("Pressione enter para sair")