# Funcion de suma
def sumamatriz(matriz1, matriz2):
    matrizsuma = matrizvacia(len(matriz1), len(matriz2[0]))

    for fila in range(len(matriz1)):
        for col in range(len(matriz1[1])):
            matrizsuma[fila][col] = matriz1[fila][col] + matriz2[fila][col]

    return matrizsuma


# Funcion de resta
def restamatriz(matriz1, matriz2):
    matrizrest = matrizvacia(len(matriz1), len(matriz2[0]))
    for fila in range(len(matriz1)):
        for col in range(len(matriz2[1])):
            matrizrest[fila][col] = matriz1[fila][col] - matriz2[fila][col]

    return matrizrest


# Funcion de multiplicacion
def multiplicacion(matriz1, matriz2):
    matrizmulti = matrizvacia(len(matriz1), len(matriz2[0]))
    if len(matriz1[0]) == len(matriz2):
        for i in range(len(matriz1)):
            for j in range(len(matriz2[0])):
                for k in range(len(matriz2)):
                    matrizmulti[i][j] += matriz1[i][k] * matriz2[k][j]

        return matrizmulti
    else:
        return ("Recuerda que la multiplicacion entre matrices debe ser mxn * nxp")


# Funcion de multiplicar una matriz por un escalar
def escalar_matriz(numero, matriz):
    matriz_escalar = []
    for i in range(len(matriz)):
        temp = []
        for j in range(len(matriz[0])):
            a = numero * matriz[i][j]
            temp.append(a)
        matriz_escalar.append(temp)
    return matriz_escalar


# Funcion de trasposicion de matriz determinada
def trasponerMatrices(matriz):
    matriztras = []
    for fila in range(len(matriz[0])):
        matriztras.append([])
        for col in range(len(matriz)):
            matriztras[fila].append(matriz[col][fila])

    return matriztras

from random import randint

#Funcion que crea un laberinto planteado por el usuario donde el ingresa los valores.
def crear_laberinto_ingresado_por_usuario(N):
  #Creamos una lista vacia que representara al laberinto.
  matriz_lab = []
  for i in range(N):
    fila = []
    for j in range (N):
        a = input(f"Ingrese un valor ya sea solo uno para agrgar a la matriz laberinto de posicion [{i}],[{j}]: ")
        #Mientras la cifra ingresada no sea "1" o "0",se le volvera pedir ingresar el valor al usuario.
        while not verificar_cifra(a):
            a = input("ERROR!, Ingrese un valor correcto ya sea '1' o '0': ")
        #Como inicialmente llamamos un string convertimos los valores aceptados a un numero entero.
        a = int(a)
        #Luego agregamos el valor en la fila ira en la matriz laberinto.
        fila.append(a)
    #Agregamos la fila a la matriz laberinto.
    matriz_lab.append(fila)

  #Sabemos que en los laberintos planteados con matrices la prosicion inicial debe tener un valor de "1".
  #Ademas al momento que el usuario llene el laberinto con valores, hay la posibilidad
  # de que ingrese en la posicion inicial un valor diferente de "1".
  if matriz_lab[0][0] != 1:
      print("Lo sentimos el valor de la posicion [0],[0] no puede ser 0 por lo tanto se le reasignara a 1")
      # Por lo que en todos los laberintos creados por el usuario obligamos que la posicion inicial sea "1".
      matriz_lab[0][0] = 1

  # Sabemos que en los laberintos planteados con matrices la prosicion final debe tener un valor de "1".
  # Ademas al momento que el usuario llene el laberinto con valores, hay la posibilidad
  # de que ingrese en la posicion final un valor diferente de "1".

  if matriz_lab[N - 1][N - 1] != 1:
      print(f"Lo sentimos el valor de la posicion [{N - 1}],[{N - 1}] no puede ser 0 por lo tanto se le reasignara a 1")
      matriz_lab[N - 1][N - 1] = 1

  return matriz_lab


def crear_laberinto_aleatorio(N):
  #Creamos una lista vacia
  matriz = []
  for i in range(N):
    fila = []
    for j in range(N):
        a = randint(0,1)
        # Agregamos a la lista fila valores aleatorios ya sean "0" o "1"
        fila.append(a)
    #Agregamos a la matriz que representara al laberinto las filas con "0" y "1"
    matriz.append(fila)
  #Sabemos que en los laberintos planteados con matrices la prosicion inicial debe tener un valor de "1".
  #Ademas al llenar el laberinto con valores aleatorios hay la posibilidad de que la posicion inicial sea 0.
  #Por lo que en todos los laberintos creados aleatoriamente obligamos que la posicion inicial sea "1".
  matriz[0][0]=1

  #Sabemos que en los laberintos planteados con matrices la prosicion final debe tener un valor de "1".
  #Ademas al llenar el laberinto con valores aleatorios hay la posibilidad de que la posicion final sea "0".
  #Por lo que en todos los laberintos creados aleatoriamente obligamos que la posicion final sea "1".
  matriz[N-1][N-1]=1

  #Finalmente retornamos la matriz que representaria al laberinto creado aleatoriamente.
  return matriz

#Funcion para verificar que la cifra sea "0" o "1":
def verificar_cifra(numero):
    if numero == "0" or numero == "1":
        return True
    else:
        return False

def is_safe(laberinto,N, x, y):
    #Funcion utilitaria que verifica si x, y son indices validos
    if x >= 0 and y >= 0 and x < N and y < N and laberinto[x][y] == 1:
        return True
    return False

def print_solution(sol):
    #Funcion utilitaria para imprimir la solución de la matriz
    print("Matriz que refleja la solucion")
    for i in sol:
        for j in i:
            print(str(j) + " ", end = "")
        print("")

def solve_laberinto(laberinto,N):
    #Crear a 4*4 2D list
    sol = [[0 for _ in range(N)] for _ in range(N)]

    if solve_laberinto_util(laberinto,N, 0, 0, sol) == False:
        print("No existe Solución")
        return False
    print_solution(sol)
    return True

#Función Recursiva utilitaria para resolver el problema del laberinto
def solve_laberinto_util(laberinto,N, x, y, sol):

    #Si se llego a la posicion final return True
    if x == N-1 and y == N-1:
        sol[x][y] = 1
        return True
    #verificar si laberinto[x][y] es valido
    if is_safe(laberinto,N, x, y) == True:
        #marcar x, y como parte de la solución
        sol[x][y] = 1
        #movemos hacia adelante
        if solve_laberinto_util(laberinto,N, x+1, y, sol) == True:
            return True

        #si moviendo hacia adelante no nos da la solución
        #entonces movemos hacia abajo
        if solve_laberinto_util(laberinto,N, x, y+1, sol) == True:
            return True

        #si ninguno de los movimientos funciona
        #BACKTRACK: desmarcamos x, y como parte de la solución
        sol[x][y] = 0
        return False

#Mostrar laberinto
def mostrar_lab_planteado(labo):
    for i in range (len(labo)):
        for j in range(len(labo[0])):
            print(labo[i][j], end=" ")
        print()
    return " "


#Creador de la matriz para la resolucion de las operaciones
def matrizvacia(m,n):
    matrizvacia = []
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(0)
        matrizvacia.append(row)
    return matrizvacia