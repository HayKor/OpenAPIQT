import logging

from app.generate_yaml import GenerateYAML
from app.ui.main_window_ui import Ui_MainWindow
from models.parsing import JsonParser
from PyQt6.QtWidgets import QWidget


class MainWindow(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.parser = JsonParser()
        self.generate_yaml_window = GenerateYAML()
        self.generate_yaml_btn.clicked.connect(self.on_click_generate_yaml)

        logging.debug("Window '%s' has initialized", self.__class__.__name__)

    def on_click_generate_yaml(self):
        self.generate_yaml_window.show()
