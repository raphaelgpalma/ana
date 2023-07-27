import wikipedia as w
import speech_recognition as sr
import pyttsx3
import sys
import time as t

keywords = ["definir", "defesa", "o que é", "o que foi", "quem é", "quem foi", "quem era", "procure por", "defina",
            "definição de", "busque a definição", "explique a", "explique o", "defesa"]
w.set_lang("pt-BR")
audio = sr.Recognizer()
machine = pyttsx3.init()
machine.say("Olá, eu sou a ANA, sua Assistente de Navegação Autônoma")
machine.say("como posso ajudar?")
machine.runAndWait()


def execute():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voz = audio.listen(source)
            command = audio.recognize_google(voz, language="pt-br")
            command = command.lower()
            return command
    except:
        machine.say("Não entendi o que você disse, tente novamente por favor.")
        machine.runAndWait()


def evaluate(query):
    for keyword in keywords:
        if query.startswith(keyword):
            return query.replace(keyword, "    ")


while True:
    word = execute()
    print(word)
    if "agora" in word:
        machine.say("tudo bem, espero que eu seja útil posteriormente.")
        machine.runAndWait()
        break

    print(w.summary(word))
    machine.say(w.summary(word))
    machine.runAndWait()

    t.sleep(5)
    machine.say("algo mais que eu possa ajudar?")
    machine.runAndWait()

sys.exit()
