import logging

from app.ui.main_widget_ui import Ui_MainWidget
from app.widgets.generate_yaml import GenerateYAML
from app.widgets.schema_manager import SchemaManager
from PyQt6.QtWidgets import QWidget


class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.generate_yaml_window = GenerateYAML()
        self.manage_schemas_btn.clicked.connect(self.on_click_manage_schemas)

        self.schema_manager_window = SchemaManager()

        # Setting initial schemas
        self.request_schema_combo.addItems(
            self.schema_manager_window.parser.get_all_types_list()
        )
        self.response_combo.addItems(
            self.schema_manager_window.parser.get_all_types_list()
        )

        self.generate_yaml_btn.clicked.connect(self.on_click_generate_yaml)

        logging.debug("Widget '%s' has initialized", self.__class__.__name__)

    def on_click_generate_yaml(self):
        # TODO: actually implement some logic
        self.generate_yaml_window.show()

    def on_click_manage_schemas(self):
        self.schema_manager_window.show()
