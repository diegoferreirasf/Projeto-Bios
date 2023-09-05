def get_disp1() :
	'''
	Essa função deve ler o arquivo boot.txt e retornar o dispositivo 
	indicado na primeira linha, sem o caractere especial \n
	Exemplo de retorno 'SSD/HDD'
	
	# abra o arquivo "boot.txt" para leitura
	# dica: utilize a instrução with
		# dentro do bloco with leia UMA linha do arquivo
		# e substitua o caractere especial '\n' por vazio ''
		# esse conteúdo deve ser salvo em uma variável ex. disp1
	# fora da instrução with, retorne o conteúdo da variável 'disp1'
	'''
	with open('boot.txt', 'r') as arquivo:
		disp1 =  arquivo.readline().strip()

	return disp1

def get_disp2() :
	'''
	Essa função deve ler o arquivo boot.txt e retornar o dispositivo 
	indicado na segunda linha, sem o caractere especial \n
	Exemplo de retorno 'DVD-ROM'
	
	# abra o arquivo "boot.txt" para leitura
	# dica: utilize a instrução with
		# dentro do bloco with leia UMA linha do arquivo
		# essa linha será ignorada
		# leia a segunda linha do arquivo
		# e substitua o caractere especial '\n' por vazio ''
		# esse conteúdo deve ser salvo em uma variável ex. disp2
	# fora da instrução with, retorne o conteúdo da variável 'disp2'
	'''
	with open('boot.txt', 'r') as arquivo:
		arquivo.readline()
		disp2 = arquivo.readline().strip()

	return disp2


def get_disp3() :
	'''
	Essa função deve ler o arquivo boot.txt e retornar o dispositivo 
	indicado na terceira linha, sem o caractere especial \n
	Exemplo de retorno 'LAN'
	
	# abra o arquivo "boot.txt" para leitura
	# dica: utilize a instrução with
		# dentro do bloco with leia UMA linha do arquivo
		# essa linha será ignorada
		# leia a segunda linha do arquivo
		# essa linha será ignorada
		# leia a terceira linha do arquivo
		# e substitua o caractere especial '\n' por vazio ''
		# esse conteúdo deve ser salvo em uma variável ex. disp3
	# fora da instrução with, retorne o conteúdo da variável 'disp3'
	'''
	with open('boot.txt', 'r') as arquivo:
			arquivo.readline()
			arquivo.readline()
			disp3 = arquivo.readline().strip()
		
	return disp3

def save_boot(disp1, disp2, disp3) :
	'''
	Essa função deve abrir o arquivo boot.txt e criar a lista de 
	dispositivos de boot, um por linha
	Exemplo de conteúdo do arquivos após a execução

	SSD/HDD
	DVD-ROM
	LAN
	
	# abra o arquivo "boot.txt" para escrita
	# dica: utilize a instrução with
		# dentro do bloco with escreva uma linha com disp1 e \n
		# escreva uma linha com disp2 e \n
		# escreva uma linha com disp3 e \n
'''
	with open('boot.txt', 'w') as arquivo:

			arquivo.write(disp1,'\n')
			arquivo.write(disp2,'\n')
			arquivo.write(disp3,'\n') 