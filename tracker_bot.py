import requests
from bs4 import BeautifulSoup
from emoji import emojize
from gtts import gTTS
from playsound import playsound
from speech_recognition import *
from os import *
import webbrowser
url='https://www.amazon.in/Fossil-Touchscreen-Smartwatch-Notifications-FTW4025/dp/B07SRW3MCM/ref=sr_1_2?crid=2GD7W1RUOXPQ&dchild=1&keywords=fossil+gen+5+smartwatch&qid=1613832023&sprefix=foss%2Caps%2C347&sr=8-2'
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
def track():
    code=requests.get(url,headers=headers).text
    soup=BeautifulSoup(code,'html.parser')
    track_cost=soup.find(id='priceblock_ourprice').get_text()
    cost=track_cost.split()[1].split(',')
    diff_cost=float(''.join(cost))
    ab=soup.find(id='availability')
    availability=ab.span.get_text().strip()
    return [diff_cost,availability,track_cost]
def stats(text):
        status=gTTS(text=text,lang='en')
        status.save('stats.mp3')
        playsound('stats.mp3')
        remove('stats.mp3')
def response():
    r=Recognizer()
    said=''
    with Microphone() as source:
        audio=r.listen(source,phrase_time_limit=5)
        try:
            said=r.recognize_google(audio)
        except Exception:
            said='Error.There is a Problem With Your Microphone.'
    return said
def open(respo):
    if respo.lower()=='yes':
        webbrowser.open(url)
    else:
        pass
    
def notify():
    x,y,z=track()
    vary=0.9*x
    if y=='In stock.' and x<=vary:
        print(f'-----{emojize(":star-struck:")}!Yes There is an offer today-----')
        stats('Your Item is having an Offer Today.')
        stats('Would You Like To Buy Now?')
        print(z)
        said=response()
        open(said)
    else:
        print(f"-----We are very sorry.There is no offer today on your item-----")
        print(z)
        stats('we are so sorry today there is no offer on your item.we will let you know')
notify()    