import pyttsx3
import PyPDF2
from gtts import gTTS

file_name = 'pdf_file_name' ## write the pdf file name
book = open('file_name', 'rb')  #open oop book and encoding format read binary
pdfReader = PyPDF2.PdfFileReader(book) #Creates reader object that stores data of book
pages = pdfReader.numPages #gives number of pages of book
speaker = pyttsx3.init() #initialising text to speech
page_no =    #enter the page number you want to listen
page = pdfReader.getPage(page_no) #storing page 8 in 'page'
tex = page.extractText() #extracts the text on the page
voices = speaker.getProperty('voices') #stores the supported voices(male or female)
speaker.setProperty('voice',voices[0].id) #setting in which voice you want to listen

speaker.say(tex) #starts speaking
speaker.runAndWait()  #waits until the speaking is over

### Saves a audio file 
want_to_save_audio =  1 # enter 0 or 1
if (want_to_save_audio == 1):
  tts = gTTS(text=tex,lang='en') #saves in audio format of text in page 8
  tts.save("saved_file.mp3")  #stores with name saved_file

