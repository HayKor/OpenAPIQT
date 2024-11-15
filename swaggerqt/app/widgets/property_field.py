from typing import Any, Callable

from PyQt6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QWidget,
)


class PropertyField(QWidget):
    def __init__(self, remove_callback: Callable):
        super().__init__()

        # Create layout for the property field
        layout = QHBoxLayout()

        # Create input fields for property name and type
        self.property_name_input = QLineEdit()
        self.property_type_input = QLineEdit()
        self.is_required_checkbox = QCheckBox("*")
        self.destroy_btn = QPushButton("X")

        #
        self.destroy_btn.setFixedSize(20, 20)

        # Set placeholder text
        self.property_name_input.setPlaceholderText("Property Name")
        self.property_type_input.setPlaceholderText("Property Type")

        self.destroy_btn.clicked.connect(remove_callback)

        # Add inputs to layout
        layout.addWidget(self.property_name_input)
        layout.addWidget(self.property_type_input)
        layout.addWidget(self.is_required_checkbox)
        layout.addWidget(self.destroy_btn)

        self.setLayout(layout)

    def get_property_fields(self) -> dict[str, Any]:
        return {
            "property_name": self.property_name_input.text(),
            "property_type": self.property_type_input.text(),
            "is_required": self.is_required_checkbox.isChecked(),
        }
