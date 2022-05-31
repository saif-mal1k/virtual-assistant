import tempfile

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
            tts = gtts.gTTS(text=text, lang='en', slow=False, lang_check=True)
            # save to tmp file
            tmp = tempfile.NamedTemporaryFile()
            temporaryfilename = tmp.name + '.mp3'
                        
            tts.save(temporaryfilename)
            # play tmp file
            playsound(temporaryfilename)
            # remove tmp file
            tmp.close()

        else:
            # offline text to speech
            engine = pyttsx3.init()
            # set rate and volume
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 1.0)
            engine.say(text)
            engine.runAndWait()

        return True
    except Exception as e:
        print(e)
        return False

# unit testing
if __name__=="__main__":
    speak("आपका नाम क्या है?")
    print(".................................")
    speak("may I help you")