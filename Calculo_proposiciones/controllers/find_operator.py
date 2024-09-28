from controllers.is_operator import is_operator

def find_operator(prop:'str') -> 'tuple':
  cont = 0
  for i in range(len(prop)):
    #Sumar y restar los paréntesis hasta que el cont sea cero
    if prop[i] == '(':
      cont += 1
    elif prop[i] == ')':
      cont -= 1
    elif cont == 0:
      # Detectar el operador lógico.
      #Separar proposición
      if prop[i:i+2] == '->':
        return i, '->'
      elif prop[i:i+3] == '<->':
        return i, '<->'
      elif is_operator(prop[i]):
        return i, prop[i]
    i += 1
  return -1, None