import logging
from typing import Any

from app.list_models.schema_list_model import SchemaListModel
from app.ui.schema_manager_ui import Ui_SchemaManager
from app.widgets.property_field import PropertyField
from models.parsing import JsonParser
from PyQt6.QtWidgets import QMessageBox, QWidget


class SchemaManager(QWidget, Ui_SchemaManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        logging.debug("Widget '%s' has initialized", self.__class__.__name__)

        # Init parser
        self.parser = JsonParser()

        # Connect when clicked
        self.add_property_btn.clicked.connect(self.add_property_field)

        #
        self.schemas_model = SchemaListModel(self.parser.get_all_types_list())
        self.schemas_list.setModel(self.schemas_model)

        # Initial field
        self.add_property_field()

        #
        self.add_schema_btn.clicked.connect(self.on_click_add_schema)
        self.delete_schema_btn.clicked.connect(self.on_click_delete_schema)

    def on_click_add_schema(self):
        schema_name = self.schema_name_input.text()
        if not schema_name:
            QMessageBox.warning(
                self,
                "Input Error",
                "Schema must have a name.",
            )
            return
        schema: dict[str, Any] = {
            "type": "object",
            "title": schema_name,
            "properties": {},
            "required": [],
        }

        for i in range(self.property_container.count()):
            property_field = self.property_container.itemAt(i).widget()  # type: ignore
            if isinstance(property_field, PropertyField):
                prop = property_field.get_property_fields()
                prop_name, prop_type, is_required = (
                    prop["name"],
                    prop["type"],
                    prop["is_required"],
                )
                prop_name = prop_name.strip()
                prop_type = prop_type.strip()
                if not prop_name or not prop_type:
                    QMessageBox.warning(
                        self,
                        "Input Error",
                        "All fields must be filled out.",
                    )
                    return
                schema["properties"][prop_name] = {
                    "type": prop_type,
                    "title": prop_name.title(),
                }
                if not is_required:
                    schema["properties"][prop_name]["default"] = None
                else:
                    schema["required"].append(prop_name)

        model = self.parser.parse_json_schema(schema_name, schema)
        self.schemas_model.add_schema(model.__name__)
        self.clear_inputs()

    def on_click_delete_schema(self):
        selected_indexes = self.schemas_list.selectedIndexes()
        if selected_indexes:
            self.schemas_model.remove_schema(selected_indexes[0])
        else:
            QMessageBox.warning(
                self, "No Selection", "Please select a path to remove."
            )

    def add_property_field(self):
        """Add a new property field."""
        property_field = PropertyField(
            remove_callback=self.remove_property_field,
            model=self.schemas_model,
        )
        self.property_container.addWidget(property_field)

    def remove_property_field(self):
        if len(self.property_container) == 2:  # because 1 is frame ig
            return
        sender = self.sender()
        property_field = sender.parent()  # type: ignore
        if isinstance(property_field, QWidget):
            self.property_container.removeWidget(property_field)
            property_field.deleteLater()

    def clear_inputs(self):
        self.schema_name_input.clear()
        properties = []

        # Gather propery fields
        for i in range(self.property_container.count()):
            property_field = self.property_container.itemAt(i).widget()  # type: ignore
            properties.append(property_field)

        for property in properties:
            if isinstance(property, QWidget):
                self.property_container.removeWidget(property)
                property.deleteLater()

        # Add one after
        self.add_property_field()
