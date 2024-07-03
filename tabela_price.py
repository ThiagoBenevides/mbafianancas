import csv

def calcular_pmt(valor_financiado, taxa_juros, num_prestacoes):
    """
    Calcula a prestação mensal usando a fórmula da Tabela Price.
    """
    pmt = (valor_financiado * taxa_juros) / (1 - (1 + taxa_juros) ** -num_prestacoes)
    return pmt

def calcular_juros(saldo_devedor, taxa_juros):
    """
    Calcula os juros de uma prestação.
    """
    return saldo_devedor * taxa_juros

def calcular_amortizacao(pmt, juros):
    """
    Calcula a amortização de uma prestação.
    """
    return pmt - juros

def calcular_saldo_devedor(saldo_devedor, amortizacao):
    """
    Calcula o novo saldo devedor após uma prestação.
    """
    return saldo_devedor - amortizacao

def gerar_tabela_price(valor_financiado, taxa_juros, num_prestacoes):
    """
    Gera a tabela completa do financiamento no formato da Tabela Price.
    """
    tabela = []
    saldo_devedor = valor_financiado
    pmt = calcular_pmt(valor_financiado, taxa_juros, num_prestacoes)

    for prestacao in range(1, num_prestacoes + 1):
        juros = calcular_juros(saldo_devedor, taxa_juros)
        amortizacao = calcular_amortizacao(pmt, juros)
        saldo_devedor = calcular_saldo_devedor(saldo_devedor, amortizacao)

        tabela.append({
            'Prestação': prestacao,
            'Valor da Prestação': round(pmt, 2),
            'Juros': round(juros, 2),
            'Amortização': round(amortizacao, 2),
            'Saldo Devedor': round(saldo_devedor, 2)
        })

    return tabela

def salvar_tabela_csv(tabela, nome_arquivo):
    """
    Salva a tabela de financiamento em um arquivo CSV.
    """
    with open(nome_arquivo, 'w', newline='') as csvfile:
        fieldnames = ['Prestação', 'Valor da Prestação', 'Juros', 'Amortização', 'Saldo Devedor']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for linha in tabela:
            writer.writerow(linha)

def main():
    # Entrada do usuário
    valor_financiado = float(input("Digite o valor do imóvel: "))
    taxa_juros = float(input("Digite a taxa de juros mensal (em %): ")) / 100
    num_prestacoes = int(input("Digite o número de prestações: "))

    # Gera a tabela Price
    tabela = gerar_tabela_price(valor_financiado, taxa_juros, num_prestacoes)

    # Salva a tabela em um arquivo CSV
    nome_arquivo = 'tabela_price.csv'
    salvar_tabela_csv(tabela, nome_arquivo)

    print(f'Tabela Price gerada e salva em {nome_arquivo}')

if __name__ == "__main__":
    main()
