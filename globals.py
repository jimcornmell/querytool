#!/usr/bin/env python3
import os
import time
from rich.console import Console,JustifyMethod
from rich import print
from rich.rule import Rule
from rich.table import Table
from rich import box

# Rich
# https://github.com/Textualize/rich
# https://rich.readthedocs.io/en/stable/
# https://www.freecodecamp.org/news/use-the-rich-library-in-python/
# https://rich.readthedocs.io/en/stable/reference.html
# python3 -m rich
# python3 -m rich.live
# python3 -m rich.table
# python3 -m rich.box
# python3 -m rich.progress
# python3 -m rich.spinner

class RichWrapper:
    def __init__(self):
        global _console
        _console = Console(color_system="auto")
        self._last_time = time.time()
        self._linecolour="#999999"
        self._justify="center"
        self._textcolour="bold yellow"
        self._box=box.HEAVY
        self._header_style="bold yellow1"
        self._row_odd="bold white"
        self._row_even="bold #BBBBBB"

    def getConsole(self):
        return _console

    def setjustify(self, justify):
        self._justify=justify

    def settextcolour(self, colour):
        self._textcolour=colour

    def setlinecolour(self, colour):
        self._linecolour=colour

    def outhr(self):
        _console.print(Rule("", style=self._linecolour))

    def outline(self, msg):
        _console.print(Rule("[" + self._textcolour + "]" + msg, style=self._linecolour))

    def outsolidbox(self, msg, border, col):
        table = Table(show_header=False, expand=True, box=box.ROUNDED, style=border)
        table.add_column("", justify=self._justify, style=col)
        table.add_row(msg)
        _console.print(table)

    def outbox(self, msg):
        self.outsolidbox(msg, self._linecolour, self._textcolour)

    def outerror(self, msg):
        self.outsolidbox(msg, "red on red", "black on red")

    def outwarning(self, msg):
        self.outsolidbox(msg, "#ffdd00 on #ffdd00", "black on #ffdd00")

    def outinfo(self, msg):
        self.outsolidbox(msg, "green on green", "black on green")

    def outnote(self, msg):
        self.outsolidbox(msg, "#999999 on #999999", "black on #999999")

    def outnonl(self, *args):
        for msg in args:
            _console.print(msg, end="")

    def outnl(self, *args):
        for msg in args:
            _console.print(msg, end="")

        _console.print()

    def outtable(self, cols, rows):
        table = Table(show_header=True,
                      show_edge=False,
                      expand=False,
                      padding=(0,0),
                      pad_edge=False,
                      box=self._box,
                      header_style=self._header_style,
                      style=self._linecolour,
                      row_styles=[self._row_odd, self._row_even])

        for col in cols:
            table.add_column(col, justify="center")

        for row in rows:
            line=[]

            for col in row:
                line.append(str(col))

            table.add_row(*line)

        _console.print(table)

    def runcmd(self, start_msg, end_msg, command):
       with _console.status(f"[bold green]{start_msg}") as status:
           _console.log(f"Running: [bold yellow]{command}")
           os.system(command)
           total_secs = round(time.time() - self._last_time)
           _console.log(f"[bold yellow]Time taken for {end_msg} = [bold green]{total_secs}s")
           self._last_time = time.time()

