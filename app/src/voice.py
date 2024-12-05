import vosk
import pyaudio
import json

class Voice:
  def __init__(self,model_path="app/models/vosk-model-small-es-0.42"):
      self.model_path = model_path
      self.model = vosk.Model(self.model_path)
      self.recognizer= vosk.KaldiRecognizer(self.model, 16000)
      self.p = pyaudio.PyAudio()
      self.stream = self.p.open(format=pyaudio.paInt16,channels=1,rate=16000,input= True,frames_per_buffer=1024)

  def Voz_a_Txt(self,cierre):
      print("Escuchando...")
      data = self.stream.read(1024)
      while True:
        data = self.stream.read(1024)
        if len(data) == 0:
          break
        if self.recognizer.AcceptWaveform(data):
          result = json.loads(self.recognizer.Result())
          print(result["text"])
          for comand in cierre:
            for key in comand:
                if  key in result["text"]:
                  self.__Parar()
                  new_comand = {"1":comand["1"],"2":comand[key],"3": result["text"]}
                  return new_comand
                
  def __Parar(self):
      self.stream.stop_stream()
      self.stream.close()
      self.p.terminate()


