def get_usar_senha() :
	'''
Essa função deve ler o arquivo advanced.txt e retornar 
'True' se a primeira linha do arquivo contiver 'True'
'False' se a primeira linha do arquivo contiver 'False'

# abra o arquivo "advanced.txt" para leitura
# dica: utilize a instrução with
	# dentro do bloco with leia UMA linha do arquivo
	# salve o conteúdo desta linha em uma variável
	# SE o valor da variável corresponder a 'False\n'
		# retorne False
	# SE o valor da variável corresponder a 'True\n'
		# retorne True
'''
	with open('advanced.txt', 'r') as arquivo:
			first_line = arquivo.readline()

			if first_line == 'True\n':
				return True
			
			elif first_line == 'False\n':
				return False
			
			else:
				return None 
def set_usar_senha(senha="") :
	'''
	Essa função deve escrever no arquivo advanced.txt
	'True\n' se a senha recebida como parametro não for vazia
	'False\n' se a senha recebida como parametro for vazia
	
	Exemplo de conteúdo do arquivo advanced.txt
	
	--------------------
	False
	      (vazio, estará em branco)
	--------------------
	ou
	--------------------
	True
	1234
	--------------------
	
	
# abra o arquivo "advanced.txt" para escrita
# dica: utilize a instrução with
	# SE o valor da variável senha for vazio
		# escreva "False\n"
		# escreva o conteúdo da variável senha
	# SE o valor da variável senha NÃO for vazio
		# escreva "True\n"
		# escreva o conteúdo da variável senha
'''
	with open('advanced.txt', 'w') as arquivo:
        
		if senha == "":
			arquivo.write('False\n')
			arquivo.write("")

		else:
			arquivo.write('True\n')
			arquivo.write('1234\n')   
