def validar_mes():
    """Valida e retorna o número do mês (1 a 12)"""
    while True:
        try:
            mes = int(input("Digite o número do mês (1-12): "))
            if 1 <= mes <= 12:
                return mes
            else:
                print("Erro: Digite um número entre 1 e 12.")
        except ValueError:
            print("Erro: Digite um número válido.")

def validar_temperatura(mes_extenso):
    """Valida e retorna a temperatura máxima do mês"""
    while True:
        try:
            temp = float(input(f"Temperatura máxima de {mes_extenso} (°C): "))
            if -60 <= temp <= 50:
                return temp
            else:
                print("Erro: Temperatura deve estar entre -60°C e +50°C.")
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

def obter_mes_por_extenso(numero_mes):
    """Retorna o nome do mês por extenso"""
    meses = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
        5: "maio", 6: "junho", 7: "julho", 8: "agosto",
        9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }
    return meses[numero_mes]

def obter_numero_mes_por_extenso(mes_extenso):
    """Retorna o número do mês a partir do nome por extenso"""
    meses = {
        "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4,
        "maio": 5, "junho": 6, "julho": 7, "agosto": 8,
        "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12
    }
    return meses[mes_extenso.lower()]

def main():
    # Dicionário para armazenar os dados
    dados_meteorologicos = {}
    
    print("=== DADOS METEOROLÓGICOS 2021 ===")
    print("Informe a temperatura máxima para cada mês:\n")
    
    # Coletar dados para os 12 meses
    meses_coletados = set()
    
    while len(meses_coletados) < 12:
        print(f"\nMês {len(meses_coletados) + 1} de 12")
        
        # Validar e obter o mês
        numero_mes = validar_mes()
        mes_extenso = obter_mes_por_extenso(numero_mes)
        
        # Verificar se o mês já foi informado
        if numero_mes in meses_coletados:
            print(f"Erro: Dados para {mes_extenso} já foram informados.")
            continue
        
        # Validar e obter a temperatura
        temperatura = validar_temperatura(mes_extenso)
        
        # Armazenar os dados
        dados_meteorologicos[numero_mes] = {
            "mes_extenso": mes_extenso,
            "temperatura": temperatura
        }
        
        meses_coletados.add(numero_mes)
        print(f"Dados de {mes_extenso} registrados com sucesso!")
    
    # Análise dos dados
    temperaturas = [dados["temperatura"] for dados in dados_meteorologicos.values()]
    
    # Cálculo da temperatura média
    temperatura_media = sum(temperaturas) / len(temperaturas)
    
    # Contagem de meses escaldantes (acima de 33°C)
    meses_escaldantes = sum(1 for temp in temperaturas if temp > 33)
    
    # Encontrar mês mais quente
    temp_maxima = max(temperaturas)
    mes_mais_quente_num = next(num for num, dados in dados_meteorologicos.items() 
                              if dados["temperatura"] == temp_maxima)
    mes_mais_quente = dados_meteorologicos[mes_mais_quente_num]["mes_extenso"]
    
    # Encontrar mês menos quente
    temp_minima = min(temperaturas)
    mes_menos_quente_num = next(num for num, dados in dados_meteorologicos.items() 
                               if dados["temperatura"] == temp_minima)
    mes_menos_quente = dados_meteorologicos[mes_menos_quente_num]["mes_extenso"]
    
    # Exibir resultados
    print("\n" + "="*50)
    print("ANÁLISE DOS DADOS METEOROLÓGICOS - 2021")
    print("="*50)
    
    print(f"\nTemperatura média das máximas: {temperatura_media:.1f}°C")
    print(f"Meses escaldantes (acima de 33°C): {meses_escaldantes}")
    print(f"Mês mais quente: {mes_mais_quente} ({temp_maxima}°C)")
    print(f"Mês menos quente: {mes_menos_quente} ({temp_minima}°C)")
    
    # Exibir tabela com todos os dados
    print("\nDADOS COMPLETOS:")
    print("-" * 30)
    print("Mês          | Temp. Máx (°C)")
    print("-" * 30)
    
    for num in range(1, 13):
        dados = dados_meteorologicos[num]
        print(f"{dados['mes_extenso']:12} | {dados['temperatura']:13.1f}")

if __name__ == "__main__":
    main()