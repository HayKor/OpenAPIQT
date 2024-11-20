import logging

import yaml
from app.ui.main_widget_ui import Ui_MainWidget
from app.widgets.generate_yaml import GenerateYAML
from app.widgets.schema_manager import SchemaManager
from models.paths import Path
from pydantic import ValidationError
from PyQt6.QtWidgets import QMessageBox, QWidget


class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # YAML generator window
        self.generate_yaml_window = GenerateYAML()
        self.generate_yaml_btn.clicked.connect(self.on_click_generate_yaml)

        # Schema Manager window
        self.schema_manager_window = SchemaManager()
        self.manage_schemas_btn.clicked.connect(self.on_click_manage_schemas)

        # Setting initial models
        self.request_schema_combo.setModel(
            self.schema_manager_window.schemas_model
        )
        self.response_combo.setModel(self.schema_manager_window.schemas_model)

        #
        self.add_path_btn.clicked.connect(self.on_click_add_path)
        self.delete_path_btn.clicked.connect(self.on_click_delete_path)

        logging.debug("Widget '%s' has initialized", self.__class__.__name__)

    def on_click_generate_yaml(self, yaml: str):
        self.generate_swagger_yaml()

        self.generate_yaml_window.show()

    def on_click_manage_schemas(self):
        self.schema_manager_window.show()

    def clear_inputs(self):
        self.api_path_input.clear()
        self.tag_input.clear()
        self.response_input.clear()

    def on_click_add_path(self):
        api_path = self.api_path_input.text()
        tags = self.tag_input.text()
        http_method = self.http_method_combo.currentText()
        request_schema = self.request_schema_combo.currentText()
        response_schema = self.response_combo.currentText()
        if not request_schema or not response_schema:
            QMessageBox.warning(
                self,
                "Schema Error",
                "Please choose a valid schema or make one.",
            )
            return
        try:
            path = Path(
                tags=[tag.strip() for tag in tags.split(",")],
                api_path=api_path,
                http_method=http_method,
                request_schema=request_schema,
                response_schema=response_schema,
            )
            self.paths_model.add_path(path)
            self.clear_inputs()
            logging.debug("Added new path: %s", path)

        except ValidationError:
            QMessageBox.warning(
                self, "Input Error", "Please enter a valid path properties."
            )

    def on_click_delete_path(self):
        selected_indexes = self.path_list.selectedIndexes()
        if selected_indexes:
            self.paths_model.remove_path(selected_indexes[0])
        else:
            QMessageBox.warning(
                self, "No Selection", "Please select a path to remove."
            )

    def generate_swagger_yaml(self):
        try:
            # Create base Swagger/OpenAPI structure
            swagger_dict = {
                "openapi": "3.0.0",
                "info": {
                    "title": self.title_input.text() or "My API",
                    "version": "1.0.0",
                    "description": "",
                },
                "paths": {},
                "components": {"schemas": {}},
            }

            # Add Paths
            for path in self.paths_model.paths:
                path_dict = {
                    path.http_method.lower(): {
                        "tags": path.tags,
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": f"#/components/schemas/{path.request_schema}"
                                    }
                                }
                            }
                        },
                        "responses": {
                            "200": {
                                "description": "Successful response",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": f"#/components/schemas/{path.response_schema}"
                                        }
                                    }
                                },
                            }
                        },
                    }
                }
                swagger_dict["paths"][path.api_path] = path_dict
                logging.debug(
                    "Added new path to Generate YAML window: %s", path.api_path
                )

            # Add Schemas
            for schema_name in self.schema_manager_window.schemas_model.schemas:
                schema = self.schema_manager_window.parser.get_json_schema(
                    schema_name
                )
                if schema:
                    swagger_dict["components"]["schemas"][schema_name] = schema

                    logging.debug(
                        "Added new schema to GenerateYAML: %s", schema_name
                    )

            # Convert to YAML
            self.swagger_yaml = yaml.dump(
                swagger_dict,
                default_flow_style=False,
                sort_keys=False,
                indent=2,
            )

            # Display YAML in text area
            self.generate_yaml_window.plainTextEdit.setPlainText(
                self.swagger_yaml
            )

            return swagger_dict

        except Exception as e:
            QMessageBox.warning(
                self,
                "YAML Generation Error",
                f"Failed to generate YAML: {str(e)}",
            )
            logging.error(f"YAML generation error: {e}")
            return None
