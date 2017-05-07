#   ===================================================================================================================================================================================================================================
#   =================================================================================================   HSU POKER   ===================================================================================================================
#   ===================================================================================================================================================================================================================================


#   =====================================================   Imports   ============================================================

import time
import pickle

#   =====================================================   Funções   ============================================================

def salvar(arquivo,nome, dinheiro,xp):  # Função de salva o jogo
	if arquivo not in lista_arquivos:
		lista_arquivos.append(arquivo)
	saves=open("lista", "wb" )
	pickle.dump(lista_arquivos, saves)
	saves.close()
	dados= open(arquivo,'wb') 
	pickle.dump({"{}".format(arquivo) : [nome, dinheiro, xp ]}, dados)
	dados.close()
	time.sleep(0.5)
	print("Jogo salvo com sucesso!")

#   =====================================================   Listas   ==============================================================

sim=["sim", "s"]  # Lista para inputs afirmativos
nao=["nao","n","não"]  # Lista para inputs negativos
lista_arquivos=[]  # Lista de jogos salvos

#   =====================================================   Início   ==============================================================

print("Bem vindo ao Hsu Poker! ") # Começo do jogo

#   =============================================   Abertura de jogo salvo  =======================================================

while True:
	time.sleep(0.5)
	abrir_salvo=input("Deseja abrir um jogo salvo? \n")  # Verifica se o usário quer abrir um jogo salvo
	time.sleep(0.5)
	if abrir_salvo in sim: # Caso o usuário queira abri um jogo

		try:
			lista_arquivos=pickle.load(open("lista","rb"))  # Verifica a existência de jogos salvos

			if len(lista_arquivos)>0: # Mostra os arquivos salvos existentes
				print("Os saves disponíveis são:")
				time.sleep(0.5)

				for i in lista_arquivos:
					print("{}".format(i))
					time.sleep(0.5)

				arquivo=str(input("Qual save deseja carregar?\n"))  # Usuário escolhe um jogo pra abrir
				if arquivo in lista_arquivos:
					dado=pickle.load(open(arquivo,"rb"))  # Traz o jogo salvo com os dados guardados
					nome=dado["{}".format(arquivo)][0]
					dinheiro=dado["{}".format(arquivo)][1]
					xp=dado["{}".format(arquivo)][2]
					carregado=sim
					print("Carregando dados...")
					time.sleep(2)
					print("O nome do seu personagem é {}, você possui {} de dinheiro e {} de experiência" .format(nome,dinheiro,xp)) # Caracterização dos dados para o usuário
					break

				else:
					time.sleep(0.5)
					print("Este save não existe")
					continue
				


		except:
			print("Não existe nenhum jogo salvo")  # Aviso caso não exista jogo salvo
			time.sleep(0.5)
			carregado=nao
			break

	if abrir_salvo in nao:	# Caso o usuário não queira abrir o jogo salvo
		carregado=nao	
		break

	else:
		print("Digite um comando válido: sim ou não")
		continue

#   ==========================================   Caracterização do personagem  ===================================================

while True:
	if carregado==sim: # Checa se houve o carregamento de dados para pular o processo de caracterizar um personagem novo
			break
		
	if carregado==nao:  # Caso não tenha nenhum arquivo salvo aberto
		nome=input("Qual vai ser o nome do seu personagem?\n")
		dinheiro= 10000
		xp=0
		print("Você tem 10 mil fichas para iniciar sua trajetória") # Definições iniciais
		break

#   =============================================   Salvamento do progresso  ======================================================

while True:

	time.sleep(0.5)
	salvar_jogo=input("Deseja salvar o jogo? \n") # Pergunta se deseja salvar o jogo
	salvar_jogo=salvar_jogo.lower()

	if salvar_jogo in sim: # Caso o usuário queira salvar o jogo
		arquivo=input("Qual será o nome do arquivo salvo?\n")		
		salvar(arquivo,nome,dinheiro,xp)
		break

	if salvar_jogo in nao: # Caso não queira salvar o jogo
		break

	else:
		print("Digite um comando válido (Sim ou Não)")
		continue
	
#   ===================================================   Fim do jogo  =============================================================

time.sleep(0.5)
print("Até a próxima!") # Finalização do jogo