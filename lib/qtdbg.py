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


__all__ = [
    "DEBUG_FILL_STYLE",
    "DEBUG_STYLESHEET",
]
