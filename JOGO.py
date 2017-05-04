import time
import pickle
lista_arquivos=[]

def salvar(arquivo,nome, dinheiro,xp):

	lista_arquivos.append(arquivo)
	saves=open("lista", "wb" )
	pickle.dump(lista_arquivos, saves)
	saves.close()
	dados= open(arquivo,'wb') 
	pickle.dump({"{}".format(arquivo) : [nome, dinheiro, xp ]}, dados)
	dados.close()
	time.sleep(0.5)
	print("Jogo salvo com sucesso!")


sim=["sim", "s"]
nao=["nao","n","não"]

print("Bem vindo ao Hsu Poker ")

abrir_salvo=input("Deseja abrir um jogo salvo? \n")  #Verifica se o usário quer abrir um jogo salvo
time.sleep(0.5)

while True:

	if abrir_salvo in sim:

		try:
			lista_arquivos=pickle.load(open("lista","rb"))

			if len(lista_arquivos)>0:
				print("Os saves disponíveis são:")
				time.sleep(0.5)

				for i in lista_arquivos:
					print("{}".format(i))
					time.sleep(0.5)

				arquivo=str(input("Qual save deseja carregar? "))
				dado=pickle.load(open(arquivo,"rb"))  # Traz o jogo salvo com os dados guardados
				nome=dado["{}".format(arquivo)][0]
				dinheiro=dado["{}".format(arquivo)][1]
				xp=dado["{}".format(arquivo)][2]
				carregado=sim
				print("Carregando dados...")
				time.sleep(2)
				print("Você possui {} de dinheiro e {} de experiência" .format(dinheiro,xp))
				break


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

while True:
	if carregado==sim: # Checa se houve o carregamento de dados para pular o processo de escolha de um inspermon
			break
		
	if carregado==nao:  # Caso não tenha nenhum arquivo salvo aberto
		nome=input("Qual vai ser o nome do seu personagem?\n")
		dinheiro= 10000
		xp=0
		print(" Você tem 10 mil fichas para iniciar sua trajetória")
		break

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
			
time.sleep(0.5)
print("Até a próxima!")