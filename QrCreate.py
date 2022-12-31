import qrcode
from PIL import Image
import os

pathQrs = os.path.join(os.getcwd(),"Qrs")
pathTemplates = os.path.join(os.getcwd(),"templates")
pathPdf = os.path.join(os.getcwd(),"Tickets")

def start():
    while True:
        ticket = input("g: GENERAL\nv: VIP\nm:MEET&GREET\n>> ")
        if ticket == "g":
            createFile("PLANTILLAGENERALFRENTE.PNG")
        elif ticket == "v":
            createFile("PLANTILLAVIPFRENTE.PNG")
        elif ticket == "m":
            createFile("PLANNTILLAMANGFRENTE.PNG")
        else:
            print("ERROR DE TICKET")
            break

def createFile(category):
    while True:
        qr = input("INGRESE CEDULA: ")
        if qr == "otro":
            break
        createQR(qr)
        addImage(category, qr)

def createQR(id):
    img = qrcode.make(id)
    img.save(f"{pathQrs}/{id}.png")

def addImage(category, id):
    template = Image.open(f"{pathTemplates}\\{category}")
    QrId = Image.open(f"{pathQrs}\\{id}.png").resize((745,745))
    template.paste(QrId,(4350,440))
    template.show()
    name = input("INGRESE EL NOMBRE: ")
    template.save(f"{pathPdf}\\{name}{id}.pdf")

def setTempalte():
    im1 = Image.open(f"{pathTemplates}\\PLANTILLAGENERALFRENTE.PNG")
    im2 = Image.open(f"{pathQrs}\\LA-ETNIA-527.png").resize((745,745))
    im1.paste(im2,(4350,440))
    im1.show()

if __name__=="__main__":
    #setTempalte()
    start()
    #createQR("output")