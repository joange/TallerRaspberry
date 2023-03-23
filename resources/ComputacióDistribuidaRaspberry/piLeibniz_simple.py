import time 
import math

def calcPi(tamany=10):

    pi4 = 0.0 

    n=1
    s=1

    for i in range(tamany):
        pi4+=s*1/n
        n+=2
        s*=-1

    return pi4*4;

tam=10
for i in range(1,11):
    start = time.time() 
    pi_calc=calcPi(tam)
    temps= time.time()-start 
    print('Valor calculat amb %12d elements  %.30f en %10.6f s. Error=%.40f'%(tam,pi_calc,temps,abs(pi_calc-math.pi)))
    tam*=10

print('Valor real de pi                 %.60f'%(math.pi))

'''
MacBook-Pro-de-Joan:~ joange$ /usr/local/bin/python3.6 /Users/joange/Dropbox/Cursos/Tallers/ComputacióDistribuidaRaspberry/piLeibniz_simple.py
Valor calculat amb           10 elements  3.041839618929403243896558706183 en   0.000011 s. Error=0.0997530346603898721014047623611986637115
Valor calculat amb          100 elements  3.131592903558553686593768361490 en   0.000021 s. Error=0.0099997500312394294041951070539653301239
Valor calculat amb         1000 elements  3.140592653839794134995599961258 en   0.000495 s. Error=0.0009999997499989810023635072866454720497
Valor calculat amb        10000 elements  3.141492653590034489496929381858 en   0.002329 s. Error=0.0000999999997586265010340866865590214729
Valor calculat amb       100000 elements  3.141582653589719775766297971131 en   0.068569 s. Error=0.0000100000000733402316654974129050970078
Valor calculat amb      1000000 elements  3.141591653589774324473182787187 en   0.255613 s. Error=0.0000010000000187915247806813567876815796
Valor calculat amb     10000000 elements  3.141592553589791503299011310446 en   1.808036 s. Error=0.0000001000000016126989521580981090664864
Valor calculat amb    100000000 elements  3.141592643589325994923910911893 en  18.361582 s. Error=0.0000000100004671210740525566507130861282
Valor calculat amb   1000000000 elements  3.141592652588050427198140823748 en 177.968044 s. Error=0.0000000010017426887998226447962224483490
Valor calculat amb  10000000000 elements  3.141592653488345820989025014569 en 1947.751928 s. Error=0.0000000001014472950089384539751335978508
Valor real de pi                 3.141592653589793115997963468544185161590576171875000000000000
'''