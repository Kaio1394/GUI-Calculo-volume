import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLineEdit, 
    QFrame, 
    QVBoxLayout, 
    QLabel,
    QPushButton)
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Cáculo do metro cúbico")
        self.setWindowIcon(QIcon("images/vericode.jpg"))
        # self.setFixedSize(300, 200)
        self.txt_altura = QLineEdit()
        self.txt_comprimento = QLineEdit()
        self.txt_largura = QLineEdit()
        self.lbl_resultado = QLabel()
        self.btn = QPushButton("CALCULAR")

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Altura"))
        self.layout.addWidget(self.txt_altura)

        self.layout.addWidget(QLabel("Comprimento"))
        self.layout.addWidget(self.txt_comprimento)

        self.layout.addWidget(QLabel("Largura"))
        self.layout.addWidget(self.txt_largura)

        self.layout.addWidget(self.lbl_resultado)
        # self.layout.addWidget(QLabel)
        self.layout.addWidget(self.btn)
       

        self.container = QFrame()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

        self.btn.clicked.connect(self.calculo)
        


    def calculo(self):
        resultado = str(
            float(self.txt_altura.text())*
            float(self.txt_largura.text())*
            float(self.txt_comprimento.text())
            )
        self.lbl_resultado.setText("O total: " + resultado)


        

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet("QWidget{background-color: brown;}")
    widget = MainWindow()
    widget.show()
    app.exec()
