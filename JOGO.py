import time


sim=["sim", "s"]
nao=["nao","n","não"]

print("Bem vindo ao Hsu Poker ")

abrir_salvo=input("Deseja abrir um jogo salvo? \n ")  #Verifica se o usário quer abrir um jogo salvo
time.sleep(0.5)

while True:

	if abrir_salvo in sim:
					
		try:
			salvo=pickle.load(open("jogo_salvo","rb"))  # Traz o jogo salvo com os dados guardados
			nome=salvo["Personagem_Poker"][0]
			dinheiro=salvo["Personagem_Poker"][1]
			xp=salvo["Personagem_Poker"][2]

			carregado=sim
			print("Carregando dados...")
			time.sleep(2)
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
		dinheiro_inicial= 10000
		print(" Você tem 10 mil fichas para iniciar sua trajetória")


while True:

		time.sleep(0.5)
		salvar_jogo=input("Deseja salvar o jogo? \n") # Pergunta se deseja salvar o jogo
		salvar_jogo=salvar_jogo.lower()

		if salvar_jogo in sim: # Caso o usuário queira salvar o jogo
			dados= open("jogo_salvo",'wb') 
			pickle.dump({"Personagem_Poker" : [nome, dinheiro, xp]}, dados)
			dados.close()
			time.sleep(0.5)
			print("Jogo salvo com sucesso!")
			break

		if salvar_jogo in nao: # Caso não queira salvar o jogo
			break

		else:
			print("Digite um comando válido (Sim ou Não)")
			continue
