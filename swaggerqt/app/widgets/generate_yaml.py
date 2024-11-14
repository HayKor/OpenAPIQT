import logging

from app.ui.generated_yaml_ui import Ui_GenerateYAML
from PyQt6.QtWidgets import QWidget


class GenerateYAML(QWidget, Ui_GenerateYAML):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        logging.debug("Widget '%s' has initialized", self.__class__.__name__)
