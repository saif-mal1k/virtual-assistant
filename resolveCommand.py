from os import system
from requests import head
import urllib3   # i need to cheange it but, right now making its use to check internet

# wikipedia search person, place or thing
import wikipedia 

# wiki how to perform certain task or activity
import whapi

import textToSpeech


#personally created
import timer
import webOpen
import perform_math
import dictionary
import systemSupport


#check if internet is connected
def internet_check():
    http = urllib3.PoolManager()
    try:
        http.request('GET', 'http://google.com')
        return True
    except:
        return False

# find on wikipedia
def find_on_wikipedia(command):
    try:
        print("me<<: Searching wikipedia for " + command)
    
        # remove "what" or "where" or "who" from command
        command = command.replace("what", "")
        command = command.replace("where", "")
        command = command.replace("who", "")
        command = command.replace("is", "")
    
        query = command
        sumry = wikipedia.summary(query, sentences=1)
        return sumry

    except Exception as e:
            return "NONE"

# find on wiki how
def find_on_wikihow(command):
    try:
        print("me<<: Searching wikihow for " + command)
        # list of articles
        list_of_dict_of_articles = whapi.search(command,max_results=1)
        id = list_of_dict_of_articles[0]['article_id']
        # gettings steps
        steps = whapi.parse_steps(id)
        # introduction = whapi.parse_intro(id)
        # print("me<<: " + introduction)
        # textToSpeech.speak(introduction)
        for step in steps:
            stp = str(step.replace("_"," "))
            textToSpeech.speak(stp)
            print(steps[step]['summary'])
            step_heading = str(steps[step]['summary'])
            textToSpeech.speak(step_heading)
            #step_description = str(steps[step]['description'])
        return True

    except Exception as e:
        return False


def isContain(text, lst):
	for word in lst:
		if word in text:
			return True
	return False


# follow command passed by main
def resolve_command(command):
    print("me<<: Resolving command: " + command + "...")
    command = command.lower()

    # commands that dont require internet connection
    if isContain(command, ["calculate", "what is the value of", "value of", "perform", "evaluate", "find the value of", "find"]):
        output = perform_math.perform(command)
        return output

    elif "set a timer for" in command:
        timer.startTimer(command)

    elif "meaning of" in command:
        command = command.replace("what is the meaning of", "")
        command = command.replace("meaning of", "")
        command = command.replace("tell me the meaning of", "")
        word, meaning, status = dictionary.getMeaning(command)
        return meaning[1]

    elif "what" in command and isContain(command,["time","date", "today", "day", "month"]):
        return systemSupport.resolveCommand(command)

    elif "exit" in command or "okay bye" in command or "go to sleep" in command:
        exit()
    

    # commands that require internet connection

    if internet_check() == False:
        print("me<<: No internet connection !!!")
        return "No internet"

    if isContain(command, ["translate", " to ", "how to say", "how do you say", " in "]):
        text, pronunciation = dictionary.lang_translate(command)
        print(text)
        return pronunciation
    
    
    elif "what" in command or "where" in command or "who" in command:
        output = find_on_wikipedia(command)
        return output

    elif "how" in command or "how to" in command:
        output = find_on_wikihow(command)
        return True

    elif "search" in command and "on google" in command:
        webOpen.googleSearch(command)
        return True

    elif "download" in command and "image" in command:
        webOpen.downloadImage(command)
        return True

    elif "play" in command and ("youtube" in command or "yt" in command):
        webOpen.youtube(command)
        return True

    elif "download" in command and ("video" in command or "youtube" in command or "yt" in command):
        webOpen.downloadVideo(command)
        return True

    elif "open chrome" in command or "open google" in command:
        webOpen.openWebsite()
        return True

    elif "open" in command and "website" in command:
        webOpen.openWebsiteByName(command)
        return True

    elif "tell" in command and "news" in command:
        headlines = webOpen.latestNews()
        for news in headlines:
            print(news)
            textToSpeech.speak(news)

    else:
        webOpen.handleQuery(command)




if __name__ == "__main__":
    #print(resolve_command("what is 1 plus 1"))
    #print(resolve_command("tell me latest news"))
    #print(resolve_command("meaning of mouth"))
    #print(find_on_wikipedia("what is a computer"))
    #print(find_on_wikipedia("where is the Eiffel Tower"))
    #print(find_on_wikipedia("who is the president of the United States"))
    #print(find_on_wikihow("how to become a pilot"))
    #print(resolve_command("translate how are you to hindi"))
    resolve_command('download rainy day short 30 sec animation video from yt')

