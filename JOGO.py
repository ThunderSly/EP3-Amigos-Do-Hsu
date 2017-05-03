import time
import pickle
import random

def save(arquivo):
	dados= open(arquivo,'wb') 
	pickle.dump({"dados": [nome,dinheiro,xp]}, dados)
	dados.close()


def load(arquivo):
	dado=pickle.load(open(arquivo,"rb"))
	return dado


xp=1
new=["new", "n", "new game"]
load=["load","l","load game"]

print("Bem vindo ao Hsu Poker ")


while True:

	inicio=input("New Game(N) ou Load Game(L)? \n ").lower()  #Verifica se o usário quer abrir um jogo salvo
	time.sleep(0.5)
	
	if inicio in load:
					
		try:
			lista_saves=pickle.load(open("lista","rb"))
			if len(lista_saves)>0:
				print("Os saves disponíveis são: {}".format(lista_saves))
				time.sleep(1)
				file=str(input("Qual save deseja carregar? "))
				dado=load(file)  # Traz o jogo salvo com os dados guardados
				nome=dado["dados"][0]
				dinheiro=dado["dados"][1]
				xp=dado["dados"][2]
				print("Carregando dados...")
				time.sleep(2)
				print("Sucesso!")
				break
		except:
			print("Não há saves ainda!")

	if inicio in new:	# Caso o usuário não queira abrir o jogo salvo
		nome=str(input("Qual vai ser o nome do seu personagem?\n"))
		dinheiro= 10000
		print(" Você tem 10 mil fichas para iniciar sua trajetória")
		break
		
lista_saves=[]
while True:
	
	acao=input("Jogar(J), Salvar(S), Load(L) ou Quitar(Q)")
	lista_saves=pickle.load(open("lista","rb"))	
	
	if acao == "s" or acao == "salvar": # Caso o usuário queira salvar o jogo
		print("Os saves disponíveis são: {}".format(lista_saves))
		arquivo=str(input("Deseja salvar com que nome? "))
		lista_saves.append(arquivo)
		save(arquivo)
		saves=open("lista", "wb" )
		pickle.dump(lista_saves, saves)
		saves.close()
		print("Salvando....")
		time.sleep(2)
		print("Sucesso!")
		time.sleep(0.5)
	
	if acao == "load" or acao == "l":
		try:
			lista_saves=pickle.load(open("lista","rb"))
			if len(lista_saves)>0:
				print("Os saves disponíveis são: {}".format(lista_saves))
				time.sleep(1)
				file=str(input("Qual save deseja carregar? "))
				dado=load(file)
				nome=dado["Personagem_Poker"][0]
				dinheiro=dado["Personagem_Poker"][1]
				xp=dado["Personagem_Poker"][2]
				print("Carregando....")
				time.sleep(2)
				print("Sucesso!")
				time.sleep(0.5)
		except:
			print("Não há saves ainda!")


	if acao == "q" or acao == "quitar":
		print("Até mais!")
		break