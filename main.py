from turtle import Turtle
t = Turtle()

t.speed(1) #ddefine velocidade




def escolha_rotacao():
    print("Rotacionar para d:direita, e:esquerda ou n:não rotacionar \n")
    resp = input()
    return resp

def rotacao_direita(turtle):
    print("Quanto para a direita devemos rotacionar? \n")
    graus = int(input())
    t.right(graus)

def rotacao_esquerda(turtle):
    print("Quanto para a esquerda devemos rotacionar? \n")
    graus = int(input())
    t.left(graus)


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

    resp = escolha_rotacao()
    if(resp == 'd'):
        rotacao_direita(t)
    elif(resp == 'e'):
       rotacao_esquerda(t)
    else:
        continue
    print("Continuar andando?\n")
    resp2 = input()
    if(resp2 == 'n'):
        break

input()
