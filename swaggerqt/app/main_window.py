import logging

from models.parsing import JsonParser
from PyQt6.QtWidgets import QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQT")
        self.parser = JsonParser()

        self.init_ui()
        logging.debug("Window '%s' has initialized", self.__class__.__name__)

    def init_ui(self):
        pass
