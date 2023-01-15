import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as spi

def desenhar(Coordenadas, Cor, CorPontos):
    xs = []
    ys = []
    for ponto in Coordenadas:
        xs.append(ponto[0])
        ys.append(ponto[1])

    t = np.array(range(0, len(xs)))

    x_cubic = spi.CubicSpline(t, xs)
    y_cubic = spi.CubicSpline(t, ys)
    
    ts = np.linspace(0, len(t)-1, 200)

    for x, y in zip(xs, ys):
        #plt.plot(x, y, marker='o', color=CorPontos, lw=1)
        pass
    plt.plot(x_cubic(ts), y_cubic(ts), color=Cor)

def rosto(Cor='black', CorPontos='orange'):
    coordenadas = [(-6, -5), (-5,-6), (-3.75,-6.5), (-2,-6.75), (0,-6.5), (0.5, -7.5), (1.5, -7.25), (1.5,-6), (3,-5.25), (5,-4), (6.75,-2), (8,0), (8.5,2), (8,4), (7.15,5.15), (6,6), (5,6.5), (4, 7)]
    desenhar(coordenadas, Cor, CorPontos)

def roupa(Cor='black', CorPontos='orange'):
    coordenadas = [(-6, -9), (-5, -7), (-3.75, -6.5), (-2, -6.75), (0, -6.5), (0.5, -7.5), (1.5, -7.25), (1.5, -6), (3, -5.25), (4.2, -4.6), (5, -4.4), (7,-5), (6,-6), (5,-7), (4, -6.5), (6, -8), (7, -9)]
    desenhar(coordenadas, Cor, CorPontos)

def nariz(Cor='black', CorPontos='orange'):
    coordenadas = [(0.7, 1.8), (1.45, 3), (2.7, 2.2)]
    desenhar(coordenadas, Cor, CorPontos)

def contorno_olhos(Cor='black', CorPontos='orange'):
    coordenadas = [(-2, 1.5), (-3, 2.5), (-3.75, 4), (-4, 5), (-4, 6), (-3.5, 7), (-2.5, 7.75), (-1, 7), (-0.25, 6), (0.5, 5.75), (1.25, 7), (2, 8), (3, 8), (4, 7), (4.45, 6), (5, 4)]
    desenhar(coordenadas, Cor, CorPontos)

def olho_dir(Cor='black', CorPontos='orange'):
    coordenadas = [(2,4.25), (2.25,6), (3.5,5), (3.25,3.5), (2,4.25)]
    desenhar(coordenadas, Cor, CorPontos)

def olho_esq(Cor='black', CorPontos='orange'):
    coordenadas = [(-2,4), (-1.5,5.75), (-0.25,4.5), (-0.5,3), (-2, 4)]
    desenhar(coordenadas, Cor, CorPontos)

def cabeca(Cor='black', CorPontos='orange'):
    coordenadas = [(-2.5, 10), (-8, 10)]
    desenhar(coordenadas, Cor, CorPontos)

def orelha(Cor='black', CorPontos='orange'):
    coordenadas = [(-5.5, -4.5), (-6,-5), (-8,-6), (-10,-5), (-11.5,-2.5),(-12.25,0.25), (-11.75,2.25), (-10,3.5), (-7,2)]
    desenhar(coordenadas, Cor, CorPontos)

def dentes(Cor='black', CorPontos='orange'):
    coordenadas = [(4, 0.25), (3, 0.5), (1, -0,25), (1.75, -1), (2.5, -0.5), (3.25, -1), (4, 0.25)]
    desenhar(coordenadas, Cor, CorPontos)

def boca(Cor='black', CorPontos='orange'):
    coordenadas = [(1, 0.1), (-1, -2), (-1.5, -4), (0, -5), (1.5, -4,), (3.25, -1.05)]
    desenhar(coordenadas, Cor, CorPontos)

def mao(Cor='black', CorPontos='orange'):
    coordenadas = [(4.5, 8.75), (3.75, 9.5),(3, 9.75), (3, 10), (2, 10.5), (1, 10.75), ( 0.25, 11), (-2, 10.75), (-2.25, 9.25), (-1, 9.25), (0.25, 11), (-1, 9.25), (0.5, 9), (2, 10.5), (0.5, 9), (1.75, 8.45), (3, 9.75), (1.75, 8.45), (3.5, 8.25), (4.5, 8.75)]
    desenhar(coordenadas, Cor, CorPontos)

def resto_do_cabelo(Cor='black', CorPontos='orange'):
    coordenadas = [(-12.2, 1.3), (-11.75 ,4),(-11, 6), (-9.5, 9), (-8, 10), (-9.5, 9.75), (-11, 8), (-12, 5), (-12.5, 3), (-12.75,1), (-12.2, 1.3)]
    desenhar(coordenadas, Cor, CorPontos)

    coordenadas = [(-10.75, 3.25), (-9.5, 6), (-7.75, 9), (-6.75, 10), (-8, 9.75), (-9.5, 8), (-10.5, 6), (-11.75, 2.3)]
    desenhar(coordenadas, Cor, CorPontos)
    
    coordenadas = [(-8.5, 3.25), (-8, 6), (-6.5, 9), (-5.5, 10), (-6.5, 9.75), (-8, 8), (-9.5, 5), (-10, 3.5)]
    desenhar(coordenadas, Cor, CorPontos)
    
    coordenadas = [(-7, 2), (-6.5, 6), (-4.5, 9), (-3, 10), (-5, 9.75), (-6.5, 8), (-7.75, 5), (-7.75, 2.75)]
    desenhar(coordenadas, Cor, CorPontos)
    
    coordenadas =  [(-2, 9), (-3.5, 7), (-5, 4), (-6.25, 1), (-6.25, 3), (-6, 5), (-4.75, 8),  (-2.5, 9.5)]
    desenhar(coordenadas, Cor, CorPontos)

def cabelinho(Cor='black', CorPontos='orange'):
    coordenadas = [(-2.5,10),(-2.5,11),(-3.5,12),(-4.75,11.5)]
    desenhar(coordenadas, Cor, CorPontos)

    coordenadas = [(-2.5,10),(-1.75,12),(-2.25,13),(-3,13.2)]
    desenhar(coordenadas, Cor, CorPontos)

    coordenadas = [(-2.5,10),(-1,12),(0,13),(0.5,12.5)]
    desenhar(coordenadas, Cor, CorPontos)

def braco(Cor='black', CorPontos='orange'):
    coordenadas = [(6.75, -4.75), (7.75, -3),(8, 0)]
    desenhar(coordenadas, Cor, CorPontos)

    coordenadas = [(6.5, 5.75), (5.6, 7.5), (4.5, 8.75)]
    desenhar(coordenadas, Cor, CorPontos)

def lingua(Cor='black', CorPontos='orange'):
    coordenadas = [(-1.45, -4), (0.25, -2.25),(2.75, -1.75)]
    desenhar(coordenadas, Cor, CorPontos)

rosto()
orelha()
roupa('red')
braco()

nariz()

contorno_olhos()
olho_esq()
olho_dir()

dentes()
boca()
lingua('red')

cabeca()

mao()

cabelinho()
resto_do_cabelo()

plt.xticks(range(-16, 17, 1))
plt.yticks(range(-9, 17, 1))
plt.grid()
