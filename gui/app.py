import sys
from color import Color
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QBoxLayout, QVBoxLayout, QPushButton, QWidget
from PySide6.QtGui import QIcon
class MainWindow(QMainWindow):
        def __init__(self):
                super().__init__()
                self._loadUiComponents()
                self._menu_button.clicked.connect(self.expand)
                self.setMinimumSize(400, 300)

        def _loadUiComponents(self):
                self._hlayout = QHBoxLayout()
                self._vlayout = QVBoxLayout()
                self._lframe = QWidget()
                #self._rframe = QWidget()
                self._menu_button = QPushButton('menu')
                self._vlayout.addWidget(self._menu_button)
                self._vlayout.addWidget(Color('yellow'))
                self._vlayout.addWidget(Color('blue'))
                self._vlayout.addWidget(Color('green'))
                self._lframe.setLayout(self._vlayout)
                self._hlayout.addWidget(self._lframe)
                self._hlayout.addWidget(Color('purple'))
                self._lframe.setMinimumWidth(50)
                self._lframe.setMaximumWidth(200)
                #self._rframe.setLayout(self._hlayout)
                frame = QWidget()
                frame.setLayout(self._hlayout)
                self.setCentralWidget(frame)


        def expand(self):
                width = self._lframe.width()
                #print(width)
                if width == 50:
                        new_width = 200
                        #self.ui.MenuButton.setIcon(QIcon("interfaces/icons/arrow-left-44.png"))
                elif width == 200:
                        new_width = 50
                        #self.ui.MenuButton.setIcon(QIcon("interfaces/icons/bars.png"))

                try:
                        self.animacion = QPropertyAnimation(self._lframe, b"maximumWidth")
                        self.animacion.setStartValue(width)
                        self.animacion.setEndValue(new_width)
                        self.animacion.setDuration(350)
                        self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
                        self.animacion.start()
                except:
                        #self.ui.MenuButton.setIcon(QIcon("interfaces/icons/bars.png"))
                        self.animacion.setStartValue(50)
                        self.animacion.setEndValue(50)
                        self.animacion.setDuration(350)
                        self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
                        self.animacion.start()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec())