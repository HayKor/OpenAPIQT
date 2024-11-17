import logging

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

        # # Setting initial schemas
        # self.request_schema_combo.addItems(
        #     self.schema_manager_window.parser.get_all_types_list()
        # )
        # self.response_combo.addItems(
        #     self.schema_manager_window.parser.get_all_types_list()
        # )
        self.request_schema_combo.setModel(
            self.schema_manager_window.schemas_model
        )
        self.response_combo.setModel(self.schema_manager_window.schemas_model)

        #
        self.add_path_btn.clicked.connect(self.on_click_add_path)
        self.delete_path_btn.clicked.connect(self.on_click_delete_path)

        logging.debug("Widget '%s' has initialized", self.__class__.__name__)

    def on_click_generate_yaml(self):
        # TODO: actually implement some logic
        self.generate_yaml_window.show()

    def on_click_manage_schemas(self):
        self.schema_manager_window.show()

    def clear_inputs(self):
        self.api_path_input.clear()
        self.tag_input.clear()
        self.response_input.clear()

    def on_click_add_path(self):
        api_path = self.api_path_input.text()
        tag = self.tag_input.text()
        http_method = self.http_method_combo.currentText()
        request_schema = self.request_schema_combo.currentText()
        response_schema = self.response_combo.currentText()
        try:
            path = Path(
                tags=[tag],
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
