import re
from word2number import w2n

def reconocer_numeros(frase):
  # Expresión regular para encontrar números en palabras
  patron = r'\b(?:mil|doscientos|trescientos|cuatrocientos|quinientos|seiscientos|setecientos|ochocientos|novecientos|cien|noventa|ochenta|setenta|sesenta|cincuenta|cuarenta|treinta|veinte|veintiuno|veintidós|veintitrés|veinticuatro|veinticinco|veintiséis|veintisiete|veintiocho|veintinueve|treinta y uno|treinta y dos|treinta y tres|treinta y cuatro|treinta y cinco|treinta y seis|treinta y siete|treinta y ocho|treinta y nueve|cuarenta y uno|cuarenta y dos|cuarenta y tres|cuarenta y cuatro|cuarenta y cinco|cuarenta y seis|cuarenta y siete|cuarenta y ocho|cuarenta y nueve|cincuenta y uno|cincuenta y dos|cincuenta y tres|cincuenta y cuatro|cincuenta y cinco|cincuenta y seis|cincuenta y siete|cincuenta y ocho|cincuenta y nueve|sesenta y uno|sesenta y dos|sesenta y tres|sesenta y cuatro|sesenta y cinco|sesenta y seis|sesenta y siete|sesenta y ocho|sesenta y nueve|setenta y uno|setenta y dos|setenta y tres|setenta y cuatro|setenta y cinco|setenta y seis|setenta y siete|setenta y ocho|setenta y nueve|ochenta y uno|ochenta y dos|ochenta y tres|ochenta y cuatro|ochenta y cinco|ochenta y seis|ochenta y siete|ochenta y ocho|ochenta y nueve|noventa y uno|noventa y dos|noventa y tres|noventa y cuatro|noventa y cinco|noventa y seis|noventa y siete|noventa y ocho|noventa y nueve|diez|once|doce|trece|catorce|quince|dieciséis|diecisiete|dieciocho|diecinueve|un|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|cero)\b'

  
  numeros_en_palabras = re.findall(patron, frase)
  numeros = []
  return numeros_en_palabras

  """for num in numeros_en_palabras:
    try:
      # Convierte la palabra a número
      numeros.append(w2n.word_to_num(num))
    except ValueError:
      # Si no es un número válido, ignora la palabra
      pass

  if not numeros:
    return False # No se encontraron números

  return {
    'frase': frase,
    'numeros': numeros # Devuelve la lista de números
  }"""

# Ejemplo de uso
resultado = reconocer_numeros("A las cinco y treinta y cinco")
print(resultado) # {'frase': 'A las cinco y treinta y cinco', 'numeros': [5, 35]}

resultado_vacio = reconocer_numeros("No hay números aquí")
print(resultado_vacio) # False


