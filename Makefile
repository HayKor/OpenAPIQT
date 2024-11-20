# Variables
PYTHON=python
PYINSTALLER=pyinstaller
SCRIPT=openapiqt/main.py
OUTPUT_NAME=openapiqt
HIDDEN_IMPORTS=pydantic pydantic.tools PyQt6.QtCore PyQt6.QtWidgets openapiqt.app openapiqt.models openapiqt.settings yaml

# Default target
all: build

# Build target for Linux
build:
	$(PYINSTALLER) --onefile \
		--add-data="openapiqt:." \
		$(foreach import,$(HIDDEN_IMPORTS),--hidden-import=$(import)) \
		--name=$(OUTPUT_NAME) \
		$(SCRIPT)

# Windows command to run to build
# pyinstaller --name="openapiqt" --onefile --add-data="openapiqt:." --hidden-import=pydantic --hidden-import=pydantic.tools --hidden-import=PyQt6.QtCore --hidden-import=PyQt6.QtWidgets --hidden-import=openapiqt.app --hidden-import=openapiqt.models --hidden-import=openapiqt.settings --hidden-import=yaml --windowed --noconsole openapiqt\main.py

# Clean target
clean:
	$(PYINSTALLER) --clean

# Run target
run: build
	./dist/$(OUTPUT_NAME)

.PHONY: all build clean run
