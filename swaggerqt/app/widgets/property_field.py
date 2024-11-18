from typing import Any, Callable

from PyQt6.QtCore import QAbstractListModel
from PyQt6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QWidget,
)


class PropertyField(QWidget):
    def __init__(self, remove_callback: Callable, model: QAbstractListModel):
        super().__init__()

        # Create layout for the property field
        layout = QHBoxLayout()

        # Create input fields for property name and type
        self.property_name_input = QLineEdit()
        self.property_type_combo = QComboBox()
        self.is_required_checkbox = QCheckBox("*")
        self.destroy_btn = QPushButton("X")

        #
        self.destroy_btn.setFixedSize(20, 20)

        # Set placeholder text
        self.property_name_input.setPlaceholderText("Property Name")
        self.property_type_combo.setModel(model)

        self.destroy_btn.clicked.connect(remove_callback)

        # Add inputs to layout
        layout.addWidget(self.property_name_input)
        layout.addWidget(self.property_type_combo)
        layout.addWidget(self.is_required_checkbox)
        layout.addWidget(self.destroy_btn)

        self.setLayout(layout)

    def get_property_fields(self) -> dict[str, Any]:
        return {
            "name": self.property_name_input.text(),
            "type": self.property_type_combo.currentText(),
            "is_required": self.is_required_checkbox.isChecked(),
        }
