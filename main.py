import wikipedia as w
import speech_recognition as sr
import pyttsx3
import sys
import time as t

# Keywords for speech recognition
keywords = ["define", "definition", "what is", "who is", "search for", "explain", "tell me about", "who was"]
# Set language to English for Wikipedia
w.set_lang("en")

# Initialize speech recognition, text-to-speech, and Wikipedia
audio = sr.Recognizer()
machine = pyttsx3.init()
machine.say("Hello, I am Hawking, your Autonomous Navigation Assistant")
machine.say("How can I help you?")
machine.runAndWait()

def execute():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio.adjust_for_ambient_noise(source, duration=1)
            voz = audio.listen(source, timeout=5)
            command = audio.recognize_google(voz, language="en-US")
            command = command.lower()
            return command
    except sr.UnknownValueError:
        machine.say("Sorry, I couldn't understand. Please try again.")
        machine.runAndWait()
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def evaluate(query):
    for keyword in keywords:
        if keyword in query:
            return query.replace(keyword, "").strip()
    return query  # Return the original query if no keyword is found

while True:
    word = execute()
    if word is None:
        continue

    print("Query:", word)
    if "stop" in word:
        machine.say("Alright, I hope I can assist you later.")
        machine.runAndWait()
        break

    query_result = evaluate(word)
    print("Processed Query:", query_result)

    try:
        result = w.summary(query_result)
        print("Wikipedia Summary:", result)
        machine.say(result)
    except w.DisambiguationError as e:
        print("Disambiguation Error:", e.options)
        machine.say(f"Multiple options found. Please specify your query.")
    except w.PageError as e:
        print("Page Error:", e)
        machine.say(f"Sorry, I couldn't find information about {query_result}.")

    machine.runAndWait()

    t.sleep(2)
    machine.say("Is there anything else I can help you with?")
    machine.runAndWait()

sys.exit()
