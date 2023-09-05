'''
Neste arquivo são definidas 
'''
# imports
import os
import sys
import platform
import psutil

from datetime import date
from pynput import keyboard
from colored import fore, back, style

from advanced import get_usar_senha
from advanced import set_usar_senha

from boot import get_disp1
from boot import get_disp2
from boot import get_disp3
from boot import save_boot

# ====================================================
# variaveis globais (terão valores alterados)
# ====================================================
# elementos de tela
# indica qual o menu está sendo navegado
menu_ativo = 0 # 0 = Main, 1 = Advanced, 2 = Boot e 3 = Exit
# indica qual o menu foi ativado
enter      = 0 # 0 = Main, 1 = Advanced, 2 = Boot e 3 = Exit
# indica qual item na tela está sendo navegado
item_tela  = 0 # a indicação depende de qual tela está ativada

# dispositivos de boot
disp1 = get_disp1() # indica qual o primeiro dispositivo de boot
disp2 = get_disp2() # indica qual o segundo dispositivo de boot
disp3 = get_disp3() # indica qual o terceiro dispositivo de boot

# ====================================================
# constantes globais (não serão alteradas)
# ====================================================
# representam as cores que serão utilizadas ao longo do projeto
color: str = f"{fore('black')}{back('cyan')}"
color_ativo: str = f"{fore('red')}{back('black')}"
color_inativo: str = f"{fore('light_gray')}{back('blue')}"
color_selecionado: str = f"{fore('blue')}{back('light_gray')}"
color_editavel: str = f"{fore('white')}{back('black')}"
color_movendo: str = f"{fore('blue')}{back('black')}"	
color_tela: str = f"{fore('black')}{back('light_gray')}"

# ====================================================
# funcoes
# ====================================================
def limpar_tela() :
	'''
	Deve limpar a tela
	
	
	# utilize uma chamada a operação do sistema usando a biblioteca os
'''
	os.system('cls')

def end():
	'''
	Deve resetar o estilo padrao do terminal, se essa funcção não for 
	executada o terminal permanecerá colorido após finalizar a aplicação
	
	# imprima na tela uma string formatada para resetar as cores padrao
'''
	reset = "\033[0;0m"
	print({}.format(reset))

def atualizar() :
	'''
	A tela será redesenhada constantemente, essa função deve executar 
	um conjunto de ações
	
	# chame a função para limpar tela
	# chame a função para desenhar a tela
	# chame a função end para resetar as cores
'''
	limpar_tela()

	end()

def titulo() :
	'''
	Exibe uma barra de titulo incial
	'''
	# crie uma string de 80 colunas, "Projeto BIOS" deve ser centralizado
	# impria a string utilizando a cor 'color'


def menu() :
	'''
	Exibe uma barra de menu
	'''
	pass
	# imprima 80 espaços usando a cor 'color_inativo'
	# chame a funcao que cria o menu 'main'
	# chame a funcao que cria o menu 'advanced'
	# chame a funcao que cria o menu 'boot'
	# chame a funcao que cria o menu 'exit'


def main_menu() :
	'''
	Exibe o menu main selecionado ou inativo
	'''
	pass
	# crie uma string de 12 colunas, "Main" deve ser centralizado
	# posicione o cursor na linha 2 coluna 2
	# SE 'menu_ativo' está na posição 0
		# imprima a string criada com a cor 'color_selecionado'
	# SE 'menu_ativo' não está na posição 0
		# imprima a string criada com a cor 'color_inativo'


def advanced_menu() :
	'''
	Exibe o menu advanced selecionado ou inativo
	'''
	pass
	# crie uma string de 12 colunas, "Advanced" deve ser centralizado
	# posicione o cursor na linha 2 coluna 12
	# SE 'menu_ativo' está na posição 1
		# imprima a string criada com a cor 'color_selecionado'
	# SE 'menu_ativo' não está na posição 1
		# imprima a string criada com a cor 'color_inativo'


