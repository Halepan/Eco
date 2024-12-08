
class ComandVoz():#Aqui se ejcutaran lo comandos predefinidos y se agregaran nuevos comandos para la adaptabilidad del sistema a la lengua materna del usuario
    def __init__(self):#constructor
        self.comand_clock= {"1":self.__Clock,"dime la hora": "time","qué hora es":"time",
"avisame dentro de":"temporizador","avisame en":"temporizador","pon un temporizador de":"temporizador",
"despiertame dentro de":"temporizador","despiertame de aquí a":"temporizador","pon una alarma para dentro de ":"temporizador",
"avisame a las":"alarma","despiertame a las":"alarma","pon una alarma ":"alarma"}
        self.comand_music={"1":self.__Music,"para la música": "Stop"}
        self.comand_video={"1":self.__Video}
        self.comand_call={"1":self.__Call}
        self.comand_messege={"1":self.__Messege}
        self.comand_camera={"1":self.__Camera}
        self.comand_redes={"1":self.__Redes}
        self.comand_calendar={"1":self.__Calendar}
        self.list_comand = [self.comand_clock,self.comand_calendar,self.comand_video,
self.comand_music,self.comand_camera,self.comand_messege,self.comand_call]


    def Agg_comand(self,tipe_comand,comand,funcion):
        pass

    def Execute_comand(self,comand):#clasifica los comandos segun el tipo y utiliza los metodos necesarios
        ejecutar = comand["1"]
        ejecutar(comand["2"],comand["3"])

    def __Clock(self,funcion,clave_escuchada):#funcion del reloj , interactua con el usuario y retorna en forma de diccionario intrucciones predefinidas
        print ("Reloj")
        print(funcion)

    def __Music(self,funcion,clave_escuchada):#funcion de la musica , interactua con el usuario y retorna en forma de diccionario intrucciones predefinidas
        print("musica")
        print(funcion)
    
    def __Video(self,funcion,clave_escuchada):#funcion del cideo , interactua con el usuario y retorna en forma de diccionario intrucciones predefinidas
        pass

    def __Call(self,funcion,clave_escuchada):#funcion de las llamadas , interactua con el usuario y retorna en forma de diccionario intrucciones predefinidas
        pass

    def __Messege(self,funcion,clave_escuchada):#funcion de mensages  , interactua con el usuario y retorna en forma de diccionario intrucciones predefinidas
        pass

    def __Camera(self,funcion,clave_escuchada):#funcion de camara , interactua con el usuario y retorna en forma de diccionario intrucciones predefinidas
        pass

    def __Redes(self,funcion,clave_escuchada):#funcion de WIFI y Bluetooth , interactua con el usuario y retorna en forma de diccionario intrucciones predefinidas
        pass

    def __Calendar(self,funcion,clave_escuchada):#funcion del calendario  , interactua con el usuario y retorna en forma de diccionario intrucciones predefinidas
        pass



    