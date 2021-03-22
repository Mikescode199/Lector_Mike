#Librerias a utilizar 

import pyttsx3
import PyPFD2 as  pypdf

class Lector_Mike():

    def __init__(pdf, pagina: int):
        self.pdf = open(pdf,"rb")
        self.pagina = pagina

    def leer_Pdf(self):
        mike = pyttsx3.init()
        inicio_pagina = pypdf.PdfFileReader(self.pdf)
        mike.say(inicio_pagina)
        mike.runAndWait()


