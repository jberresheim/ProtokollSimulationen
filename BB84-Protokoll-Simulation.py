# importing libraries
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

#Schnelligkeit der Simulation setzen
animationSpeed = 1500

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #Titel für das Fenster
        self.setWindowTitle("BB84 Protokoll")
        #Geometrie des Fensters setzen
        self.setGeometry(500, 100, 1000, 515) #(x-Achsee, y-Achse, Länge, Höhe)

        #Wenn Animation nicht läuft = False, damit während der Animation nichts verändert werden kann
        self.isAnimationRunning = False
        self.bobStateColor = 'lightGray'

        #Schrift Alice erstellen
        self.aliceLabel = QLabel('Alice', self)
        self.aliceLabel.setFont(QFont('Arial', 30))
        self.aliceLabel.setGeometry(120, 10, 200, 90)

        #Schrift Bob erstellen
        self.bobLabel = QLabel('Bob', self)
        self.bobLabel.setFont(QFont('Arial', 30))
        self.bobLabel.setGeometry(775, 10, 200, 90)

        #Schrift Zufallsbits a von Alice erstellen
        self.aStateLabel = QLabel('a', self)
        self.aStateLabel.setFont(QFont('Arial', 15))
        self.aStateLabel.setGeometry(115, 100, 160, 40)

        #Schrift Zufallsbits a' von Alice erstellen
        self.aBaseLabel = QLabel("a'", self)
        self.aBaseLabel.setFont(QFont('Arial', 15))
        self.aBaseLabel.setGeometry(215, 100, 500, 40)

        #Schrift Zufallsbits b' von Bob erstellen
        self.bBaseLabel = QLabel("b'", self)
        self.bBaseLabel.setFont(QFont('Arial', 15))
        self.bBaseLabel.setGeometry(765, 100, 500, 40)

        #Schrift Bits b von Bob erstellen
        self.bStateLabel = QLabel("b", self)
        self.bStateLabel.setFont(QFont('Arial', 15))
        self.bStateLabel.setGeometry(865, 100, 160, 40)

        #Schrift Schlüsselbit erstellen
        self.keyLabel = QLabel('Schlüsselbit', self)
        self.keyLabel.setFont(QFont('Arial', 15))
        self.keyLabel.setGeometry(370, 420, 300, 40)

        #Schrift Quantenkanal erstellen
        self.quantumLabel = QLabel('Quantenkanal', self)
        self.quantumLabel.setFont(QFont('Arial', 10))
        self.quantumLabel.setGeometry(425, 210, 300, 40)
        #horizontale Linie für den Quantenkanal erstellen
        self.quantumchannel = QFrame(self)
        self.quantumchannel.setGeometry(280, 200, 440, 20)
        self.quantumchannel.setFrameShadow(QFrame.Plain)
        self.quantumchannel.setLineWidth(3)
        self.quantumchannel.setFrameShape(QFrame.HLine)

        #Schrift klassischer Kanal erstellen
        self.classicalLabel = QLabel('klassischer Kanal', self)
        self.classicalLabel.setFont(QFont('Arial', 10))
        self.classicalLabel.setGeometry(410, 360, 300, 40)
        #horizontale Linie für klassischen kanal erstellen
        self.classicalChannel = QFrame(self)
        self.classicalChannel.setGeometry(280, 350, 440, 20)
        self.classicalChannel.setFrameShadow(QFrame.Plain)
        self.classicalChannel.setLineWidth(1)
        self.classicalChannel.setFrameShape(QFrame.HLine)

        #Schrift a'=b'? über dem klassischen Kanal erstellen
        self.compareLabel = QLabel("a' = b' ?", self)
        self.compareLabel.setFont(QFont('Arial', 10))
        self.compareLabel.setGeometry(460, 300, 300, 40)

        #horizontale Linie für Seperation von Protokoll und Legende erstellen
        self.seperation = QFrame(self)
        self.seperation.setGeometry(0, 510, 1000, 20)
        self.seperation.setFrameShadow(QFrame.Sunken)
        self.seperation.setLineWidth(3)
        self.seperation.setFrameShape(QFrame.HLine)

        #Legende erstellen
        #Entscheidungsbaum
        self.Basenbit = QLabel("a'", self)
        self.Basenbit.setGeometry(135, 550, 60, 30)
        self.Basenbit.setFrameShape(QFrame.Box)
        self.Basenbit.setLayoutDirection(Qt.LeftToRight)
        self.Basenbit.setAlignment(Qt.AlignCenter)
        self.Basenbit.setObjectName("Basenbit")

        #Linien erstellen, um Entscheidungsbaum zu visualisieren
        self.line1 = QFrame(self)
        self.line1.setGeometry(80, 555, 55, 20)
        self.line1.setFrameShadow(QFrame.Plain)
        self.line1.setLineWidth(1)
        self.line1.setFrameShape(QFrame.HLine)
        self.line11 = QFrame(self)
        self.line11.setGeometry(50, 565, 60, 50)
        self.line11.setFrameShadow(QFrame.Plain)
        self.line11.setLineWidth(1)
        self.line11.setFrameShape(QFrame.VLine)
        self.line2 = QFrame(self)
        self.line2.setGeometry(195, 555, 55, 20)
        self.line2.setFrameShadow(QFrame.Plain)
        self.line2.setLineWidth(1)
        self.line2.setFrameShape(QFrame.HLine)
        self.line21 = QFrame(self)
        self.line21.setGeometry(220, 565, 60, 50)
        self.line21.setFrameShadow(QFrame.Plain)
        self.line21.setLineWidth(1)
        self.line21.setFrameShape(QFrame.VLine)

        self.InBasisBit = QLabel("a", self)
        self.InBasisBit.setGeometry(135, 690, 60, 30)
        self.InBasisBit.setLayoutDirection(Qt.LeftToRight)
        self.InBasisBit.setFrameShape(QFrame.Box)
        self.InBasisBit.setAlignment(Qt.AlignCenter)
        self.InBasisBit.setObjectName("InBasisBit")

        self.BitZero = QLabel("0", self)
        self.BitZero.setGeometry(55, 610, 50, 50)
        self.BitZero.setLayoutDirection(Qt.LeftToRight)
        self.BitZero.setFrameShape(QFrame.Box)
        self.BitZero.setAlignment(Qt.AlignCenter)
        self.BitZero.setObjectName("BitZero")
        #Linie für Entscheidungsbaum
        self.BitZeroLine = QFrame(self)
        self.BitZeroLine.setGeometry(35, 660, 50, 100)
        self.BitZeroLine.setFrameShadow(QFrame.Plain)
        self.BitZeroLine.setLineWidth(1)
        self.BitZeroLine.setFrameShape(QFrame.VLine)
        self.BitZeroLine2 = QFrame(self)
        self.BitZeroLine2.setGeometry(75, 660, 50, 100)
        self.BitZeroLine2.setFrameShadow(QFrame.Plain)
        self.BitZeroLine2.setLineWidth(1)
        self.BitZeroLine2.setFrameShape(QFrame.VLine)

        self.BitZeroIsZero = QLabel("0", self)
        self.BitZeroIsZero.setGeometry(20, 730, 50, 50)
        self.BitZeroIsZero.setLayoutDirection(Qt.LeftToRight)
        self.BitZeroIsZero.setFrameShape(QFrame.Box)
        self.BitZeroIsZero.setAlignment(Qt.AlignCenter)
        self.BitZeroIsZero.setObjectName("BitZeroIsZero")
        #Linie für Entscheidungsbaum
        self.BitZeroIsZeroLine = QFrame(self)
        self.BitZeroIsZeroLine.setGeometry(20, 780, 50, 20)
        self.BitZeroIsZeroLine.setFrameShadow(QFrame.Plain)
        self.BitZeroIsZeroLine.setLineWidth(1)
        self.BitZeroIsZeroLine.setFrameShape(QFrame.VLine)

        self.BitZeroState = QLabel("|0⟩",self)
        self.BitZeroState.setGeometry(20, 790, 50, 50)
        self.BitZeroState.setLayoutDirection(Qt.LeftToRight)
        self.BitZeroState.setFrameShape(QFrame.Box)
        self.BitZeroState.setAlignment(Qt.AlignCenter)
        self.BitZeroState.setObjectName("BitZeroState")

        self.BitZeroIsOne = QLabel("1",self)
        self.BitZeroIsOne.setGeometry(90, 730, 50, 50)
        self.BitZeroIsOne.setLayoutDirection(Qt.LeftToRight)
        self.BitZeroIsOne.setFrameShape(QFrame.Box)
        self.BitZeroIsOne.setAlignment(Qt.AlignCenter)
        self.BitZeroIsOne.setObjectName("BitZeroIsOne")
        #Linie für Entscheidungsbaum
        self.BitZeroIsOneLine = QFrame(self)
        self.BitZeroIsOneLine.setGeometry(90, 780, 50, 20)
        self.BitZeroIsOneLine.setFrameShadow(QFrame.Plain)
        self.BitZeroIsOneLine.setLineWidth(1)
        self.BitZeroIsOneLine.setFrameShape(QFrame.VLine)

        self.BitOneState = QLabel("|1⟩",self)
        self.BitOneState.setGeometry(90, 790, 50, 50)
        self.BitOneState.setLayoutDirection(Qt.LeftToRight)
        self.BitOneState.setFrameShape(QFrame.Box)
        self.BitOneState.setAlignment(Qt.AlignCenter)
        self.BitOneState.setObjectName("BitOneState")

        self.BitOne = QLabel("1", self)
        self.BitOne.setGeometry(225, 610, 50, 50)
        self.BitOne.setLayoutDirection(Qt.LeftToRight)
        self.BitOne.setFrameShape(QFrame.Box)
        self.BitOne.setAlignment(Qt.AlignCenter)
        self.BitOne.setObjectName("BitOne")
        #Linie für Entscheidungsbaum
        self.BitOneLine = QFrame(self)
        self.BitOneLine.setGeometry(205, 660, 50, 100)
        self.BitOneLine.setFrameShadow(QFrame.Plain)
        self.BitOneLine.setLineWidth(1)
        self.BitOneLine.setFrameShape(QFrame.VLine)
        self.BitOneLine2 = QFrame(self)
        self.BitOneLine2.setGeometry(245, 660, 50, 100)
        self.BitOneLine2.setFrameShadow(QFrame.Plain)
        self.BitOneLine2.setLineWidth(1)
        self.BitOneLine2.setFrameShape(QFrame.VLine)

        self.BitOneIsZero = QLabel("0",self)
        self.BitOneIsZero.setGeometry(190, 730, 50, 50)
        self.BitOneIsZero.setLayoutDirection(Qt.LeftToRight)
        self.BitOneIsZero.setFrameShape(QFrame.Box)
        self.BitOneIsZero.setAlignment(Qt.AlignCenter)
        self.BitOneIsZero.setObjectName("BitOneIsZero")
        #Linie für Entscheidungsbaum
        self.BitOneIsZeroLine = QFrame(self)
        self.BitOneIsZeroLine.setGeometry(190, 780, 50, 20)
        self.BitOneIsZeroLine.setFrameShadow(QFrame.Plain)
        self.BitOneIsZeroLine.setLineWidth(1)
        self.BitOneIsZeroLine.setFrameShape(QFrame.VLine)

        self.BitPlusState = QLabel("|+⟩", self)
        self.BitPlusState.setGeometry(190, 790, 50, 50)
        self.BitPlusState.setLayoutDirection(Qt.LeftToRight)
        self.BitPlusState.setFrameShape(QFrame.Box)
        self.BitPlusState.setAlignment(Qt.AlignCenter)
        self.BitPlusState.setObjectName("BitPlusState")

        self.BitOneIsOne = QLabel("1",self)
        self.BitOneIsOne.setGeometry(260, 730, 50, 50)
        self.BitOneIsOne.setLayoutDirection(Qt.LeftToRight)
        self.BitOneIsOne.setFrameShape(QFrame.Box)
        self.BitOneIsOne.setAlignment(Qt.AlignCenter)
        self.BitOneIsOne.setObjectName("BitOneIsOne")
        #Linie für Entscheidungsbaum
        self.BitOneIsOneLine = QFrame(self)
        self.BitOneIsOneLine.setGeometry(260, 780, 50, 20)
        self.BitOneIsOneLine.setFrameShadow(QFrame.Plain)
        self.BitOneIsOneLine.setLineWidth(1)
        self.BitOneIsOneLine.setFrameShape(QFrame.VLine)

        self.BitMinusState = QLabel("|-⟩", self)
        self.BitMinusState.setGeometry(260, 790, 50, 50)
        self.BitMinusState.setLayoutDirection(Qt.LeftToRight)
        self.BitMinusState.setFrameShape(QFrame.Box)
        self.BitMinusState.setAlignment(Qt.AlignCenter)
        self.BitMinusState.setObjectName("BitMinusState")

        #Legende zu den Farben erstellen
        self.pinkLabel = QLabel("Rosa:  ", self)
        self.pinkLabel.setFont(QFont('Arial', 10))
        self.pinkLabel.setGeometry(350, 530, 75, 25)
        self.pinkLabel.setStyleSheet('background-color: pink')
        self.pinkLabelText = QLabel("Standardbasis gewählt, da a' = 0 oder b' = 0.", self)
        self.pinkLabelText.setFont(QFont('Arial', 10))
        self.pinkLabelText.setGeometry(430, 530, 605, 25)

        self.violetLabel = QLabel("Violett: ", self)
        self.violetLabel.setFont(QFont('Arial', 10))
        self.violetLabel.setGeometry(350, 560, 75, 25)
        self.violetLabel.setStyleSheet('background-color: violet')
        self.violetLabelText = QLabel("Hadamardbasis gewählt, da a' = 1 oder b' = 1.", self)
        self.violetLabelText.setFont(QFont('Arial', 10))
        self.violetLabelText.setGeometry(430, 560, 605, 25)

        self.blueLabel = QLabel("Blau: ", self)
        self.blueLabel.setFont(QFont('Arial', 10))
        self.blueLabel.setGeometry(350, 590, 75, 25)
        self.blueLabel.setStyleSheet('background-color: lightblue')
        self.blueLabelText = QLabel("In Standardbasis: a = 0; Qubit wird |0⟩. Bob misst; b = 0.", self)
        self.blueLabelText.setFont(QFont('Arial', 10))
        self.blueLabelText.setGeometry(430, 590, 605, 25)

        self.cyanLabel = QLabel("Cyan: ", self)
        self.cyanLabel.setFont(QFont('Arial', 10))
        self.cyanLabel.setGeometry(350, 620, 75, 25)
        self.cyanLabel.setStyleSheet('background-color: cyan')
        self.cyanLabelText = QLabel("In Standardbasis: a = 1; Qubit wird |1⟩. Bob misst; b = 1.", self)
        self.cyanLabelText.setFont(QFont('Arial', 10))
        self.cyanLabelText.setGeometry(430, 620, 605, 25)

        self.yellowLabel = QLabel("Gelb: ", self)
        self.yellowLabel.setFont(QFont('Arial', 10))
        self.yellowLabel.setGeometry(350, 650, 75, 25)
        self.yellowLabelText = QLabel("In Hadamardbasis: a = 0; Qubit wird |+⟩. Bob misst; b = 0.", self)
        self.yellowLabelText.setFont(QFont('Arial', 10))
        self.yellowLabelText.setGeometry(430, 650, 605, 25)
        self.yellowLabel.setStyleSheet('background-color: yellow')

        self.orangeLabel = QLabel("Orange: ", self)
        self.orangeLabel.setFont(QFont('Arial', 10))
        self.orangeLabel.setGeometry(350, 680, 75, 25)
        self.orangeLabelText = QLabel("In Hadamardbasis: a = 1; Qubit wird |-⟩. Bob misst; b = 1.", self)
        self.orangeLabelText.setFont(QFont('Arial', 10))
        self.orangeLabelText.setGeometry(430, 680, 605, 25)
        self.orangeLabel.setStyleSheet('background-color: orange')

        self.greenLabel = QLabel("Grün: ", self)
        self.greenLabel.setFont(QFont('Arial', 10))
        self.greenLabel.setGeometry(350, 710, 75, 25)
        self.greenLabel.setStyleSheet('background-color: lightgreen')
        self.greenLabelText = QLabel("Alice und Bob wählten gleiche Basis. Es gibt ein Schlüsselbit.", self)
        self.greenLabelText.setFont(QFont('Arial', 10))
        self.greenLabelText.setGeometry(430, 710, 605, 25)

        self.redLabel = QLabel("Rot: ", self)
        self.redLabel.setFont(QFont('Arial', 10))
        self.redLabel.setGeometry(350, 740, 75, 25)
        self.redLabel.setStyleSheet('background-color: red')
        self.redLabelText = QLabel("Alice und Bob wählten unterschiedliche Basen. Bit wird gelöscht.", self)
        self.redLabelText.setFont(QFont('Arial', 10))
        self.redLabelText.setGeometry(430, 740, 605, 25)

        self.aLabel = QLabel("a: ", self)
        self.aLabel.setFont(QFont('Arial', 10))
        self.aLabel.setGeometry(350, 770, 75, 25)
        self.aLabelText = QLabel("Alice' zufälliges Bit für Qubit Kodierung. Auswahl Zustand.", self)
        self.aLabelText.setFont(QFont('Arial', 10))
        self.aLabelText.setGeometry(430, 770, 605, 25)

        self.bLabel = QLabel("b: ", self)
        self.bLabel.setFont(QFont('Arial', 10))
        self.bLabel.setGeometry(350, 800, 75, 25)
        self.bLabelText = QLabel("Bobs Ergebnis nach Qubit-Messung. Z = Zufallssbit.", self)
        self.bLabelText.setFont(QFont('Arial', 10))
        self.bLabelText.setGeometry(430, 800, 605, 25)

        self.aStrichLabel = QLabel("a': ", self)
        self.aStrichLabel.setFont(QFont('Arial', 10))
        self.aStrichLabel.setGeometry(350, 830, 75, 25)
        self.aStrichLabelText = QLabel("Alice' zufälliges Bit für Qubit Kodierung. Auswahl Basis.", self)
        self.aStrichLabelText.setFont(QFont('Arial', 10))
        self.aStrichLabelText.setGeometry(430, 830, 605, 25)

        self.bStrichLabel = QLabel("b': ", self)
        self.bStrichLabel.setFont(QFont('Arial', 10))
        self.bStrichLabel.setGeometry(350, 860, 75, 25)
        self.bStrichLabelText = QLabel("Bobs zufälliges Bit für Qubit Messung. Auswahl Basis.", self)
        self.bStrichLabelText.setFont(QFont('Arial', 10))
        self.bStrichLabelText.setGeometry(430, 860, 605, 25)

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
        self.random.setGeometry(420, 50, 150, 50)
        self.random.clicked.connect(self.createRandomBits)
        self.random.setText("Zufallsbits erstellen")

        #Kästchen Alice Bit a manuell ändern (Zustand auswählen)
        self.aliceState = QPushButton("CLICK", self)
        self.aliceState.setGeometry(100, 150, 50, 50)
        self.aliceState.clicked.connect(self.changeAliceStateBit)
        self.aliceState.setText("1")
        self.aliceState.setStyleSheet('background-color: orange')

        #Kästchen Alice Bit a' manuell ändern (Basis auswählen)
        self.aliceBase = QPushButton("CLICK", self)
        self.aliceBase.setGeometry(200, 150, 50, 50)
        self.aliceBase.clicked.connect(self.changeAliceBaseBit)
        self.aliceBase.setText("1")
        self.aliceBase.setStyleSheet('background-color: violet')

        #Kästchen Senden erstellen
        self.send = QPushButton("CLICK", self)
        self.send.setGeometry(280, 100, 70, 40)
        self.send.clicked.connect(self.runAnimation) #Funktion Animation aufrufen, damit Animation mit Klick startet
        self.send.setText("Senden")

        #Kästchen Alice Basis auf klassischem Kanal kopieren. Visualisiert den Vergleich mit Bob Base
        self.aliceBaseCompare = QPushButton("ClICK", self)
        self.aliceBaseCompare.setGeometry(400, 300, 50, 50)
        self.aliceBaseCompare.setText("1")
        self.aliceBaseCompare.setEnabled(False) #Klicken auf das Kästchen bewirkt nichts
        self.aliceBaseCompare.setVisible(False) #Kästchen soll noch nicht angezeigt werden
        self.aliceBaseCompare.setStyleSheet('color: black;background-color: violet')
        #Starten der Animation Alice Basis Bit wird kopiert und bewegt sich auf den klassischen Kanal
        self.aliceBaseCompareAnimation = QPropertyAnimation(self.aliceBaseCompare, b'pos')
        self.aliceBaseCompareAnimation.setEasingCurve(QEasingCurve.InOutQuad) #Animation Verlauf, beginnt langsam und wird schneller
        self.aliceBaseCompareAnimation.setStartValue(self.aliceBase.pos())
        self.aliceBaseCompareAnimation.setEndValue(self.aliceBaseCompare.pos())
        self.aliceBaseCompareAnimation.setDuration(animationSpeed)

        #Qubit Kästchen erstellen
        self.qubit = QPushButton("CLICK", self)
        self.qubit.setGeometry(260, 150, 50, 50)
        self.qubit.setText("|-⟩")
        self.qubit.setVisible(False)
        self.qubit.setEnabled(False)
        self.qubit.setStyleSheet('color: black; background-color: orange')
        #Starten der Animation Qubit. Qubit fährt von Alice über Quantenkanal an Bob
        self.qubitAnimation = QPropertyAnimation(self.qubit, b'pos')
        self.qubitAnimation.setEasingCurve(QEasingCurve.InOutQuad)
        self.qubitAnimation.setStartValue(self.qubit.pos())
        self.qubitAnimation.setEndValue(QPoint(690, 150))
        self.qubitAnimation.setDuration(animationSpeed)

        #Kästchen Bob Basenbit erstellen PushButton
        self.bobBase = QPushButton("CLICK", self)
        self.bobBase.setGeometry(750, 150, 50, 50)
        self.bobBase.clicked.connect(self.changeBobBaseBit)
        self.bobBase.setText("1")
        self.bobBase.setStyleSheet('background-color: violet')

        #Kästchen Bob Basis auf klassischem Kanal kopieren. Visualisiert den Vergleich mit Alice Base
        self.bobBaseCompare = QPushButton("CLICK", self)
        self.bobBaseCompare.setGeometry(535, 300, 50, 50)
        self.bobBaseCompare.setText("1")
        self.bobBaseCompare.setVisible(False)
        self.bobBaseCompare.setEnabled(False)
        self.bobBaseCompare.setStyleSheet('color: black;background-color: violet')
        #Starten der Animation. Bob Basis Bit wird kopiert und bewegt sich auf den klassischen Kanal
        self.bobBaseCompareAnimation = QPropertyAnimation(self.bobBaseCompare, b'pos')
        self.bobBaseCompareAnimation.setEasingCurve(QEasingCurve.InOutQuad)
        self.bobBaseCompareAnimation.setStartValue(self.bobBase.pos())
        self.bobBaseCompareAnimation.setEndValue(self.bobBaseCompare.pos())
        self.bobBaseCompareAnimation.setDuration(animationSpeed)

        #Kästchen für Bobs gemessenes Bit erstellen
        self.bobState = QPushButton("CLICK", self)
        self.bobState.setGeometry(850, 150, 50, 50)
        self.bobState.setText("1")
        self.bobState.setEnabled(False)
        self.bobState.setVisible(False)
        self.bobStateColor = 'orange'

        #Kästchen für das Schlüsselbit erstellen
        self.key = QPushButton("CLICK", self)
        self.key.setGeometry(550, 410, 50, 50)
        self.key.setText("1")
        self.key.setVisible(False)
        self.key.setEnabled(False)
        self.key.setStyleSheet('color: black;background-color: lightgreen')
        #Schlüsselbit Animation. Bobs Ergebnis bewegt sich zum Schlüsselbit
        self.bobStateToKeyAnimation = QPropertyAnimation(self.key, b'pos')
        self.bobStateToKeyAnimation.setEasingCurve(QEasingCurve.InOutQuad)
        self.bobStateToKeyAnimation.setStartValue(self.bobState.pos())
        self.bobStateToKeyAnimation.setEndValue(self.key.pos())
        self.bobStateToKeyAnimation.setDuration(animationSpeed)

        #"..." Kästchen erstellen, um durch Klicken ganze Schlüsselfolge anzuschauen
        self.fullSequence  = QPushButton("CLICK", self)
        self.fullSequence.clicked.connect(self.displayFullSequence)
        self.fullSequence.setGeometry(60, 480, 30, 30)
        self.fullSequence.setText("...")
        self.fullSequence.setVisible(False) #wird noch nicht angezeigt

        #Kästchen i erstellen, das die Legende durch Klicken öffnet
        self.legende = QPushButton("CLICK", self)
        self.legende.setGeometry(5, 470, 40, 40)
        self.legende.clicked.connect(self.showLegende)
        self.legende.setText("i")

        #Kästchen des Entscheidungsbaums einfärben
        self.BitZero.setStyleSheet('background-color: pink')
        self.BitZeroIsZero.setStyleSheet('background-color: lightblue')
        self.BitZeroIsOne.setStyleSheet('background-color: cyan')
        self.BitZeroState.setStyleSheet('background-color: lightblue')
        self.BitOneState.setStyleSheet('background-color: cyan')
        self.BitOne.setStyleSheet('background-color: violet')
        self.BitOneIsZero.setStyleSheet('background-color: yellow')
        self.BitOneIsOne.setStyleSheet('background-color: orange')
        self.BitPlusState.setStyleSheet('background-color: yellow')
        self.BitMinusState.setStyleSheet('background-color: orange')

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
        #Qubit Animation starten
        self.qubit.setVisible(True)
        self.qubitAnimation.start()
        self.qtWait(self.qubitAnimation.duration())

        self.bobState.setVisible(True) #Bobs gemessenes bit wird sichtbar
        #Animation starten, die Basen vergleicht
        self.aliceBaseCompareAnimation.start()
        self.aliceBaseCompare.setVisible(True)
        self.bobBaseCompareAnimation.start()
        self.bobBaseCompare.setVisible(True)

        #auf Animation warten, die die längste Duration hat
        self.qtWait(max(self.aliceBaseCompareAnimation.duration(), self.bobBaseCompareAnimation.duration()))
        self.bobState.setStyleSheet('color: black; background-color: ' + self.bobStateColor)
        self.bobStateToKeyAnimation.start()
        self.key.setVisible(True)

        self.qtWait(self.bobStateToKeyAnimation.duration())
        self.copyToKeySequence()

        self.isAnimationRunning = False


    isLegendVisible = False
    #Legende anzeigen oder nicht mit Klicken auf den i-Push Button
    def showLegende(self):
        if self.isLegendVisible:
            self.resize(1000, 515)
            self.isLegendVisible = False
        else:
            self.resize(1000, 890)
            self.isLegendVisible = True

    #zufällife Bits erstellen
    def createRandomBits(self):
        if self.isAnimationRunning:
            return

        self.isAnimationRunning = True

        self.resetAnimationParts()
        #während Bits zufällig gesucht werden, ist der Hintergund der Kästchen der Zufallsbits grau und nicht gefärbt
        self.setTextAndColor(self.aliceBase, None, "lightGray")
        self.setTextAndColor(self.aliceState, None, "lightGray")
        self.setTextAndColor(self.bobBase, None, "lightGray")
        #Die zufällige Auswahl wird visualisiert, indem Zahlen flackern, es irgenwann stoppt, wodurch Zufallszahl erstellt ist
        for _ in range(10): #wie lange es flackert
            self.aliceBase.setText(str(random.randint(0, 1)))
            self.aliceState.setText(str(random.randint(0, 1)))
            self.bobBase.setText(str(random.randint(0, 1)))
            self.qtWait(50) #Zeit zwischen dem flackern

        self.update()

        self.isAnimationRunning = False

        self.runAnimation()

    #Text und Farbe der Kästchen erstellen
    def setTextAndColor(self, element, text, color):
        if text is not None: #wenn kein text mitgegeben wird
            element.setText(text)
        if color is not None: #wenn keine Farbe beim Funktionsaufruf dazugegeben wird
            #Bobs Zustand bleibt bis zum Schluss grau, weshalb wir die Farbe hier nun in einer Variable speichern
            if element == self.bobState:
                self.bobStateColor = color
            else:
                element.setStyleSheet('color: black; background-color: ' + color)

    #Funktion, um alle Sachen upzudaten; Farbe und Text von den Kästchen
    def update(self):
        if self.aliceBase.text() == "0":
            self.setTextAndColor(self.aliceBase, None, "pink")
            self.setTextAndColor(self.aliceBaseCompare, "0", "pink")
            # Zustand Bit ist 1 bei default
            if self.aliceState.text() == "1":
                self.setTextAndColor(self.aliceState, None, "cyan")
                self.setTextAndColor(self.qubit, "|1⟩", "cyan")
                if self.bobBase.text() == "0":
                    self.setTextAndColor(self.bobState, "1", "cyan")
                    self.setTextAndColor(self.key, "1", "lightgreen")
                elif self.bobBase.text() == "1":
                    self.setTextAndColor(self.bobState, "Z", "red")
                    self.setTextAndColor(self.key, "Z", "red")

            elif self.aliceState.text() == "0":
                self.setTextAndColor(self.aliceState, None, "lightblue")
                self.setTextAndColor(self.qubit, "|0⟩", "lightblue")
                if self.bobBase.text() == "0":
                    self.setTextAndColor(self.bobState, "0", "lightblue")
                    self.setTextAndColor(self.key, "0", "lightgreen")
                elif self.bobBase.text() == "1":
                    self.setTextAndColor(self.bobState, "Z", "red")
                    self.setTextAndColor(self.key, "Z", "red")
        else:
            self.setTextAndColor(self.aliceBase, None, "violet")
            self.setTextAndColor(self.aliceBaseCompare, "1", "violet")
            if self.aliceState.text() == "1":
                self.setTextAndColor(self.aliceState, None, "orange")
                self.setTextAndColor(self.qubit, "|-⟩", "orange" )
                if self.bobBase.text() == "1":
                    self.setTextAndColor(self.bobState, "1", "orange")
                    self.setTextAndColor(self.key, "1", "lightgreen")
                elif self.bobBase.text() == "0":
                    self.setTextAndColor(self.bobState, "Z", "red")
                    self.setTextAndColor(self.key, "Z", "red")
            elif self.aliceState.text() == "0":
                self.setTextAndColor(self.aliceState, None, "yellow")
                self.setTextAndColor(self.qubit, "|+⟩", "yellow" )
                if self.bobBase.text() == "1":
                    self.setTextAndColor(self.bobState, "0", "yellow")
                    self.setTextAndColor(self.key, "0", "lightgreen")
                elif self.bobBase.text() == "0":
                    self.setTextAndColor(self.bobState, "Z", "red")
                    self.setTextAndColor(self.key, "Z", "red")

        if self.bobBase.text() == "0":
            self.setTextAndColor(self.bobBase, None, "pink")
            self.setTextAndColor(self.bobBaseCompare, "0", "pink")
        else:
            self.setTextAndColor(self.bobBase, None, "violet")
            self.setTextAndColor(self.bobBaseCompare, "1", "violet")

    #Funktion, die durch manuelles Klicken auf Alice a' Bit aufgerufen wird
    #Alice Basis ändert sich dadurch
    def changeAliceBaseBit(self):
        if self.isAnimationRunning:
            return

        self.resetAnimationParts()

        if self.aliceBase.text() == "1":
            self.aliceBase.setText("0")
        else:
            self.aliceBase.setText("1")

        self.update()

    #Funktion, die durch manuelles Klicken auf Alice a Bit aufgerufen wird
    #Alice Zustand Auswahl ändert sich dadurch
    def changeAliceStateBit(self):
        if self.isAnimationRunning:
            return

        self.resetAnimationParts()
        if self.aliceState.text() == "1":
            self.aliceState.setText("0")
        else:
            self.aliceState.setText("1")
        self.update()

    #Funktion, die durch manuelles Klicken auf Bobs a' Bit aufgerufen wird
    #Bobs Basis ändert sich dadurch
    def changeBobBaseBit(self):
        if self.isAnimationRunning:
            return

        self.resetAnimationParts()
        if self.bobBase.text() == "0":
            self.bobBase.setText("1")
        else:
            self.bobBase.setText("0")
        self.update()

    KeyBitsList = []

    #nach Durchlauf der Animation, soll alles wieder auf den Standard gesetzt werden
    def resetAnimationParts(self):
        self.key.setVisible(False)
        self.aliceBaseCompare.setVisible(False)
        self.bobBaseCompare.setVisible(False)
        self.bobState.setVisible(False)
        self.qubit.setVisible(False)
        self.bobState.setStyleSheet('color: black; background-color: lightGray')

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

App = QApplication(sys.argv)
window = Window()
#start der App
sys.exit(App.exec())