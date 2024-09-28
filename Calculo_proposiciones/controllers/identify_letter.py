from typing import List

def identify_letter(proposition: 'str') -> List: #Identificar las variables para los valores de verdad
  chars = []
  for i in proposition:
    if ord(i) >= 97 and ord(i) <= 122:
      if i not in chars:
        chars.append(i)
  return chars #lista con todas las letras