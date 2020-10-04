import pyttsx3
import PyPDF2
from gtts import gTTS
book = open('oop.pdf', 'rb')  #open oop book and encoding format read binary
pdfReader = PyPDF2.PdfFileReader(book) #Creates reader object that stores data of book
pages = pdfReader.numPages #gives number of pages of book
print(pages)
speaker = pyttsx3.init() #initialising text to speech
page = pdfReader.getPage(8) #storing page 8 in 'page'
tex = page.extractText() #extracts the text on the page
voices = speaker.getProperty('voices') #stores the supported voices(male or female)
speaker.setProperty('voice',voices[0].id) #setting in which voice you want to listen

speaker.say(tex) #starts speaking
speaker.runAndWait()  #waits until the speaking is over
tts = gTTS(text=tex,lang='en') #saves in audio format of text in page 8
tts.save("saved_file.mp3")  #stores with name saved_file

