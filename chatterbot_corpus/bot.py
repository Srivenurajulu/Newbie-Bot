import os
import speech_recognition as sr
from gtts import gTTS
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "newbie-hnpwmn-1c53e8ba348e.json"

import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "newbie-hnpwmn"

x=0
while(x<100):
    print("                                                                                                                                                         ")
    x+=1

print("""\
                         ______   _______  _       _________ _______           _______      _______  _______  _______  _       
                        (  ___ \ (  ___  )( (    /|\__    _/(  ___  )|\     /|(  ____ )     (  ____ \(  ____ \(  ____ \| \    /\\
                        | (   ) )| (   ) ||  \  ( |   )  (  | (   ) || )   ( || (    )|     | (    \/| (    \/| (    \/|  \  / /
                        | (__/ / | |   | ||   \ | |   |  |  | |   | || |   | || (____)|     | |      | (__    | (__    |  (_/ / 
                        |  __ (  | |   | || (\ \) |   |  |  | |   | || |   | ||     __)     | | ____ |  __)   |  __)   |   _ (  
                        | (  \ \ | |   | || | \   |   |  |  | |   | || |   | || (\ (        | | \_  )| (      | (      |  ( \ \ 
                        | )___) )| (___) || )  \  ||\_)  )  | (___) || (___) || ) \ \__     | (___) || (____/\| (____/\|  /  \ \\
                        |/ \___/ (_______)|/    )_)(____/   (_______)(_______)|/   \__/     (_______)(_______/(_______/|_/    \/


                                                         _______________
                                                        < Hacuna, mata! >
                                                         ---------------
                                                               \   ^__^
                                                                \  (oo)\_______
                                                                   (__)\       )\/
                                                                       ||----w | 
                                                                       ||     ||
                                                                                                    
""")
x=0
while(x<10):
    print("                                                                                                                                                         ")
    x+=1


def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result


def fetch_reply(query, session_id):
	response = detect_intent_from_text(query,session_id)
	return response.fulfillment_text

print('         NewBie: Hello geek!! ')

while True:
    request = input('         You   : ')
    if(request=='bye'):
        print('         NewBie: Bye!')
        break
    responses = fetch_reply(request, 1234567890)
    
    myText = responses

    language = 'en'
    
    output = gTTS(text = myText, lang = language, slow=False)

    output.save("output.mp3")

    os.system("start output.mp3")
    print('         NewBie:',responses)


