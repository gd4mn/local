import datetime
import sys
from enum import IntEnum
from rich.console import Console
from rich.pretty import pprint
from rich.traceback import install


class LogLevel(IntEnum):
    """Log levels for the application.

    Defines the different log levels available for use.
    """
    ALL = 1
    TRACE = 50
    DEBUG = 100
    INFO = 200
    WARNING = 300
    ERROR = 400
    NONE = 900  # nothing allowed, except for LOG
    LOG = 998       # always allowed
    NOTHING = 999      # nothing allowed and we're not kidding


COLOR_SCHEME = {
    LogLevel.TRACE: "blue",
    LogLevel.DEBUG: "cyan",
    LogLevel.INFO: "bold blue",
    LogLevel.WARNING: "bold light_goldenrod3",
    LogLevel.ERROR: "bold red on red",
    LogLevel.LOG: "white",
    LogLevel.NOTHING: "white",
}

DEBUG = False
LOG_LEVEL = LogLevel.ERROR
ELLIPSIS_MARKER = " ... "


class ConsoleMessages:
    """A class for managing console messages with timestamps and log levels.

    Provides methods for printing messages to the console with timestamps,
    log levels, and styles.  Manages timestamps to avoid repetition within
    the same minute unless a timestamp is explicitly forced.
    """
    __previous_message_at = 0

    def __init__(self, minimum_level=LogLevel.ALL, time_format="%y-%m-%d %H:%M"):
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

    def print(self, message, level=LogLevel.NOTHING, scheme=None, force_timestamp=False):

        color_scheme = scheme or COLOR_SCHEME[level]

        if level >= LOG_LEVEL:
            self.console.print(
                self.timestamp(force_timestamp), message, style=color_scheme
            )

    def write(self, message, end="\n"):
        print(message, end=end)

    def blank(self, count=1):
        self.write("\n" * count, end="")

    def log(self, message):
        self.print(f"Log: {message}", level=LogLevel.LOG)

    def debug(self, message):
        self.print(f"Debug: {message}", level=LogLevel.DEBUG)

    def info(self, message):
        self.print(f"Info: {message}", level=LogLevel.INFO)

    def warning(self, message):
        self.print(f"Warning: {message}", level=LogLevel.WARNING)

    def error(self, message):
        self.print(f"ERROR!: {message}",
                   level=LogLevel.ERROR, force_timestamp=True)

    def trace(self, message):
        self.print(f"Trace: {message}",
                   level=LogLevel.TRACE, force_timestamp=True)

    def dump(self, data):
        """Dump data to the console using rich's pretty print.

        Prints a header message and then pretty prints the provided data to the console.
        Inserts a blank line after the output.

        Args:
            data: The data to dump.
        """
        if LOG_LEVEL < LogLevel.NOTHING:
            self.console.print("   Dumping data:   ", style="black on red")
            pprint(data)
            self.blank()


console = ConsoleMessages()
dump = console.dump
install(show_locals=True)

if ("-d" in sys.argv) or ("--debug" in sys.argv) or DEBUG:
    DEBUG = True
    LOG_LEVEL = LogLevel.DEBUG
    console.print("Debug mode enabled", scheme="bold red on red")

if ("-t" in sys.argv) or ("--trace" in sys.argv):
    DEBUG = True
    LOG_LEVEL = LogLevel.TRACE
    console.debug("Trace mode enabled")

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
    "console",
    "dump",
    "DEBUG",
    "LOG_LEVEL",
    "LogLevel",
    "DEBUG_FILL_STYLE",
    "DEBUG_STYLESHEET",
    "ELLIPSIS_MARKER",
]


if __name__ == "__main__":

    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "gaming", "coding"],
    }
    dump(data)

    console = ConsoleMessages()
    LOG_LEVEL = LogLevel.ALL
    console.write("All levels:")
    console.trace("Hello World!")
    console.debug("Hello World!")
    console.info("Hello World!")
    console.warning("Hello World!")
    console.error("Hello World!")
    console.log("Hello World!")
    console.blank()

    LOG_LEVEL = LogLevel.NOTHING
    console.write(
        "You should not see any trace, debug or info messages after this one", end=ELLIPSIS_MARKER)
    console.trace("Trace: Hello World!")
    console.debug("Debug: Hello World!")
    console.info("Info: Hello World!")

    console.write("Done!")
