import platform
import wmi # Usando o módulo WMI (apenas para Windows) pode ser instalado usando o comando: pip install wmi
import psutil # pip install psutil
import platform, socket, psutil
from tkinter import *

my_system = platform.uname()
texto = ' Informações do Sistema '
print(f'\n\033[0;31m{texto:.^80}\033[m\n')
print(f"Nome do Computador: \033[0;32m{my_system.node}\033[m")
print(f"Sistema Operacional: \033[0;32m{my_system.system} {my_system.release}\033[m")
print(f"Versão: \033[0;32m{my_system.version}\033[m")
print(f"Arquitetura do Processador: \033[0;32m{my_system.machine}\033[m")
print(f"Processador: \033[0;32m{my_system.processor}\033[m")
c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]
print(f"Fabricante da Placa Mãe: \033[0;32m{my_system.Manufacturer}\033[m")
print(f"Modelo da Placa Mãe: \033[0;32m{my_system. Model}\033[m")
print(f"Nome do Computador: \033[0;32m{my_system.Name}\033[m")
print(f"Quantidade de Processadores: \033[0;32m{my_system.NumberOfProcessors}\033[m")
print(f"Tipo de Sistema: \033[0;32m{my_system.SystemType}\033[m")
print(f"Família do Equipamento: \033[0;32m{my_system.SystemFamily}\033[m")
print(f"Memória: \033[0;32m{psutil.virtual_memory()}\033[m")
info = {}
info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 **3)))
print(f'RAM: \033[0;32m{info}\033[m')

texto = ' Informações do Sistema '
print(f'\n\033[0;31m{texto:.^80}\033[m\n')
c = wmi.WMI()    
my_system = c.Win32_ComputerSystem()[0]
print(f'Nome do Computador: \033[0;33m{platform.node()}\033[m')
print(f'Sistema Operacional: \033[0;33m{platform.system()}\033[m')
print(f'Lançamento: \033[0;33m{platform.release()}\033[m')
print(f'Versão: \033[0;33m{platform.version()}\033[m')
print(f'Distribuição do Sistema: \033[0;33m{platform.platform()}\033[m')
print(f"Arquitetura do Sistema: \033[0;33m{my_system.SystemType}\033[m")
print(f'Processador: \033[0;33m{platform.processor()}\033[m')
print(f'Arquitetura do Processador: \033[0;33m{platform.machine()}\033[m')
print(f"Número de Processadores: \033[0;33m{my_system.NumberOfProcessors}\033[m")
print(f"Quantidade de Núcleos do Processador: \033[0;33m{psutil.cpu_count()}\033[m")
print(f"Memória: \033[0;33m{psutil.virtual_memory()}\033[m")
print(f"Fabricante da Placa Mãe: \033[0;33m{my_system.Manufacturer}\033[m")
print(f"Modelo da Placa Mãe: \033[0;33m{my_system. Model}\033[m")
print(f"Família do Equipamento: \033[0;33m{my_system.SystemFamily}\033[m\n")

'''

f = open("systeminfo.txt","w")
f.write(str(my_system))

import wmi # Usando o módulo WMI (apenas para Windows) pode ser instalado usando o comando: pip install wmi
c = wmi.WMI()    
my_system = c.Win32_ComputerSystem()[0]
f = open("systeminfo.txt","w")
f.write(str(my_system))
print('Salvo em ' + str(my_system))

import os
print('\033[0;32m')
for line in os.popen('systeminfo'): print(line.rstrip())
print('\033[m')

'''