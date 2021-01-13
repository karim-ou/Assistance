""" Alexa an Assistance do simple tasks"""
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
# Give Alexa a female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    """
create talk function to give Alexa the ability to say whatever the text is
    :param text: depend on the command
    """
    engine.say(text)
    engine.runAndWait()


talk('please enter your name')
name = input('Enter your name here: ')


def take_command():
    """
take the command from the user, and the command will be printed is alexa's in the command
    :return: the command
    """
    with sr.Microphone() as source:
        talk(f'hello {name} what can i do for you')
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)

    return command


def run_alexa():
    """
search i the command for keywords
    """
    command = take_command()
    print(command)
    # if play was in the command then program will play what's after play on youtube.
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    # if time was in the command then  the program tell you what's the current time.
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%H %p')
        print(time)
        talk('Current time is ' + time)
    # if search for was in the command then the program will search in wikipedia for what's after search for.
    elif 'search for' in command:
        something = command.replace('search for', '')
        info = wikipedia.summary(something, 2)
        print(info)
        talk(info)
    # if joke was in the command then the program will tell you a joke
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'good bye' in command:
        talk(f'good bye {name}, happy to help')
        quit()
    elif 'stop' in command:
        quit()
    else:
        talk('please say the command again')


while True:
    # the program will run till you don't give a command or the program didn't understand the command
    run_alexa()
