xp = 0
nomeHeroi = input("Digite o Nome do seu Herói: ").title()
print("Você está entrando em uma aventura para se tornar o maior Herói de todos")
list = ["1-Espada", "2-Machado", "3-Arco", "4-Cajado"]
print(list)
arma = str(input("Escolha Sua Arma: ")).upper()
if arma == "MACHADO" or arma == "ESPADA" or arma == "1" or arma == "2":
    print("Você será um Guerreiro")
elif arma == "ARCO" or arma == "3":
    print("Você será um Caçador")
elif arma == "CAJADO" or arma == "4":
    print("Você Será um Mago")
else:
    print("Escolha uma arma valida")
print("Agora que Escolheu sua arma prepare-se para Batalha")
luta=int(input("Quantas batalhas você quer lutar? "))
for c in range(1,luta+1):
    print("Um Ogro apareceu você irá atacar? 1-Ataque 2-Fuja")
    ataque = input("Esolha agora {} ou morra  ".format(nomeHeroi))
if ataque == "1":
    print("Você Derrubou o ogro e ganhou 1000xp")
    xp =int(xp + (c*1000))
else:
    print("Você escolheu a Vergonha {}".format(nomeHeroi))
    xp =int(xp + (c*1000))

print("Depois de Muita luta você {} Conseguiu sua Xp é {}".format(nomeHeroi, xp))
nivel=xp/1000
if xp <=1000:
    print("Parabéns Herói {} você Chegou ao Nível {} e é \033[30mFerro".format(nomeHeroi,nivel))
elif xp >=1001 and xp <= 2000:
    print("Parabéns Herói {} você Chegou ao Nível {} e é \031[37mBronze".format(nomeHeroi, nivel))
elif xp >=2001 and xp <=5000:
    print("Parabéns Herói {} você Chegou ao Nível {} e é \033[37mPrata".format(nomeHeroi, nivel))
elif xp >=5001 and xp <= 8000:
    print("Parabéns Herói {} você Chegou ao Nível {} e é \033[36mPlatina".format(nomeHeroi, nivel))
elif xp >=8001 and xp <= 9000:
    print("Parabéns seu Herói {} você Chegou ao Nível {} e é \033[33mDiamante".format(nomeHeroi, nivel))
elif xp >=9001 and xp <=10000:
    print("Parabéns Herói {} você Chegou ao Nível {} e é \033[35mImortal".format(nomeHeroi, nivel))
elif xp >=10001:
    print("Parabéns Herói {}  Chegou ao Nível {} e é Radiante".format(nomeHeroi, nivel))
