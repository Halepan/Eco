from re import *

from re import IGNORECASE,findall

class TransatorType():
 def __init__(self):
  self.centas = ["cien","ciento","docientos","trecientos","cuatrocientos",
               "quinientos","seicientos","setecientos","ochocientos","novecientos","mil","menos"]
  self.decenascompuestas = [
    "treinta y uno", "treinta y dos", "treinta y tres", "treinta y cuatro",
    "treinta y cinco", "treinta y seis", "treinta y siete", 
    "treinta y ocho", "treinta y nueve",
    "cuarenta y uno", "cuarenta y dos", "cuarenta y tres", "cuarenta y cuatro",
    "cuarenta y cinco", "cuarenta y seis", "cuarenta y siete", 
    "cuarenta y ocho", "cuarenta y nueve",
    "cincuenta y uno", "cincuenta y dos", "cincuenta y tres", "cincuenta y cuatro",
    "cincuenta y cinco", "cincuenta y seis", "cincuenta y siete", 
    "cincuenta y ocho", "cincuenta y nueve",
    "sesenta y uno", "sesenta y dos", "sesenta y tres", "sesenta y cuatro",
    "sesenta y cinco", "sesenta y seis", "sesenta y siete", 
    "sesenta y ocho", "sesenta y nueve",
    "setenta y uno", "setenta y dos", "setenta y tres", "setenta y cuatro",
    "setenta y cinco", "setenta y seis", "setenta y siete", 
    "setenta y ocho", "setenta y nueve",
    "ochenta y uno", "ochenta y dos", "ochenta y tres", "ochenta y cuatro",
    "ochenta y cinco", "ochenta y seis", "ochenta y siete", 
    "ochenta y ocho", "ochenta y nueve",
    "noventa y uno", "noventa y dos", "noventa y tres", "noventa y cuatro",
    "noventa y cinco", "noventa y seis", "noventa y siete", 
    "noventa y ocho", "noventa y nueve"
]
  
  self.decenas = [
    "diez", "once", "doce", "trece", "catorce", "quince", 
    "dieciséis", "diecisiete", "dieciocho", "diecinueve", 
    "veinte", "veintiuno", "veintidós", "veintitrés", 
    "veinticuatro", "veinticinco", "veintiséis", 
    "veintisiete", "veintiocho", "veintinueve", 
    "treinta", "cuarenta", "cincuenta", "sesenta", 
    "setenta", "ochenta", "noventa","cuarto","media"
]
  
  self.unidades =["una","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]

  self.diccionary_num= {"cero": 0,"uno": 1,"dos": 2,"tres": 3,"cuatro": 4,"cinco": 5,"seis": 6,"siete": 7,
        "ocho": 8,"nueve": 9,"diez": 10,"once": 11,"doce": 12,"trece": 13,"catorce": 14,"quince": 15,
        "dieciséis": 16,"diecisiete": 17,"dieciocho": 18,"diecinueve": 19,"veinte": 20,"veintiuno": 21,
        "veintidós": 22,"veintitrés": 23,"veinticuatro": 24,"veinticinco": 25,"veintiséis": 26,
        "veintisiete": 27,"veintiocho": 28,"veintinueve": 29,"treinta": 30,"treinta y uno": 31,
        "treinta y dos": 32,"treinta y tres": 33,"treinta y cuatro": 34,"treinta y cinco": 35,
        "treinta y seis": 36,"treinta y siete": 37,"treinta y ocho": 38,"treinta y nueve": 39,
        "cuarenta": 40,"cuarenta y uno": 41,"cuarenta y dos": 42,"cuarenta y tres": 43,"cuarenta y cuatro": 44,
        "cuarenta y cinco": 45,"cuarenta y seis": 46,"cuarenta y siete": 47,"cuarenta y ocho": 48,
        "cuarenta y nueve": 49,"cincuenta": 50,"cincuenta y uno": 51,"cincuenta y dos": 52,
        "cincuenta y tres": 53,"cincuenta y cuatro": 54,"cincuenta y cinco": 55,"cincuenta y seis": 56,
        "cincuenta y siete": 57,"cincuenta y ocho": 58,"cincuenta y nueve": 59,"sesenta": 60,
        "sesenta y uno": 61,"sesenta y dos": 62,"sesenta y tres": 63,"sesenta y cuatro": 64,
        "sesenta y cinco": 65,"sesenta y seis": 66,"sesenta y siete": 67,"sesenta y ocho": 68,
        "sesenta y nueve": 69,"setenta": 70,"setenta y uno": 71,"setenta y dos": 72,"setenta y tres": 73,
        "setenta y cuatro": 74,"setenta y cinco": 75,"setenta y seis": 76,"setenta y siete": 77,
        "setenta y ocho": 78,"setenta y nueve": 79,"ochenta": 80,"ochenta y uno": 81,"ochenta y dos": 82,
        "ochenta y tres": 83,"ochenta y cuatro": 84,"ochenta y cinco": 85,"ochenta y seis": 86,
        "ochenta y siete": 87,"ochenta y ocho": 88,"ochenta y nueve": 89,"noventa": 90,"noventa y uno": 91,
        "noventa y dos": 92,"noventa y tres": 93,"noventa y cuatro": 94,"noventa y cinco": 95,
        "noventa y seis": 96,"noventa y siete": 97,"noventa y ocho": 98,"noventa y nueve": 99,"cien": 100,
        "doscientos": 200,"trescientos": 300,"cuatrocientos": 400,"quinientos": 500,"seiscientos": 600,
        "setecientos": 700,"ochocientos": 800,"novecientos": 900,"mil": 1000,
    }



  self.frase = " "


 def __RecopilatorNumString(self):
  patron = self.centas
  patron.extend(self.decenascompuestas )
  patron.extend(self.decenas)
  patron.extend(self.unidades)
   
  return findall("|".join(patron),self.frase,IGNORECASE)
      
 def __TransiciontoInt(self,numeros_en_palabras):
  print(numeros_en_palabras)
  numeros = []

  for num in numeros_en_palabras:
   print(self.diccionary_num[num])
   numeros.append(self.diccionary_num[num])

  return {
    'frase': self.frase, 'numeros': numeros # Devuelve la lista de números
  }
 
 def get_Time(self):
  pass

 def getStringInt(self,frase):
  self.frase = frase
  matris = self.__RecopilatorNumString()
  print(self.__TransiciontoInt (matris))
  
  
frase = input()
com = TransatorType()
com.getStringInt(frase)
