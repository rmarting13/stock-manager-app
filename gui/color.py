from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget

class Color(QWidget):
    def __init__(self, value_color):
        super().__init__()
        self.setAutoFillBackground(True)
        color_palette = self.palette()
        color_palette.setColor(QPalette.Window, QColor(value_color))
        self.setPalette(color_palette)