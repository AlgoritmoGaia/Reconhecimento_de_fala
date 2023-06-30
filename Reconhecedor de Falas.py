import speech_recognition as sr
import pyttsx3

def ouvir_e_transcrever():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Fale alguma coisa...")
        audio = r.listen(source)

        try:
            texto = r.recognize_google(audio, language="pt-BR")
            return texto
        except sr.UnknownValueError:
            print("Não foi possível reconhecer o áudio.")
        except sr.RequestError:
            print("Não foi possível acessar o serviço de reconhecimento de fala.")

def ler_em_voz_alta(texto):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Define a velocidade da voz (padrão: 200)
    engine.setProperty("volume", 1.0)  # Define o volume da voz (padrão: 1.0)
    engine.say(texto)
    engine.runAndWait()

# Exemplo de uso
while True:
    transcricao = ouvir_e_transcrever()
    if transcricao:
        print("Transcrição: " + transcricao)
        ler_em_voz_alta(transcricao)
