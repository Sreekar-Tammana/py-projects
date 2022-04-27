import pyttsx3
import PyPDF2

book = open('ms-17.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
page = pdfreader.getPage(1)
text = page.extractText()
speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()