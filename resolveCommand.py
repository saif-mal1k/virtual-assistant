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


#check if internet is connected
def internet_check():
    http = urllib3.PoolManager()
    try:
        http.request('GET', 'http://google.com')
        return True
    except:
        return False


# check if command can be resolved by perform math
def check_for_math(command):
    listt = ["calculate", "what is the value of", "value of", "perform", "evaluate", "find the value of", "find"]
    for word in list:
        if word in command:
            return True

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



# follow command passed by main
def resolve_command(command):
    print("me<<: Resolving command: " + command + "...")
    command = command.lower()

    if internet_check() == False:
        print("me<<: No internet connection !!!")
        return "No internet"
    else:
        pass

    if check_for_math(command) == True:
        perform_math.perform(command)

    elif "what" in command or "where" in command or "who" in command:
        output = find_on_wikipedia(command)
        return output

    elif "set a timer for" in command:
        timer.startTimer(command)

    elif "search" in command and "on google" in command:
        webOpen.googleSearch(command)

    elif "download image" in command:
        webOpen.downloadImage(command)

    elif "play" in command and ("youtube" in command or "yt" in command):
        webOpen.youtubeSearch(command)

    elif "open chrome" in command or "open google" in command:
        webOpen.openWebsite()

    elif "how" in command or "how to" in command:
        output = find_on_wikihow(command)
        pass

    elif "open" in command and "website" in command:
        webOpen.openWebsiteByName(command)

    elif "tell" in command and "news" in command:
        headlines = webOpen.latestNews()
        for news in headlines:
            print(news)
            textToSpeech.speak(news)


    elif "exit" in command or "okay bye" in command:
        exit()
    
    else:
        webOpen.handleQuery(command)




if __name__ == "__main__":
    #print(resolve_command("what is 1 plus 1"))
    print(resolve_command("tell me latest news"))
    #print(find_on_wikipedia("what is a computer"))
    #print(find_on_wikipedia("where is the Eiffel Tower"))
    #print(find_on_wikipedia("who is the president of the United States"))
    #print(find_on_wikihow("how to become a pilot"))
    

