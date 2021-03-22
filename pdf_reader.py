#Librerias a utilizar
import pyttsx3
import PyPDF2 as pypdf

class Lector_Mike():
    def __init__(self, pdf, pagina: int):
        self.pdf = open(pdf,"rb")
        self.pagina = pagina
    def leer_Pdf(self):
        leer = pypdf.PdfFileReader(self.pdf)
        paginas_pdf = leer.numPages

        mike = pyttsx3.init()
        pagina_leer= leer.getPage(self.pagina)
        texto = pagina_leer.extractText()
        voices = mike.getProperty('voices')
        mike.setProperty('voice', voices[1].id)
        mike.say(texto)
        mike.runAndWait()

