import datetime
from enum import IntEnum
from rich.console import Console


class LogLevel(IntEnum):
    LOG = 0
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    TRACE = 999


COLOR_SCHEME = {
    LogLevel.LOG: 'white',
    LogLevel.DEBUG: 'bold cyan',
    LogLevel.INFO: 'bold green',
    LogLevel.WARNING: 'bold light_goldenrod3',
    LogLevel.ERROR: 'bold red on red',
    LogLevel.TRACE: 'blue'
}

LOG_LEVEL = LogLevel.INFO


class ConsoleMessages:
    __previous_message_at = 0

    def __init__(self, minimum_level=LogLevel.ERROR, time_format='%y-%m-%d %H:%M'):
        self.console = Console()
        self.time_format = time_format

    def timestamp(self, force_timestamp=False):
        current_time = datetime.datetime.now()
        current_minute = current_time.minute
        timestring = current_time.strftime(self.time_format)
        if current_minute == self.__previous_message_at and not force_timestamp:
            self.__previous_message_at = current_minute
            return ' ' * len(timestring)
        else:
            self.__previous_message_at = current_minute
            return current_time.strftime(self.time_format)

    def print(self, message, level=LogLevel.LOG, force_timestamp=False):
        if level >= LOG_LEVEL:
            self.console.print(self.timestamp(force_timestamp), message, style=COLOR_SCHEME[level])

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


if __name__ == "__main__":
    console = ConsoleMessages()
    LOG_LEVEL = LogLevel.DEBUG
    console.log('Log: Hello World!')
    console.debug('Debug: Hello World!')
    console.info('Info: Hello World!')
    console.warning('Warning: Hello World!')
    console.error('Error: Hello World!')
    console.trace('Trace: Hello World!')
    console.debug('Debug: Another Debug!')