def boot_menu():
	'''
	Exibe o menu boot selecionado ou inativo
	'''
	pass
	# crie uma string de 12 colunas, "Boot" deve ser centralizado
	# posicione o cursor na linha 2 coluna 22
	# SE 'menu_ativo' está na posição 2
		# imprima a string criada com a cor 'color_selecionado'
	# SE 'menu_ativo' não está na posição 2
		# imprima a string criada com a cor 'color_inativo'


def exit_menu() :
	'''
	Exibe o menu exit selecionado ou inativo
	'''
	pass
	# crie uma string de 12 colunas, "Exit" deve ser centralizado
	# posicione o cursor na linha 2 coluna 32
	# SE 'menu_ativo' está na posição 3
		# imprima a string criada com a cor 'color_selecionado'
	# SE 'menu_ativo' não está na posição 3
		# imprima a string criada com a cor 'color_inativo'


def rodape() :
	'''
	Exibe o conteúdo do rodape, exibindo a lista de comandos
	'''
	pass
	# posicione o cursor na linha 22 coluna 0
	# imprima as opções 
	# Enter: Selecionar menu
	# \u2191\u2193 (setas): Navegar valores
	# \u2190\u2192 (setas): Navegar menus
	# + -: Alterar valores
	# q: Sair
	# Observe que será necessario completar a quantidade de colunas
	# imprimindo espaços em branco


def tela() :
	'''
	Desenha a tela realizando uma chamada para todas as outras funcoes
	'''
	pass
	# declare o uso da variavel global 'menu_ativo'
	
	# chame a funcao que imprime o titulo
	# chame a funcao que imprime os menus
	# por hora não implemente as funcoes de tela
	# chame a funcao que imprime o rodape

#########################################################
# Vamos testar
# No final do arquivo crie o programa principal com as 
# seguintes chamadas
#
# # main
# limpar_tela()
# tela()
# end()
#
# Se tudo esta certo você verá a tela sendo desenhada 
# apenas com os menus e sem navegação pelas setas
#########################################################

#########################################################
# Continuando
#
# Substitua na função 'tela' a linha
# 'por hora não implemente as funcoes de tela'
# pelas linhas a seguir
# 
# # SE 'menu_ativo' tem valor 0
# 	# chame a funcao main_tela
# # SE 'menu_ativo' tem valor 1
# 	# chame a funcao advanced_tela
# # SE 'menu_ativo' tem valor 2
# 	# chame a funcao boot_tela
# # SE 'menu_ativo' tem valor 3
# 	# chame a funcao mexit_tela
#########################################################

def main_tela() :
	'''
	Exibe o conteúdo da tela main, quando selecionada
	'''
	pass
	# imprima 20 vezes uma linha, com 80 espaços em branco
	# usando  a cor 'color_tela'
	
	# posicione o cursor na linha 5 coluna 5
	# capture a data atual
	# formate a data no padrão dd/mm/aaa
	# imprima a data com a cor 'color_tela'
	
	# posicione o cursor na linha 8 coluna 0
	# imprima as informações sobre o computador com a cor 'color_tela'
	# calcule o total de memoria em GB
	# imprima a informação sobre a memoria com a cor 'color_tela'


