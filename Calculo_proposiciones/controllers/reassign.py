from typing import List

def reassign(lista: 'List') -> 'List': #Redefinir los operadores lógicos para lectura de librería
  for i in range(len(lista)):
    lista[i] = lista[i].replace('<->', '=')
    lista[i] = lista[i].replace('¬', 'not')
    lista[i] = lista[i].replace('&', 'and')
    lista[i] = lista[i].replace('|', 'or')
    lista[i] = lista[i].replace('->', '=>')
  return lista