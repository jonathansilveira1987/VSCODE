# Desenvolvido por Jonathan Silveira.
# Instagram: @jonathandev01

from speedtest import Speedtest

st = Speedtest()
st.get_servers()
best = st.get_best_server()
ping_result = st.results.ping

print('\n\033[32mSPEEDTEST 1\033[m')
print(f"\n\033[31mServidor encontrado --> {best['host']} localizado em {best['country']}.\033[m\n")
print('Sua velocidade de Download é de {:.2f} Mbit/s.'.format(st.download() / 1024 / 1024))
print('Sua velocidade de Upload é de {:.2f} Mbit/s.'.format(st.upload() / 1024 / 1024))
print('Seu PING atual é de {:.2f} ms.\n'.format(ping_result))




##########################################################################################################
# Desenvolvido por Filippo Carcano e aprimorado por Jonathan Silveira.
# https://www.youtube.com/watch?v=vtLLSYjiPtA
# Instagram: @filo_carca

print('\033[32mSPEEDTEST 2\033[m')

def test():
    s = Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res['download'], res['upload'], res['ping']

def main():
    for i in range(3):
        d, u, p = test()
        print('\nDownload: {:.2f} kb/s.'.format(d / 1024))
        print('Upload: {:.2f} kb/s.'.format(u / 1024))
        print('Ping: {} kb/s.\n'.format(p))
        break

if __name__ == "__main__":
    main()