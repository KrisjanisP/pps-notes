import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLineEdit

class SudokuUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Sudoku")

        # Create the central widget and set it as the main window's central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create the grid layout
        self.grid_layout = QGridLayout(self.central_widget)

        # Add the QLineEdit widgets to the grid layout
        self.line_edits = []
        for row in range(9):
            line_edits_row = []
            for col in range(9):
                line_edit = QLineEdit(self.central_widget)
                line_edit.setMaxLength(1)
                self.grid_layout.addWidget(line_edit, row, col)
                line_edits_row.append(line_edit)
            self.line_edits.append(line_edits_row)

# Create the PySide6 application
app = QApplication(sys.argv)

# Create the sudoku UI and show it
sudoku_ui = SudokuUI()
sudoku_ui.show()

# Run the application
sys.exit(app.exec_())