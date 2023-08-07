# Importação das bibliotecas necessárias
import wikipedia as w
import speech_recognition as sr
import pyttsx3

# Lista de palavras-chave para identificar o tipo de consulta do usuário
keywords = ["definir", "defesa", "o que é", "o que foi", "quem é", "quem foi", "quem era", "procure por", "defina",
            "definição de", "busque a definição", "explique a", "explique o", "defesa"]

# Configuração da linguagem para a biblioteca Wikipedia
w.set_lang("pt-BR")

# Inicialização do mecanismo de voz
audio = sr.Recognizer()
machine = pyttsx3.init()

# Função para executar o reconhecimento de fala
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

# Função para avaliar a consulta do usuário e remover as palavras-chave
def evaluate(query):
    for keyword in keywords:
        if query.startswith(keyword):
            return query.replace(keyword, "").strip()

# Mensagem de boas-vindas
machine.say("Olá, eu sou a ANA, sua Assistente de Navegação Autônoma")
machine.say("Como posso ajudar?")
machine.runAndWait()

# Loop principal do assistente
while True:
    # Execução da função para ouvir a entrada de voz do usuário
    word = execute()
    print(word)
    
    # Verifica se o usuário quer sair do programa
    if "agora" in word:
        machine.say("Tudo bem, espero que eu seja útil posteriormente.")
        machine.runAndWait()
        break

    # Remove as palavras-chave da consulta para realizar a pesquisa
    query = evaluate(word)

    # Busca na Wikipedia a definição da palavra consultada
    try:
        summary = w.summary(query)
        print(summary)
        machine.say(summary)
    except w.exceptions.DisambiguationError as e:
        # Caso ocorra um erro de ambiguidade, busca pelo primeiro resultado possível
        summary = w.summary(e.options[0])
        print(summary)
        machine.say(summary)
    except w.exceptions.PageError:
        # Caso a página não seja encontrada na Wikipedia
        print("Não foi possível encontrar informações sobre a consulta.")
        machine.say("Não foi possível encontrar informações sobre a consulta.")
    except Exception as ex:
        # Outros erros inesperados
        print("Ocorreu um erro na pesquisa.")
        machine.say("Ocorreu um erro na pesquisa.")

    machine.runAndWait()

    # Pequena pausa antes de perguntar se há algo mais que o assistente possa ajudar
    machine.say("Algo mais que eu possa ajudar?")
    machine.runAndWait()

# Encerra o assistente de voz
sys.exit()
