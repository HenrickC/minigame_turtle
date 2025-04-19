from turtle import Turtle
t = Turtle()

t.speed(1) #ddefine velocidade



while True:
    print("Para onde devemos ir? \"f:frente\" ou \"t:trás\"\n")
    direcao = input();
    if(direcao == "f"):
        print("Quantos pixels devemos movimentar para frente?\n")
        move = int(input())
        t.forward(move)
    else:
        print("Quantos pixels devemos movimentar para trás?\n")
        move = int(input())
        t.backward(move)

    print("Rotacionar para d:direita, e:esquerda ou n:não rotacionar \n")
    resp = input()
    if(resp == 'd'):
        print("Quanto para a direita devemos rotacionar? \n")
        graus = int(input())
        t.right(graus)
    elif(resp == 'e'):
        print("Quanto para a esquerda devemos rotacionar? \n")
        graus = int(input())
        t.left(graus)
    else:
        continue
    print("Continuar andando?\n")
    resp2 = input()
    if(resp2 == 'n'):
        break
input()
