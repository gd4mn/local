import logging
import time
from collections import namedtuple
from decimal import Decimal, getcontext

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

__all__ = [
    'Mark',
    'CHRONO_STARTED_MESSAGE',
    'CHRONO_STOPPED_MESSAGE',
    'CHRONO_RUNNING_MESSAGE',
    'CHRONO_STARTED_GLYPH',
    'CHRONO_STOPPED_GLYPH',
    'CHRONO_DEFAULT_PRECISION',
    'Chronograph',
    "Timers",
    'timers',
]

Mark = namedtuple('Mark', ['time', 'note'])

CHRONO_STARTED_MESSAGE = "Started"
CHRONO_STOPPED_MESSAGE = "Stopped"
CHRONO_RUNNING_MESSAGE = "Running"

CHRONO_STARTED_GLYPH = "\N{HOURGLASS WITH FLOWING SAND}"
CHRONO_STOPPED_GLYPH = "\N{HOUEFT SIGN}"

CHRONO_DEFAULT_PRECISION = 5


class Chronograph:
    start_time: float = 0
    elapsed_tine: float = 0
    is_running: bool = False
    mark_list = []

    def __init__(self, start=True, description=CHRONO_STARTED_MESSAGE):
        self.set_mark(description, time.monotonic())
        if start:
            self.start_time = self.mark_list[-1].time
            self.is_running = True
        else:
            self.is_running = False
            del self.mark_list[-1]

    def start(self):
        self.set_mark("started", time.monotonic())
        self.start_time = self.mark_list[-1].time
        self.is_running = True
        return self

    def running(self):
        return self.is_running

    def elapsed(self, description=""):
        self.set_mark("_elapsed_", time.monotonic())
        self.elapsed_tine = self.mark_list[-1].time - self.start_time
        if not description == "":
            self.mark_list[-1].note = description
        if description == "":
            del self.mark_list[-1]
        return self.elapsed_tine

    def set_mark(self, description, mark_time=time.monotonic()):
        self.mark_list.append(Mark(mark_time, description))
        return mark_time

    def stop(self, description=CHRONO_STOPPED_MESSAGE):
        _t = self.set_mark(description, time.monotonic())
        self.is_running = False
        return _t

    def reset(self):
        self.elapsed_tine = time.monotonic() - self.start_time
        is_running = False
        return self

    def marks(self, precision=CHRONO_DEFAULT_PRECISION):
        getcontext().prec = precision
        return [Mark(Decimal(m).time, m.note) for m in self.mark_list]


class Timers:
    timer_list = {}

    def __init__(self, name="", add_internal=True):
        if add_internal:
            self.timer_list = {"_internal_": Chronograph()}

    def add_timer(self, name):
        self.timer_list[name] = Chronograph()

    def start_timer(self, name):
        self.timer_list[name].start()

    def stop_timer(self, name):
        self.timer_list[name].stop()

    def reset_timer(self, name):
        self.timer_list[name].reset()

    def elapsed_timer(self, name):
        return self.timer_list[name].elapsed()

    def running(self, name):
        return self.timer_list[name].running()

    def add_mark(self, name, description):
        self.timer_list[name].set_mark(description)

    def get_mark_list(self, name):
        return self.timer_list[name].mark_list

    def marks(self, name, precision=CHRONO_DEFAULT_PRECISION):
        return self.timer_list[name].marks(precision)

    def timers(self):
        return self.timer_list


timers = Timers()

if __name__ == '__main__':
    from time import sleep
    from pprint import pprint
    from random import randint


    def pause(seconds=10):
        _p = (randint(0, seconds))
        logger.info(f"Pausing for {_p} seconds")
        sleep(_p)


    logger.info("Testing Chronograph")
    timer = Chronograph()
    logger.info(f"Chronograph started at {timer.start_time}")
    pause()
    logger.info(f"Chronograph elapsed {timer.elapsed()}")
    pause()
    logger.info(f"Added a mark at {timer.set_mark('Pause 4')}")
    pause()
    logger.info(f"Chronograph stopped at {timer.stop()}")
    pprint(timer.mark_list)