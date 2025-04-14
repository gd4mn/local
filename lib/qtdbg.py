import datetime
import sys
from enum import IntEnum
from rich.console import Console
from rich.traceback import install


class LogLevel(IntEnum):
    LOG = 0
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    TRACE = 999


COLOR_SCHEME = {
    LogLevel.LOG: "white",
    LogLevel.DEBUG: "bold cyan",
    LogLevel.INFO: "blue",
    LogLevel.WARNING: "bold light_goldenrod3",
    LogLevel.ERROR: "bold red on red",
    LogLevel.TRACE: "bold blue",
}

LOG_LEVEL = LogLevel.INFO

DEBUG = False
LOG_LEVEL = LogLevel.INFO


class ConsoleMessages:
    __previous_message_at = 0

    def __init__(self, minimum_level=LogLevel.ERROR, time_format="%y-%m-%d %H:%M"):
        self.console = Console()
        self.time_format = time_format

    def timestamp(self, force_timestamp=False):
        current_time = datetime.datetime.now()
        current_minute = current_time.minute
        timestring = current_time.strftime(self.time_format)
        if current_minute == self.__previous_message_at and not force_timestamp:
            self.__previous_message_at = current_minute
            return " " * len(timestring)
        else:
            self.__previous_message_at = current_minute
            return current_time.strftime(self.time_format)

    def print(self, message, level=LogLevel.LOG, force_timestamp=False):
        if level >= LOG_LEVEL:
            self.console.print(
                self.timestamp(force_timestamp), message, style=COLOR_SCHEME[level]
            )

    def log(self, message):
        self.print(message, level=LogLevel.LOG)

    def debug(self, message):
        self.print(message, level=LogLevel.DEBUG)

    def info(self, message):
        self.print(message, level=LogLevel.INFO)

    def warning(self, message):
        self.print(message, level=LogLevel.WARNING)

    def error(self, message):
        self.print(message, level=LogLevel.ERROR, force_timestamp=True)

    def trace(self, message):
        self.print(message, level=LogLevel.TRACE, force_timestamp=True)


console = ConsoleMessages()
install(show_locals=True)

if ("-d" in sys.argv) or ("--debug" in sys.argv) or DEBUG:
    DEBUG = True
    LOG_LEVEL = LogLevel.DEBUG
    console.debug("Debug mode enabled")

DEBUG_FILL_STYLE = "background-color: rgba(255, 0, 255, 0.2);"
DEBUG_STYLESHEET = """
    QWidget {
        background-color: rgba(255, 0, 255, 0.2);
        border: 1px solid rgba(0, 0, 0, 0.5);
    }
    QLabel {
        background-color: rgba(0,0,0, 0.25);
        border: 1px solid rgba(255,255,255,0.2);
    }
"""


__all__ = [
    "console",
    "DEBUG",
    "LOG_LEVEL",
    "DEBUG_FILL_STYLE",
    "DEBUG_STYLESHEET",
]

if __name__ == "__main__":
    console = ConsoleMessages()
    LOG_LEVEL = LogLevel.DEBUG
    console.log("Log: Hello World!")
    console.debug("Debug: Hello World!")
    console.info("Info: Hello World!")
    console.warning("Warning: Hello World!")
    console.error("Error: Hello World!")
    console.trace("Trace: Hello World!")
    console.debug("Debug: Another Debug!")