def advanced_tela() :
	'''
	Exibe o conteúdo da tela advanced, quando selecionada
	Obs.: O valor da senha não é verdadeiramente editável, está com
	um valor padrão 1234
	'''
	pass
	# salve em uma variável se a senha está sendo utilizada 
	# observe a função de advanced.py
	
	# imprima 20 vezes uma linha, com 80 espaços em branco
	# usando  a cor 'color_tela'
	
	# posicione o cursor na linha 8 coluna 0
	# SE o menu ativado NÃO for 1 (observe as variáveis globais)
		# SE senha NÃO está sendo utilizada 
			# imprima com cor 'color_tela' Usar senha: e com a cor 'color_ativo' Off
			# imprima com cor 'color_tela' Senha: e com a cor 'color_editavel' 4 espaços em branco
		# SE senha está sendo utilizada 
			# imprima com cor 'color_tela' Usar senha: e com a cor 'color_ativo' On
			# imprima com cor 'color_tela' Senha: e com a cor 'color_editavel' 4 espaços em branco
	# SE o menu ativado for 1 (observe as variáveis globais)
		# SE item na tela que está sendo navegado é o 0 (On ou Off)
			# SE senha NÃO está sendo utilizada
				# imprima com cor 'color_tela' Usar senha: e com a cor 'color_ativo' Off 
				# imprima com cor 'color_tela' Senha: e com a cor 'color_editavel' 4 espaços em branco
			# SE senha está sendo utilizada
				# imprima com cor 'color_tela' Usar senha: e com a cor 'color_ativo' On 
				# imprima com cor 'color_tela' Senha: e com a cor 'color_editavel' 1234
		# SE item na tela que está sendo navegado é o 1 (Senha)
			# SE senha NÃO está sendo utilizada
				# imprima com cor 'color_tela' Usar senha: e com a cor 'color_ativo' Off 
				# imprima com cor 'color_tela' Senha: e com a cor 'color_movendo' 4 espaços em branco
			# SE senha está sendo utilizada
				# imprima com cor 'color_tela' Usar senha: e com a cor 'color_ativo' On 
				# imprima com cor 'color_tela' Senha: e com a cor 'color_movendo' 1234


def boot_tela() :
	'''
	Exibe o conteúdo da tela boot, quando selecionada
	'''
	pass
	# declare o uso da variavel global 'disp1'
	# declare o uso da variavel global 'disp2'
	# declare o uso da variavel global 'disp3'
	
	# imprima 20 vezes uma linha, com 80 espaços em branco
	# usando  a cor 'color_tela'
	
	# posicione o cursor na linha 8 coluna 0
	# SE o menu ativado NÃO for 2 (observe as variáveis globais) 
		# imprima na cor 'color_tela' 1º dispositivo de boot: e na cor 'color_editavel' o valro da variável disp1
		# imprima na cor 'color_tela' 2º dispositivo de boot: e na cor 'color_editavel' o valro da variável disp2
		# imprima na cor 'color_tela' 3º dispositivo de boot: e na cor 'color_editavel' o valro da variável disp3
	# SE o menu ativado for 2 (observe as variáveis globais)
		# SE item na tela que está sendo navegado é o 0 (1º disp)
			# imprima na cor 'color_tela' 1º dispositivo de boot: e na cor 'color_movendo' o valor da variável disp1 
		# SE item na tela que está sendo navegado NÃO é o 0 (1º disp)
			# imprima na cor 'color_tela' 1º dispositivo de boot: e na cor 'color_editavel' o valor da variável disp1

		# SE item na tela que está sendo navegado é o 1 (2º disp)
			# imprima na cor 'color_tela' 2º dispositivo de boot: e na cor 'color_movendo' o valor da variável disp2 
		# SE item na tela que está sendo navegado NÃO é o 1 (2º disp)
			# imprima na cor 'color_tela' 2º dispositivo de boot: e na cor 'color_editavel' o valor da variável disp2

		# SE item na tela que está sendo navegado é o 2 (3º disp)
			# imprima na cor 'color_tela' 3º dispositivo de boot: e na cor 'color_movendo' o valor da variável disp3 
		# SE item na tela que está sendo navegado NÃO é o 2 (3º disp)
			# imprima na cor 'color_tela' 2º dispositivo de boot: e na cor 'color_editavel' o valor da variável disp3


def mexit_tela() :
	'''
	Exibe o conteúdo da tela mexit_tela, quando selecionada
	'''	
	pass
	# imprima 20 vezes uma linha, com 80 espaços em branco
	# usando  a cor 'color_tela'
	
	# posicione o cursor na linha 8 coluna 0
	# imprima a descrição 'Pressione ENTER para sair!' usando a cor 'color_tela'


