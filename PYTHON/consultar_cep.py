import requests

def main():
	cep_input = input('\nDigite o CEP para a consulta: ')

	if len(cep_input) != 8:
		print('\n\033[0;31mQuantidade de dígitos inválida!\033[m\n')
		exit()

	request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

	address_data = request.json()

	if 'erro' not in address_data:
		print('\n\033[0;32mCEP ENCONTRADO\033[m\n')
		
		print('CEP: \033[0;33m{}\033[m\n'.format(address_data['cep']))
		print('Logradouro: \033[0;34m{}\033[m'.format(address_data['logradouro']))
		print('Complemento: \033[0;34m{}\033[m'.format(address_data['complemento']))
		print('Bairro: \033[0;34m{}\033[m'.format(address_data['bairro']))
		print('Cidade: \033[0;34m{}\033[m'.format(address_data['localidade']))
		print('Estado: \033[0;34m{}\033[m'.format(address_data['uf']))
		
	else:
		print('\033[0;31m{}: CEP inválido.\033[m'.format(cep_input))

	print('---------------------------------')
	option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n> '))
	if option == 1:
		main()
	else:
		print('Saindo...')

if __name__ == '__main__':
	main()
print()