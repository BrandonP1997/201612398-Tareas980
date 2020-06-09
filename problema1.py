
print('Ingrese el numero:')
N = int(input())

def division(num):
    if(num>1):
        dividendos = list(range(1,num))
        Sparcial = 0
        for i in dividendos:
            cociente = num%i
            if (cociente==0):
                Sparcial = Sparcial + i
    else:
        Sparcial = 0
    return Sparcial     
          
print('La division es: ', division(N))


def BuscarNumsP(num):
    posibles = list(range(2,num + 1))
    NPer = []
    for i in posibles:
        
        divisores = list(range(1, i ))
        sumaiesimo = 0
        for j in divisores:
            cociente = i % j
            if (cociente==0):
                sumaiesimo = sumaiesimo + j
        if(sumaiesimo==i):
            NPer.append(i)

    return NPer            
print('Los numeros perfectos son:',BuscarNumsP(N))

def BuscarNumsA(num):
    posibles = list(range(2,num + 1))
    NA = []
    friends = []

    for i in posibles:
        divisores = list(range(1, i))
        sumaiesimo = 0
        for j in divisores:
            cociente = i % j
            if (cociente==0):
                sumaiesimo = sumaiesimo + j
        NA.append(sumaiesimo)

    for i in NA:
        for j in range(len(posibles)):
            if (division(i)==posibles[j]):
                friends.append((posibles[j], NA[j]))
    return friends  
        
print('Los numeros amigos son',BuscarNumsA(N))