# ====================================================
# eventos	
# ====================================================
def on_press(key):
	'''
	Trata todos os eventos de teclado no programa
	'''
	# declare o uso da variavel global 'menu_ativo'
	# declare o uso da variavel global 'enter'
	# declare o uso da variavel global 'item_tela'

	# declare o uso da variavel global 'disp1'
	# declare o uso da variavel global 'disp2'
	# declare o uso da variavel global 'disp3'
	
	try:
		'''
		Quando o caractere q é presionado, sai do programa
		'''
		if (key.char == 'q' or key.char == 'Q') :
			exit()
		# SE o caractere pressionado é '+'
			# SE a tela ativa é advanced
				# chame a função que seta o uso da senha, passando 1234 como parametro
			# SE a tela ativa é boot
				# SE item na tela que está sendo navegado é 0
					# realize troca dos conteúdos das variáveis disp1 e disp2
				# SE item na tela que está sendo navegado é 1
					# realize troca dos conteúdos das variáveis disp2 e disp3			
				# SE item na tela que está sendo navegado é 2
					# realize troca dos conteúdos das variáveis disp3 e disp1	
				# chame a função que salva a ordem de boot passando disp1, disp2 e disp3 como parametros (observe boot.py)
		# SE o caractere pressionado é '-'
			# SE a tela ativa é advanced
				# chame a função que seta o uso da senha, com o parametro vazio
			# SE a tela ativa é boot
				# SE item na tela que está sendo navegado é 0
					# realize troca dos conteúdos das variáveis disp1 e disp3
				# SE item na tela que está sendo navegado é 1
					# realize troca dos conteúdos das variáveis disp2 e disp1	
				# SE item na tela que está sendo navegado é 2
					# realize troca dos conteúdos das variáveis disp3 e disp2		
				# chame a função que salva a ordem de boot passando disp1, disp2 e disp3 como parametros (observe boot.py)
		else :
			pass
	except AttributeError:
		# para indicar quantos itens são editáveis em cada tela
		###########################################
		# não precisa alterar as linhas a seguir
		mod = 1
		if (enter == 0) :
			mod = 1	
		elif (enter == 1) :
			mod = 2
		elif (enter == 2) :
			mod = 3	
		# não precisa alterar as linhas anteriores
		###########################################
		
		if (key == keyboard.Key.up) : # seta para cima
			# atualize o item da tela para o anterior
			# ex. item na tela é 1 (um), deve ser atualizado para 0
			# ex. item na tela é 2 (dois), deve ser atualizado para 1
			# Cuiado! só existem 'mod' (variável anterior) itens em cada tela. Valor deve circular, como em um relógio
		elif (key == keyboard.Key.down) : # seta para baixo
			# atualize o item da tela para o anterior
			# ex. item na tela é 0 (zero), deve ser atualizado para 1
			# ex. item na tela é 1 (um), deve ser atualizado para 2
			# Cuiado! só existem 'mod' (variável anterior) itens em cada tela. Valor deve circular, como em um relógio
			# Esse calculo pode ser realizado em UMA linha
		elif (key == keyboard.Key.left) : # seta esquerda
			# atualize o menu ativo para o anterior
			# ex. menu é 0 (zero), deve ser atualizado para 4
			# ex. menu é 1 (um), deve ser atualizado para 0
			# Cuiado! só existem 4 menus. Valor deve circular, como em um relógio
			# Esse calculo pode ser realizado em UMA linha
		elif (key == keyboard.Key.right) : # seta direita
			# atualize o menu ativo para o proximo
			# ex. menu é 0 (zero), deve ser atualizado para 1
			# ex. menu é 1 (um), deve ser atualizado para 2
			# Cuiado! só existem 4 menus. Valor deve circular, como em um relógio
			# Esse calculo pode ser realizado em UMA linha
		elif (menu_ativo == 3) and (key == keyboard.Key.enter) :
			exit()
		elif (key == keyboard.Key.enter) : # enter
			enter     = menu_ativo
			item_tela = 0

			if (menu_ativo == 2) :
				save_boot(disp1, disp2, disp3)
			
	# chame a funcao para atualizar a tela

def on_release(key):
	'''
	Finaliza o programa ao pressionar ESC
	Obs.: Não é necesário modificar
	'''
	if key == keyboard.Key.esc:
		return False


# main
####################################################
# Chegou aqui, retire os comentários e execute
####################################################
'''
try:
	limpar_tela()
	tela()
	end()

	# Collect events until released
	with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()

except :
	limpar_tela()
	print("BIOS finalizada!")
'''
