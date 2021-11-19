import speech_recognition as sr         
import urllib3
import pocketsphinx # used for offline speech recognisition, method called by recognizer instance of speech_recognition had to install it even when speechrecognition is not used

# check internet connection
def internet_on():
    """
    check internet connection
    @return: bool
    """
    try:
        http = urllib3.PoolManager()
        http.request('GET', 'http://www.google.com')
        return True
    except:
        return False


# obtain audio from the microphone
r = sr.Recognizer()

# listens through microphone and returns string
def listen_input():
    """
    listens through microphone returns audio as text string
    @param: NONE
    @return: str
    """
    print("Listening...")
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            if not internet_on():
                # offline mode
                return r.recognize_sphinx(audio)


            if internet_on():
                text = r.recognize_google(audio,language="en-in")
                # name by which audio file will be saved
                fileName = text.replace(" ", "_")
                #save listened audio in speechToText folder in mp3 file with name same as audioToText
                #with open("speechToText/"+fileName+".mp3", "wb") as f:
                #    f.write(audio.get_wav_data())
                # return audioToText
                print(text)  #"You:>> "
                return str(text)
        except Exception as e:
            #print(e)
            #print("\n"+"me<<: pardon, please...")
            return "NONE"


