# importing libraries
import random
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os

#Schnelligkeit der Simulation setzen
animationSpeed = 2500
animationSpeedKey = 1500

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #Titel für das Fenster erstellen
        self.setWindowTitle("KB02 Protokoll")
        #Geometrie des Fensters setzen
        self.setGeometry(500, 100, 1000, 515) #(x-Achse, y-Achse, Länge, Höhe)

        #Wenn Animation nicht läuft = False, damit während der Animation nichts verändert werden kann
        self.isAnimationRunning = False

        #Schrift Alice erstellen
        self.aliceLabel = QLabel('Alice', self)
        self.aliceLabel.setFont(QFont('Arial', 30))
        self.aliceLabel.setGeometry(120, 10, 200, 90)

        #Schrift Bob erstellen
        self.bobLabel = QLabel('Bob', self)
        self.bobLabel.setFont(QFont('Arial', 30))
        self.bobLabel.setGeometry(775, 10, 200, 90)

        #Schrift Zufallsbits a von Alice erstellen
        self.aKeyBitLabel = QLabel("Schlüsselbit", self)
        self.aKeyBitLabel.setFont(QFont('Arial', 13))
        self.aKeyBitLabel.setGeometry(50, 150, 160, 40)

        #Schrift TQ = Travel Qubit von Bob erstellen
        self.bTravelQubit = QLabel("TQ", self)
        self.bTravelQubit.setFont(QFont('Arial', 13))
        self.bTravelQubit.setGeometry(780, 150, 500, 40)

        #Schrift HQ = Home Qubit von Bob erstellen
        self.bHomeQubit = QLabel("HQ", self)
        self.bHomeQubit.setFont(QFont('Arial', 13))
        self.bHomeQubit.setGeometry(845, 150, 500, 40)

        #Schrift Schlüsselbit Bobs erstellen
        self.keyLabel = QLabel('Schlüsselbit', self)
        self.keyLabel.setFont(QFont('Arial', 15))
        self.keyLabel.setGeometry(620, 400, 300, 40)

        #Schrift Quantenkanal erstellen
        self.quantumLabel = QLabel('Quantenkanal', self)
        self.quantumLabel.setFont(QFont('Arial', 10))
        self.quantumLabel.setGeometry(425, 260, 300, 40)
        #horizontale Linie für den Quantenkanal erstellen
        self.quantumchannel = QFrame(self)
        self.quantumchannel.setGeometry(280, 250, 440, 20)
        self.quantumchannel.setFrameShadow(QFrame.Plain)
        self.quantumchannel.setLineWidth(3)
        self.quantumchannel.setFrameShape(QFrame.HLine)

        #horizontale Linie für Seperation von Protokoll und Legende erstellen
        self.seperation = QFrame(self)
        self.seperation.setGeometry(0, 510, 1000, 20)
        self.seperation.setFrameShadow(QFrame.Sunken)
        self.seperation.setLineWidth(3)
        self.seperation.setFrameShape(QFrame.HLine)

        #Legende erstellen
        self.travelQubitLabel = QLabel("TQ: ", self)
        self.travelQubitLabel.setFont(QFont('Arial', 10))
        self.travelQubitLabel.setGeometry(100, 560, 65, 22)
        self.travelQubitLabelText = QLabel("Travel-Qubit. Teil des Qubit-Paares. Wird über den Quantenkanal gesendet.", self)
        self.travelQubitLabelText.setFont(QFont('Arial', 10))
        self.travelQubitLabelText.setGeometry(170, 560, 800, 22)

        self.homeQubitLabel = QLabel("HQ: ", self)
        self.homeQubitLabel.setFont(QFont('Arial', 10))
        self.homeQubitLabel.setGeometry(100, 590, 65, 22)
        self.homeQubitLabelText = QLabel("Home-Qubit. Teil des Qubit-Paares. Bleibt während des Verfahrens immer bei Bob.", self)
        self.homeQubitLabelText.setFont(QFont('Arial', 10))
        self.homeQubitLabelText.setGeometry(170, 590, 800, 22)

        self.violetLabel = QLabel("Violett: ", self)
        self.violetLabel.setFont(QFont('Arial', 10))
        self.violetLabel.setGeometry(100, 620, 65, 22)
        self.violetLabel.setStyleSheet('background-color: violet')
        self.violetLabelText = QLabel("Das verschränkte Qubit-Paar ist im |\u03C8+⟩ Bell-Zustand. Bit = 0.", self)
        self.violetLabelText.setFont(QFont('Arial', 10))
        self.violetLabelText.setGeometry(170, 620, 605, 22)

        self.blueLabel = QLabel("Blau: ", self)
        self.blueLabel.setFont(QFont('Arial', 10))
        self.blueLabel.setGeometry(100, 650, 65, 22)
        self.blueLabel.setStyleSheet('background-color: lightblue')
        self.blueLabelText = QLabel("Das verschränkte Qubit-Paar ist im |\u03C8-⟩ Bell-Zustand. Bit = 1.", self)
        self.blueLabelText.setFont(QFont('Arial', 10))
        self.blueLabelText.setGeometry(170, 650, 605, 22)

        self.greenLabel = QLabel("Grün: ", self)
        self.greenLabel.setFont(QFont('Arial', 10))
        self.greenLabel.setGeometry(100, 680, 65, 22)
        self.greenLabel.setStyleSheet('background-color: lightgreen')
        self.greenLabelText = QLabel("Die Schlüsselbits stimmen überein.", self)
        self.greenLabelText.setFont(QFont('Arial', 10))
        self.greenLabelText.setGeometry(170, 680, 605, 22)

        #Kästchen für die Schlüsselfolge erstellen, die horizontal am Fenster angeordnet werden
        self.KeySequence = []
        geoKeySequence = QRect(100, 480, 30, 30)
        for i in range(22):
            label = QLabel(self)
            label.setVisible(False)
            label.setGeometry(geoKeySequence)
            label.setFrameShape(QFrame.Box)
            label.setAlignment(Qt.AlignCenter)
            name = "sequenceBit_{}".format(i + 1)
            label.setObjectName(name)
            geoKeySequence.translate(40, 0)
            setattr(self, name, label)
            self.KeySequence.append(label)

        #Methode aufrufen
        self.UiComponents()
        #Widgets anzeigen
        self.show()

    def UiComponents(self):
        #Push Button Kästchen Zufallsbits erstellen, damit Zufallsbits zufällig gewählt werden können
        self.random = QPushButton("CLICK", self)
        self.random.setGeometry(200, 150, 50, 40)
        self.random.clicked.connect(self.createRandomBits)
        self.random.setText("Zufall")

        #Kästchen auf Alice Seite. Enthält Alice Schlüsselbit
        self.aliceKeyBit = QPushButton("CLICK", self)
        self.aliceKeyBit.setGeometry(120, 200, 50, 50)
        self.aliceKeyBit.clicked.connect(self.changeAliceKeyBit) #ruft Funktion auf, die bei Klicken Alice Schlüsselbit ändert
        self.aliceKeyBit.setText("1")

        #Kästchen Senden erstellen (nun auf Bobs seite)
        self.send = QPushButton("CLICK", self)
        self.send.setGeometry(680, 150, 70, 40)
        self.send.clicked.connect(self.runAnimation) #Funktion Animation aufrufen, damit Animation mit Klick startet
        self.send.setText("Senden")

        #Kästchen für das Qubit-Paar erstellen
        #Travel Qubit Kästchen
        self.travelQubit = QPushButton("CLICK", self)
        self.travelQubit.setGeometry(780, 200, 50, 50)
        self.travelQubit.setText("|\u03C8+⟩")
        self.travelQubit.setStyleSheet('background-color: violet')
        #Animation TravelQubit. Qubit fährt von Bobs Seite über den Quantenkanal an Alice
        self.travelQubitAnimation = QPropertyAnimation(self.travelQubit, b'pos')
        self.travelQubitAnimation.setEasingCurve(QEasingCurve.InOutQuad)
        self.travelQubitAnimation.setStartValue(self.travelQubit.pos())
        self.travelQubitAnimation.setEndValue(QPoint(190, 200))
        self.travelQubitAnimation.setDuration(animationSpeed)
        #Alice sendet TQ an Bob zurück
        self.travelQubitAnimationTwo = QPropertyAnimation(self.travelQubit, b'pos')
        self.travelQubitAnimationTwo.setEasingCurve(QEasingCurve.InOutQuad)
        self.travelQubitAnimationTwo.setStartValue(QPoint(190, 200))
        self.travelQubitAnimationTwo.setEndValue(QPoint(780, 200))
        self.travelQubitAnimationTwo.setDuration(animationSpeed)

        #Kästchen Home-Qubit aus Bobs Seite erstellen
        self.homeQubit = QPushButton("CLICK", self)
        self.homeQubit.setGeometry(830, 200, 50, 50)
        self.homeQubit.setText("|\u03C8+⟩")
        self.homeQubit.setStyleSheet('background-color: violet')

        #Kästchen Schlüsselbit erstellen
        self.key = QPushButton("CLICK", self)
        self.key.setGeometry(805, 250, 50, 50)
        self.key.setText("0")
        self.key.setVisible(False)
        self.key.setEnabled(False)
        self.key.setStyleSheet('color: black; background-color: lightgray')
        self.keyBitAnimation = QPropertyAnimation(self.key, b'pos')
        self.keyBitAnimation.setEasingCurve(QEasingCurve.InOutQuad)
        self.keyBitAnimation.setStartValue(self.key.pos())
        self.keyBitAnimation.setEndValue(QPoint(805, 390))
        self.keyBitAnimation.setDuration(animationSpeedKey)

        #"..." Kästchen erstellen, um durch Klicken ganze Schlüsselfolge anzuschauen
        self.fullSequence  = QPushButton("CLICK", self)
        self.fullSequence.clicked.connect(self.displayFullSequence)
        self.fullSequence.setGeometry(60, 480, 30, 30)
        self.fullSequence.setText("...")
        self.fullSequence.setVisible(False)

        #Kästchen i erstellen, das die Legende durch Klicken öffnet
        self.legende = QPushButton("CLICK", self)
        self.legende.setGeometry(5, 470, 40, 40)
        self.legende.clicked.connect(self.showLegende)
        self.legende.setText("i")

    #Funktion erstellen, die wartet bis die Animation beendet ist, bevor eine andere gestartet wird
    def qtWait(self, duration):
        loop = QEventLoop()
        QTimer.singleShot(duration, loop.quit)
        loop.exec_()

    #Animation starten
    def runAnimation(self):
        if self.isAnimationRunning:
            return

        self.isAnimationRunning = True
        self.resetAnimationParts()

        self.travelQubitAnimation.start()
        self.qtWait(self.travelQubitAnimation.duration())
        #Alice Operation, wenn Schlüsselbit = 1 Zustand ändern
        self.update()
        #Alice Animation TQ fährt von Alice zurück an Bob
        self.travelQubitAnimationTwo.start()
        self.qtWait(self.travelQubitAnimationTwo.duration())

        self.key.setVisible(True)
        self.keyBitAnimation.start()
        self.qtWait(self.keyBitAnimation.duration())

        self.setTextAndColor(self.key, None, "lightgreen")
        self.setTextAndColor(self.aliceKeyBit, None, "lightgreen")

        self.copyToKeySequence()

        self.isAnimationRunning = False


    isLegendVisible = False
    #Legende anzeigen oder nicht mit Klicken auf den i-Push Button
    def showLegende(self):
        if self.isLegendVisible:
            self.resize(1000, 515)
            self.isLegendVisible = False
        else:
            self.resize(1000, 750)
            self.isLegendVisible = True

    #zufällige Auswahl, welches Schlüsselbit Alice hat
    def createRandomBits(self):
        if self.isAnimationRunning:
            return

        self.isAnimationRunning = True

        self.resetAnimationParts()
        #während Bits zufällig gesucht werden, ist der Hintergund der Kästchen der Zufallsbits grau und nicht gefärbt
        self.setTextAndColor(self.aliceKeyBit, None, "lightGray")

        #Die zufällige Auswahl wird visualisiert, indem Zahlen flackern, es irgenwann stoppt, wodurch Zufallszahl erstellt ist
        for _ in range(10): #wie lange es flackert
            self.aliceKeyBit.setText(str(random.randint(0, 1)))
            self.qtWait(50) #Zeit zwischen dem flackern

        self.update()

        self.isAnimationRunning = False

        self.runAnimation()

    #Text und Farbe der Kästchen erstellen
    def setTextAndColor(self, element, text, color):
        if text is not None: #wenn kein text mitgegeben wird
            element.setText(text)
        if color is not None: #wenn keine Farbe dazugegeben wird
            element.setStyleSheet('color: black; background-color: ' + color)

    #Funktion, um alle Sachen upzudaten; Farbe und Text von den Kästchen
    def update(self):
        if self.aliceKeyBit.text() == "1":
            self.setTextAndColor(self.travelQubit, "|\u03C8-⟩", "lightblue")
            self.setTextAndColor(self.homeQubit, "|\u03C8-⟩", "lightblue")
            self.setTextAndColor(self.key, "1", None)
        else:
            self.setTextAndColor(self.travelQubit, "|\u03C8+⟩", "violet")
            self.setTextAndColor(self.homeQubit, "|\u03C8+⟩", "violet")
            self.setTextAndColor(self.key, "0", None)

    #Funktion, die durch manuelles Klicken auf Alice Schlüsselbit aufgerufen wird
    def changeAliceKeyBit(self):
        if self.isAnimationRunning:
            return

        self.resetAnimationParts()
        if self.aliceKeyBit.text() == "1":
            self.aliceKeyBit.setText("0")
        else:
            self.aliceKeyBit.setText("1")


    KeyBitsList = []

    #nach Durchlauf der Animation, soll alles wieder auf den Standard gesetzt werden
    def resetAnimationParts(self):
        self.key.setVisible(False)
        self.setTextAndColor(self.homeQubit, "|\u03C8+⟩", "violet")
        self.setTextAndColor(self.travelQubit, "|\u03C8+⟩", "violet")
        self.setTextAndColor(self.aliceKeyBit, None, "lightgray")
        self.key.setStyleSheet('color: black; background-color: lightgray')

    #Schlüsselfolge erstellen
    def copyToKeySequence(self):
        keyBit = self.key.text()
        self.KeyBitsList.append(keyBit)

        for ks in self.KeySequence:
            ks.setVisible(False)

        firstReadPos = max(len(self.KeyBitsList) - len(self.KeySequence), 0)

        for i in range(min(len(self.KeyBitsList), len(self.KeySequence))):
            self.KeySequence[i].setText(self.KeyBitsList[firstReadPos+i]) #Liste der Schlüsselfolge
            self.KeySequence[i].setVisible(True)

        self.fullSequence.setVisible(True)

    #Schlüsselfolge anzeigen
    def displayFullSequence(self):
        self.fullSequenceWindow = FullSequenceWindow(self.KeyBitsList)
        self.fullSequenceWindow.show()

#neues Fenster erstellen, welches gesamte Schlüsselfolge anzeigt
class FullSequenceWindow(QWidget):
    def __init__(self, sequence):
        super().__init__()
        # Titel für Fenster erstellen
        self.setWindowTitle("Schlüsselfolge")
        self.setGeometry(500, 100, 500, 800)

        self.fullSequenceTextBox = QPlainTextEdit(self)
        self.fullSequenceTextBox.setGeometry(10, 10, 480, 780)
        self.fullSequenceTextBox.setPlainText("".join(sequence))
        self.fullSequenceTextBox.setReadOnly(True)

if ("-h" in sys.argv):
    if hasattr(PyQt5.QtCore.Qt, 'AA_EnableHighDpiScaling'):
        PyQt5.QtWidgets.QApplication.setAttribute(PyQt5.QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(PyQt5.QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        PyQt5.QtWidgets.QApplication.setAttribute(PyQt5.QtCore.Qt.AA_UseHighDpiPixmaps, True)
App = QApplication(sys.argv)
window = Window()
#start der App
sys.exit(App.exec())