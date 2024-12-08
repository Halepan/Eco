import voice  
import comandVoz 


comandos =  comandVoz.ComandVoz()
translate =  voice.Voice()

dicc = comandos.list_comand
text_recibido = translate.Voz_a_Txt(dicc)#un diccionario con los comandos y el texto introducido

comandos.Execute_comand( text_recibido)#ejecutar los comandos recibidos