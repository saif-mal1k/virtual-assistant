from textToSpeech import speak
from speechToText import listen_input

import resolveCommand

#very useful especially when you have this module imported in another
if __name__=="__main__":
    try:
        speak("Hello, Sir. How you doing!")
        speak("I am a virtual assistant. may I help you?")

        while(True):
            print("enter command")
            # get command from user and resolve it
            command = listen_input()

            if command == "exit" or command == "okay bye" or command == "ok by":
                speak("Bye Sir. See you soon!")
                break

            output = resolveCommand.resolve_command(command)

            if output == "No internet":
                speak("sorry, please connect me to internet")

            elif output == None:
                speak("I can't understand you. Please try again.")

            elif output == True:
                continue
            else:
                # create a list of all symbols that must be removed from the output
                symbols = ["?","!",":",";","(",")","[","]","{","}","/","\\","^","~","`","|",]

                # remove symbols from output
                for symbol in symbols:
                    output = output.replace(symbol,"")

                # add "\n" after every "." in output
                output = output.replace(".",".\n")

                # create a list of lines in output
                output = output.split("\n")        

                # speak each line in output
                for line in output:
                    print(line)
                    done = speak(line)

    except Exception as e:
        exit()

