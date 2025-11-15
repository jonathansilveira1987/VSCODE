import os
shutdown = input("Deseja desligar o computador? (Sim / Não): ")
if shutdown == 'Não':
    exit()
else:
    os.system("shutdown /s /t 120")











'''


import os
shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")
if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 120")



'''