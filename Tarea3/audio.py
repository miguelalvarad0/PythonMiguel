#importar libreria de TTS: text to speech para traducit un texto a audio
#importar libreria playsound para ejecutar/reproducir un archivo mp3
from gtts import gTTS
from playsound import playsound


# salida de audio
def reproducir_audio(resultado):
        print("Cargando...")
        frase = "El resultado de la operación es : "
        speech = frase + str(resultado) #concatenar parametro de entrada con texto 
        tts = gTTS(speech, lang='es') #convertir el texto en audio en espanol
        tts.save("tt5.mp3") #generar y nombrar y guardar archivo mp3
        playsound(r'tt5.mp3') #ejecutar archivo mp3 y reproducir audio / REPRODUCIR RESULTADO DE LA OPERACION
