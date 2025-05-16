DEBUG_FILL_STYLE = "background-color: rgba(255, 0, 255, 0.2);"
DEBUG_STYLESHEET = """
    QMainWindow {
        background-color: rgb(255, 255, 255);
    }
    QLabel {
        background-color: rgba(0,0,0, 0.25);
        border: 1px solid rgba(255, 255, 255, 1);
    }
    QPushButton {
        background-color: rgba(255, 0, 255, 0.2);
        border: 1px solid rgba(0, 0, 0, 1);
    }
    QWidget {
        background-color: rgba(255, 0, 255, 0.2);
        border: 1px solid rgba(0, 0, 0, 1);
    }
"""

class Console(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create layout
        layout = QVBoxLayout(self)
        
        # Create scroll area for console output
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        # Create widget to hold text
        self.text_widget = QWidget()
        self.text_layout = QVBoxLayout(self.text_widget)
        
        # Set up text display using label
        self.text_display = QLabel()
        self.text_display.setWordWrap(True)
        self.text_display.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.text_layout.addWidget(self.text_display)
        
        # Add text widget to scroll area
        self.scroll_area.setWidget(self.text_widget)
        
        # Add scroll area to main layout
        layout.addWidget(self.scroll_area)
        
        # Set size policy
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        

__all__ = [
    "DEBUG_FILL_STYLE",
    "DEBUG_STYLESHEET",
]
