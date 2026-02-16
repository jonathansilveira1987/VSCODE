# 6. Teste desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

import schedule
import time
import speedtest
from datetime import datetime
import pandas as pd
import numpy as np
from threading import Timer

# Função para gravar dados da velocidade da internet em csv
def internet ():
    def = pd.read_excel('dados.xlsx', sheet_name='base')
    s = speedtest.Speedtest()
    data_atual = datetime.now().strftime('%d/%m/%y')
    hora_atual = datetime.now().strftime('%h:%m')
    velocidade = s.download (threads=None)*(10**-6)
    df.loc[len(df)] = [data_atual, hora_atual, velocidade]
    df.to_excel('dados.xlsx', sheet_name='base', index=False)
    Timer(1800, internet).start()

internet()