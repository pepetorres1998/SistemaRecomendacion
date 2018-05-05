import random
import sys
import Heroe as h
import Calculos as c

GolpeFuego = h.GolpeFuego()
BolaFuego = h.BolaFuego()
Llamarada = h.Llamarada()
Explosion = h.Explosion()

GolpeRayo = h.GolpeRayo()
BolaRayo = h.BolaRayo()
Relampago = h.Relampago()
Tormenta = h.Tormenta()

GolpeAgua = h.GolpeAgua()
BolaAgua = h.BolaAgua()
Ciclon = h.Ciclon()
Tsunami = h.Tsunami()

GolpeAire = h.GolpeAire()
BolaAire = h.BolaAire()
Ventisca = h.Ventisca()
Tornado = h.Tornado()

GolpeRoca = h.GolpeRoca()
BolaTierra = h.BolaTierra()
Derrumbe = h.Derrumbe()
Terremoto = h.Terremoto()


poder_list = [GolpeFuego, BolaFuego, Llamarada, Explosion, GolpeRayo, BolaRayo, Relampago, Tormenta,
            GolpeAgua, BolaAgua, Ciclon, Tsunami, GolpeAire, BolaAire, Ventisca, Tornado,
            GolpeRoca, BolaTierra, Derrumbe, Terremoto]
a = sys.argv[1]

def generate_binary(a):
    list = []
    for i in range(int(a)):
        list.append("{0:020b}".format(random.randint(1, (2**20)+1)))
    return list

def posicion_true(lista):
    posicion = []
    for i in lista:
        p = []
        #print(i)
        for j in range(len(i)):
            #print(i[j])
            if(i[j] == '1'):
                p.append(j)
        posicion.append(p)
    return posicion

def poderes_true(poder, pos):
    for i in range(int(a)):
        for j in range(20):
            if(j in pos[i]):
                print(j+1)
                print(poder[j].__class__.__name__)
                print(poder[j].damage)
                print()

def poderes_main(poder, pos, h1, h2):
    peso_cromosomas = []
    for i in range(int(a)):#for para lista de cromosomas
        peso_total = 0
        for j in range(20):#for para cromosoma
            if(j in pos[i]):
                if(c.Peso(h1, h2, poder[j]) == 0):
                    peso_cromosomas.append(0)
                    print('if')
                    print(peso_cromosomas)
                    break
                else:
                    peso_total = peso_total+c.Peso(h1, h2, poder[j])
                    print('else')
                    print(peso_total)
            if(j in pos[i] and c.Peso(h1, h2, poder[j]) == 0):#Rompe el for del cromosoma si es igual a 0
                break
        if(j in pos[i] and c.Peso(h1, h2, poder[j]) == 0): #Continua con la sig iteracion de la lista si es igual a 0
            continue
        print(peso_total)
        peso_cromosomas.append(peso_total)
        print(peso_cromosomas)
    return peso_cromosomas

blist = generate_binary(a)
pos = posicion_true(blist)

print(blist)
print(pos)
print()
print()
peso_cromosomas = poderes_main(poder_list, pos, c.k1, c.s2)
print(peso_cromosomas)
#poderes_true(poder_list, pos)