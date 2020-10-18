

""" todo.py imports the Ui of the software (which is created in  QtCreator),
	and is a simple and basic todo list using QListView. This was just a 
	practic for me to understand the way ListModel interacts with QtWidgets
"""

import sys
import json

from PySide2 import QtWidgets
from PySide2.QtCore import Qt, QAbstractListModel
from PySide2.QtGui import QImage, QKeySequence

from MainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	""" main class of todo list """
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setWindowTitle("Todo App (from Angry Coders)")
		self.setStyleSheet(".QWidget{background-color:khaki}")
		self.setStatusBar(None)

		self.model = TodoModel()
		self.todoView.setModel(self.model)

		self.addButton.clicked.connect(self.add)
		self.addButton.setShortcut(QKeySequence(Qt.Key_Return))

		self.deleteButton.pressed.connect(self.delete)
		self.completeButton.pressed.connect(self.complete)

		self.todoEdit.setFocus()

		self.load()


	def add (self):
		""" when add button clicked """
		text = self.todoEdit.text()
		text = text.strip()
		if text:
			self.model.todos.append((False, text))
			self.model.layoutChanged.emit()
			self.todoEdit.setText("")
			self.todoEdit.setFocus()
			self.save()

	def delete(self):
		""" when delete button clicked """
		indexes = self.todoView.selectedIndexes()
		if indexes:
			index = indexes[0]
			del self.model.todos[index.row()]
			self.model.layoutChanged.emit()
			self.todoView.clearSelection()
			self.todoEdit.setFocus()
			self.save()


	def complete(self):
		""" when complete button clicked = todoList-task is done """
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
			with open("data.json", "r") as f:
				self.model.todos = json.load(f)
		except Exception:
			pass

	def save(self):
		with open("data.json", "w") as f:
			data = json.dump(self.model.todos, f)



class TodoModel(QAbstractListModel):
	""" class for the model of QListView """
	def __init__(self, todos=None):
		QAbstractListModel.__init__(self)
		self.todos = todos or []

		image_not_done = QImage("not_done.png")
		self.not_done = QImage(image_not_done.scaled(18,18, Qt.KeepAspectRatio))

		image_done = QImage("done.png")
		self.done = QImage(image_done.scaled(18,18, Qt.KeepAspectRatio))


	def data(self, index, role):
		""" standard Model method """
		if role == Qt.DisplayRole:
			_, text = self.todos[index.row()]
			return text
		elif role == Qt.DecorationRole:
			status, _ = self.todos[index.row()]
			if not status:
				return self.not_done
			elif status:
				return self.done

	def rowCount(self, index):
		""" standard model method """
		return len(self.todos)


app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")
w = MainWindow()
w.show()
app.exec_()