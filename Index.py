import os

base= 0
cont=0
classe=0
ataque=0
luta=0
rodadas=0
nomeHeroi = input("Digite o Nome do seu Herói: ").title()
print("Você está entrando em uma aventura para se tornar o maior Herói de todos")
list = ["1-Espada", "2-Machado", "3-Arco", "4-Cajado"]
print(list)
arma = str(input("Escolha Sua Arma: ")).upper()
if arma == "ESPADA" or arma == "1" :
    print("Você será um Espadachin")
    classe="Espadachin"
    ataque="Espada Cortante"
elif arma == "Machado" or arma == "2":
    print("Você será um Bárbaro")
    classe="Bábaro"
    ataque="Machadada Dupla"
elif arma == "ARCO" or arma == "3":
    print("Você será um Caçador")
    classe="Caçador"
    ataque="Flecha Perfurante"
elif arma == "CAJADO" or arma == "4":
    print("Você Será um Mago")
    classe="Mago"
    ataque="Bola de Fogo"
else:
    print("Você não escolheu uma opção válida, então acabou ficando sem arma")
    classe="Aldeão"
    ataque="Soco"

print("Agora que Escolheu sua arma prepare-se para Batalha")
rodadas=int(input("Quantas batalhas você quer lutar? "))
for c in range(1,rodadas+1):
    print("Um Ogro apareceu você irá atacar? 2-Ataque 1-Fuja")
    luta =int(input("Esolha agora {} {} ou morra  ".format(classe,nomeHeroi)))
    if luta %2==0:
        print("{} {} você usou o ataque \033[031m{}\033[0;0m Derrubou o ogro e ganhou 1000xp".format(classe,nomeHeroi,ataque))
        base +=luta
        cont +=1
    else:
        print("{} {} Você escolheu a Vergonha".format(classe,nomeHeroi))
xp=(base/2)*1000
nivel=xp/1000

print("{} {} Depois de Muita luta você Conseguiu sua Xp é {}".format(classe,nomeHeroi, xp))
if xp <=1000:
    print("Parabéns {} {} você Chegou ao Nível {} e é \033[47mFerro\033[0;0m".format(classe,nomeHeroi,nivel))
elif xp >=1001 and xp <= 2000:
    print("Parabéns {} {} você Chegou ao Nível {} e é \033[37mBronze\033[0;0m".format(classe,nomeHeroi, nivel))
elif xp >=2001 and xp <=5000:
    print("Parabéns {} {} você Chegou ao Nível {} e é \033[37mPrata\033[0;0m".format(classe,nomeHeroi, nivel))
elif xp >=5001 and xp <= 8000:
    print("Parabéns {} {} você Chegou ao Nível {} e é \033[36mPlatina\033[0;0m".format(classe,nomeHeroi, nivel))
elif xp >=8001 and xp <= 9000:
    print("Parabéns seu {} {} você Chegou ao Nível {} e é \033[33mDiamante\033[0;0m".format(classe,nomeHeroi, nivel))
elif xp >=9001 and xp <=10000:
    print("Parabéns {} {} você Chegou ao Nível {} e é \033[35mImortal\033[0;0m".format(classe,nomeHeroi, nivel))
elif xp >=10001:
    print("Parabéns {} {}  Chegou ao Nível {} e é Radiante".format(classe,nomeHeroi, nivel))
