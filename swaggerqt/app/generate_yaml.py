import logging

from app.ui.generated_yaml_ui import Ui_GenerateYAML
from PyQt6.QtWidgets import QWidget


class GenerateYAML(QWidget, Ui_GenerateYAML):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        logging.debug("Window '%s' has initialized", self.__class__.__name__)
