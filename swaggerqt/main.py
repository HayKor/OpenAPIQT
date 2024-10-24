import logging
import sys

from app.main_window import MainWindow
from PyQt6.QtWidgets import QApplication
from settings import configure_logging, except_hook


def main():
    configure_logging(level=logging.DEBUG)

    app = QApplication(sys.argv)
    main_window = MainWindow()

    logging.info("App started")

    main_window.show()

    sys.excepthook = except_hook

    exit_code = app.exec()
    logging.info("App exited with code %s", exit_code)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
