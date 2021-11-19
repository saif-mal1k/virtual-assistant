import tempfile
import os
from playsound import playsound


# offline text to speech
import pyttsx3

# online text to speech
import gtts

# check internet connection
import urllib3


# check internet connection
def internet_on():
    try:
        http = urllib3.PoolManager()
        http.request('GET', 'http://google.com')
        return True
    except:
        return False


#text to speech
def speak(text):
    """
    text to speech
    @param text: str
    @return: Bool (True/False)
    """
    # put all of below code in try block
    try:
        # if internet on
        if internet_on():
            # online text to speech
            tts = gtts.gTTS(text=text, lang='en')
            # save to tmp file
            tmp = tempfile.NamedTemporaryFile(delete=False)
            tmp.close()
            tts.save(tmp.name + '.mp3')
            # play tmp file
            playsound(tmp.name + '.mp3')
            # delete tmp file
            os.remove(tmp.name + '.mp3')
        else:
            # offline text to speech
            engine = pyttsx3.init()
            # set rate and volume
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 1.0)
            engine.say(text)
            engine.runAndWait()

        return True
    except:
        return False


if __name__=="__main__":
    speak("hellow, may i help you?")