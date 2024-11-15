from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt


# TODO: maybe actually use pydantic model?
class Path:
    def __init__(
        self,
        tags: list[str],
        api_path: str,
        http_method: str,
        request_schema: str | None = None,
        response_schema: str | None = None,
    ):
        self.tags = tags
        self.api_path = api_path
        self.http_method = http_method
        self.request_schema = request_schema
        self.response_schema = response_schema

    def __repr__(self):
        return f"{self.http_method} {self.api_path}"


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

    def get_person(self, index: QModelIndex):
        if index.isValid():
            return self.paths[index.row()]
        return None

    def add_person(self, path: Path):
        self.beginInsertRows(QModelIndex(), len(self.paths), len(self.paths))
        self.paths.append(path)
        self.endInsertRows()

    def remove_person(self, index: QModelIndex):
        if index.isValid():
            self.beginRemoveRows(QModelIndex(), index.row(), index.row())
            self.paths.pop(index.row())
            self.endRemoveRows()
