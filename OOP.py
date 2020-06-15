class matriz(object):

    def __init__(self, data = []):
        self.data = data
    
    def __len__(self):
        return len(self.data)

    def equalLenghts(self,nextObjeto):
        return len(self)==len(nextObjeto)

    def condmulmatricial(self, arreglo):
        filas = len(self.data)
        columnas = len(arreglo.data)
        return filas == columnas
            
    def __add__(self, sumando):
        if self.equalLenghts(sumando):
            x=[]
            for i in range(len(self.data)):
                y=[]
                for j in range(len(self.data[0])):
                    y.append(self.data[i][j] + sumando.data[i][j])
                x.append(y)
            return matriz(x)
        else:
            raise ErrorDimensional(len(self.data),len(sumando.data))
    
    def __mul__(self, multip):
        x=[]
        
        if type(multip) == int or type(multip)==float:
            for i in self.data:
                y=[]
                for j in i:
                    y.append(j*multip)
                x.append(y)
            return matriz(x)

        else:
            if self.condmulmatricial(multip):
                for i in range(len(self.data)):
                    
                    acumulador=[]
                    while(len(acumulador)!=len(self.data)):
                        a=0
                        total=0
                        for j in range(len(multip.data[0])):
                            total = total + (self.data[i][j]*multip.data[j][a])
                        acumulador.append(total)
                        a = a + 1 
                    x.append(acumulador)
                return matriz(x)

        
    def determinante(self):
        for z in range(len(self.data)-1):
            for x in range(1, len(self.data)-z):
                if self.data[z][z] != 0:
                    p = self.data[x+z][z] / self.data[z][z]
                    for y in range(len(self.data)):
                        self.data[x+z][y] = self.data[x+z][y] - (self.data[z][y]*p)

        deter = 1
        for x in range(len(self.data)):
            deter = self.data[x][x]*deter
        return deter

    def identidad(self):
        id = []
        for i in range(len(self.data)):
            filas=[]
            for j in range(len(self.data[0])):
                if (i==j):
                    filas.append(1)
                else:
                    filas.append(0)
            id.append(filas)
        return matriz(id)
    
    def aumentada(self):
        aumen = []
        for i in range(len(self.data)):
            filai = []
            for j in range(len(self.data[0])):
                filai.append(self.data[i][j])
                if(j==len(self.data[0])):
                    filai.extend(self.data.identidad[i])
            aumen.append(filai)
                
        return matriz(aumen)

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return self.__str__()

class ErrorDimensional(Exception):
    def __init__(self,l1,l2):
        self.l1=l1
        self.l2=l2
    
    def __str__(self):
        return str("Las longitudes no coinciden: " + str(len(self.l1)) + "~=" + str(len(self.l2)))
    
    def __repr__(self):
        return self.__str__()

class ErrorDimensionalMat(Exception):
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    def __str__(self):
        return "Las dimensiones no cumplen"
    
    def __repr__(self):
        return self.__str__()