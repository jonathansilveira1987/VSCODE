from time import sleep
# pip install psutil
import psutil
# Captura o sensor da bateria
battery = psutil.sensors_battery()
# Captura o percentual da bateria
percent = int(battery.percent)
if percent <= 20:
    # Mostra o resultado
    print(f'\n\033[0;31mAtenção! Seu computador está operando com {percent}% de bateria. Conecte o carregador!\033[m\n')
    sleep(5)
    print(f'\033[0;35mEm 15 segundos será ativado o desligamento automático de seu computador para preservação da bateria.\033[m\n')
    sleep(5)
    print(f'\033[0;36mCaso deseje cancelar o desligamento digite shutdown -a no Prompt de Comando e pressione ENTER.\033[m\n')
    sleep(15)
    import os
    os.system("shutdown /s /t 180")
else:
    # Mostra o resultado
    print(f'\n\033[0;32mNo momento seu computador está operando com {percent}% de bateria.\033[m\n')