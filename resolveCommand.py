import urllib3   # i need to cheange it but, right now making its use to check internet

# wikipedia
import wikipedia 

# wiki how
import whapi

import textToSpeech



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
        sumry = wikipedia.summary(query, sentences=3)
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
        return None
    else:
        pass

    if "what" in command or "where" in command or "who" in command:
        output = find_on_wikipedia(command)
        return output


    elif "how" in command or "how to" in command:
        output = find_on_wikihow(command)
        pass



if __name__ == "__main__":
    print(find_on_wikipedia("what is a computer"))
    print(find_on_wikipedia("where is the Eiffel Tower"))
    print(find_on_wikipedia("who is the president of the United States"))
    print(find_on_wikihow("how to become a pilot"))
    

