from models.paths import Path
from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt


# Custom model to hold Person instances
class PathListModel(QAbstractListModel):
    def __init__(self, paths: list[Path] | None = None):
        super().__init__()
        self.paths: list[Path] = paths or []

    def data(self, index: QModelIndex, role: int = ...):
        if role == Qt.ItemDataRole.DisplayRole:
            return repr(self.paths[index.row()])  # Show the name in the list

    def rowCount(self, parent: QModelIndex = ...):
        return len(self.paths)

    def get_path(self, index: QModelIndex):
        if index.isValid():
            return self.paths[index.row()]
        return None

    def add_path(self, path: Path):
        self.beginInsertRows(QModelIndex(), len(self.paths), len(self.paths))
        self.paths.append(path)
        self.endInsertRows()

    def remove_path(self, index: QModelIndex):
        if index.isValid():
            self.beginRemoveRows(QModelIndex(), index.row(), index.row())
            self.paths.pop(index.row())
            self.endRemoveRows()
