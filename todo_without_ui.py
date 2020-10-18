
import sys

from PySide2.QtWidgets import (
	QApplication, 
	QMainWindow, QWidget, QListView, QLineEdit,
	QPushButton, 
	QVBoxLayout, QHBoxLayout
	)
from PySide2.QtCore import Qt, QAbstractListModel
from PySide2.QtGui import QImage, QKeySequence

import json

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setWindowTitle("Todo")
		self.setFixedSize(400,600)

		main_layout = QVBoxLayout()

		self.todoView = QListView()
		self.model = TodosModel()
		self.todoView.setModel(self.model)

		hor_layout = QHBoxLayout()

		#>>> button sets
		self.addButton = QPushButton("Add Todo")
		self.addButton.clicked.connect(self.add)
		self.addButton.setShortcut(QKeySequence(Qt.Key_Return))
		
		self.deleteButton = QPushButton("Delete")
		self.deleteButton.clicked.connect(self.delete)
		self.deleteButton.setShortcut(QKeySequence(Qt.Key_Delete))

		self.completeButton = QPushButton ("todo Completed")
		self.completeButton.pressed.connect(self.complete)

		self.todoEdit = QLineEdit()

		#>>> layout management
		main_layout.addWidget(self.todoView)
		hor_layout.addWidget(self.deleteButton)
		hor_layout.addWidget(self.completeButton)
		main_layout.addLayout(hor_layout)
		main_layout.addWidget(self.todoEdit)
		main_layout.addWidget(self.addButton)


		container = QWidget()
		container.setLayout(main_layout)

		self.setCentralWidget(container)
		self.todoEdit.setFocus()
		self.load()


	def add (self):
		text = self.todoEdit.text()
		text = text.split()
		if text:
			self.model.todos.append((False, text))
			self.model.layoutChanged.emit()
			self.todoEdit.setText("")
			self.todoEdit.setFocus()
			self.save()

	def delete(self):
		indexes = self.todoView.selectedIndexes()
		if indexes:
			index = indexes[0]
			del self.model.todos[index.row()]
			self.model.layoutChanged.emit()
			self.todoView.clearSelection()
			self.todoEdit.setFocus()
			self.save()

	def complete (self):
		indexes = self.todoView.selectedIndexes()
		if indexes:
			index = indexes[0]
			row = index.row()
			status, text = self.model.todos[row]
			self.model.todos[row] = (True, text)
			self.model.dataChanged.emit(index, index)
			self.todoView.clearSelection()
			self.todoEdit.setFocus()
			self.save()

	def load(self):
		try:
			with open("data_for_without_ui.json", "r") as f:
				self.model.todos = json.load(f)
		except Exception:
			pass

	def save(self):
		with open("data_for_without_ui.json", "w") as f:
			data = json.dump(self.model.todos, f)




class TodosModel(QAbstractListModel):
	def __init__(self, todos=None):
		QAbstractListModel.__init__(self)
		self.todos = todos or []

		#>>> icon sets
		icon_not_done = QImage("not_done.png")
		self.not_done = QImage(icon_not_done.scaled(18,18))
		icon_done = QImage("done.png")
		self.done = QImage(icon_done.scaled(18,18))

	def data(self, index, role):
		if role == Qt.DisplayRole:
			__, text = self.todos[index.row()]
			return text

		if role == Qt.DecorationRole:
			status, _ = self.todos[index.row()]
			if not status:
				return self.not_done

			if status:
				return self.done

	def rowCount(self, index):
		return len(self.todos)

app = QApplication(sys.argv)
app.setStyle("Fusion")
w = MainWindow()
w.show()
app.exec_()