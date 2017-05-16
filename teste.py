import pickle
dado = pickle.load(open("jogo",'wb'))  
nome = dado["jogo"][0]
fichas = dado["jogo"][1]
xp = dado["jogo"][2]
carregado = sim
jogador = Jogador(nome, fichas, xp)
time.sleep(2)
print("O nome do seu personagem é {}, você possui {} de fichas e {} de experiência" .format(nome, fichas, xp)) # Caracterização dos dados para o usuário
