import logging

from app.ui.schema_manager_ui import Ui_SchemaManager
from app.widgets.property_field import PropertyField
from PyQt6.QtWidgets import QWidget


class SchemaManager(QWidget, Ui_SchemaManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        logging.debug("Widget '%s' has initialized", self.__class__.__name__)

        # Initial field
        self.add_property_field()

        # Connect when clicked
        self.add_property_btn.clicked.connect(self.add_property_field)

    def add_property_field(self):
        """Add a new property field."""
        property_field = PropertyField(self.remove_property_field)
        self.property_container.addWidget(property_field)

    def remove_property_field(self):
        if len(self.property_container) == 2:  # because 1 is frame ig
            return
        sender = self.sender()
        property_field = sender.parent()  # type: ignore
        if isinstance(property_field, QWidget):
            self.property_container.removeWidget(property_field)
            property_field.deleteLater()
