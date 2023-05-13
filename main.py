from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import time

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("view.ui",self)

        
        self.mother = [self.cbHair_M.currentText(),self.cbEye_M.currentText(),self.cbSkin_M.currentText(),self.cbBlood_M.currentText()]
        self.father = [self.cbHair_F.currentText(),self.cbEye_F.currentText(),self.cbSkin_F.currentText(),self.cbBlood_F.currentText()]
        
        # Father:
        
            #Hair type
        self.currentFhair = self.cbHair_F.currentText()
        self.cbHair_F.currentIndexChanged.connect(self.updateFhair)
            #Eye color
        self.currentFeye = self.cbEye_F.currentText()
        self.cbEye_F.currentIndexChanged.connect(self.updateFeye)
        
            #Skin color
        self.currentFskin = self.cbSkin_F.currentText()
        self.cbSkin_F.currentIndexChanged.connect(self.updateFskin)
        
            #Blood type
        self.currentFblood = self.cbBlood_F.currentText()
        self.cbBlood_F.currentIndexChanged.connect(self.updateFblood)
        #-------------------------------------------------------
        
        # Mother:
        
            #Hair type
        self.currentMhair = self.cbHair_M.currentText()
        self.cbHair_M.currentIndexChanged.connect(self.updateMhair)
            #Eye color
        self.currentMeye = self.cbEye_M.currentText()
        self.cbEye_M.currentIndexChanged.connect(self.updateMeye)
        
            #Skin color
        self.currentMskin = self.cbSkin_M.currentText()
        self.cbSkin_M.currentIndexChanged.connect(self.updateMskin)
        
            #Blood type
        self.currentMblood = self.cbBlood_M.currentText()
        self.cbBlood_M.currentIndexChanged.connect(self.updateMblood)
        #-------------------------------------------------------
        
        # Check Button
        
        self.btnCheck.clicked.connect(self.check)
        
        self.btnClear.clicked.connect(self.clear)
        
        self.child = None
        
    def clear(self):
        self.txtOutput.clear()
        self.txtOutput_number.clear()
        
        
    # father hair update comboBox    
    def updateFhair(self, index):
        self.currentFhair = self.cbHair_F.currentText()
        self.father[0] = self.currentFhair
        
        
    # father eye update comboBox    
    def updateFeye(self, index):
        self.currentFeye = self.cbEye_F.currentText()
        self.father[1] = self.currentFeye
        
    # father skin update comboBox    
    def updateFskin(self, index):
        self.currentFskin = self.cbSkin_F.currentText()
        self.father[2] = self.currentFskin
        
        # father blood update comboBox    
    def updateFblood(self, index):
        self.currentFblood = self.cbBlood_F.currentText()
        self.father[3] = self.currentFblood
    #-----------------------------------------------------------
    
    # mother hair update comboBox    
    def updateMhair(self, index):
        self.currentMhair = self.cbHair_M.currentText()
        self.mother[0] = self.currentMhair
        
    # mother eye update comboBox    
    def updateMeye(self, index):
        self.currentMeye = self.cbEye_M.currentText()
        self.mother[1] = self.currentMeye
        
    # mother skin update comboBox    
    def updateMskin(self, index):
        self.currentMskin = self.cbSkin_M.currentText()
        self.mother[2] = self.currentMskin
        
    # mother blood update comboBox    
    def updateMblood(self, index):
        self.currentMblood = self.cbBlood_M.currentText()
        self.mother[3] = self.currentMblood
    
    #-----------------------------------------------------------
    
    #result function
    
    def check(self):
        self.txtOutput.clear()
        self.child = Child(self.father,self.mother)
        self.child.child.connect(self.append_text)
        self.child.childNum.connect(self.set_text)
        self.child.start()
        
    def append_text(self, text):
        self.txtOutput.appendPlainText(text)
        
        
    def set_text(self, num):
        self.txtOutput_number.setPlainText(num)
        
    def closeEvent(self, event):
        if self.child:
            self.child.terminate()
        super().closeEvent(event)
        
                    
class Child(QThread):
    child = pyqtSignal(str)
    childNum = pyqtSignal(str)

    def __init__(self,father,mother ,parent=None):
        super().__init__(parent)
        self.father = father
        self.mother = mother
        self.children = []

    def run(self):
        result = ""
        for hair in [self.father[0], self.mother[0]]:
            for eye in [self.father[1], self.mother[1]]:
                for skin in [self.father[2], self.mother[2]]:
                    for blood in [self.father[3], self.mother[3]]:
                        child = [hair, eye, skin,blood]
                        if child not in self.children:
                            self.children.append(child)
                        
        for children in self.children:
            result += f"Hair: {children[0]},\nEye: {children[1]},\nSkin: {children[2]}\nBlood: {children[3]}\n"
            result += "----------------------\n"
        self.child.emit(result)
        self.childNum.emit(str(len(self.children)))
        time.sleep(1)    


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()