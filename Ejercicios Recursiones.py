#Funcion para encontrar todas las permutaciones de una lista dada
def dfs_permutaciones(lista):
  resultado = []
  return dfs_p([], lista, resultado)

def dfs_p(actual, restantes, resultado):
  if len(restantes) == 0:
    resultado.append(actual)
    return resultado
  for i in range(len(restantes)):
    siguiente = restantes[i]
    nuevo_resto = restantes[:i] + restantes[i+1:]
    dfs_p(actual + [siguiente], nuevo_resto, resultado)
  return resultado

dfs_permutaciones([1,2,3])

#Funcion para encontrar todas las combinaciones de r elementos de una lista dada
def dfs_combinaciones(lista, r):
  resultado = []
  return dfs_c([], 0, lista, r, resultado)

def dfs_c(actual, inicio, lista, r, resultado):
  if len(actual) == r:
    resultado.append(actual)
    return resultado
  for i in range(inicio, len(lista)):
    dfs_c(actual+[lista[i]], i+1, lista, r, resultado)
  return resultado

dfs_combinaciones([1,2,3,4], 2)

#Funcion para calcular el factorial de un entero no negativo n
def factorial(n):
  if n == 0:
    return 1
  else:
    return n*factorial(n-1)

factorial(6)
