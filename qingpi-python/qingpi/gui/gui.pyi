import tkinter as tk
import typing

def make_window_be_resized_only_by_keypress(master: tk.Tk, min_size: tuple[int, int]) -> None: ...
def make_window_transparent(master: tk.Tk) -> None: ...

ALMOST_TRANSPARENT: typing.Final

def create_transparent_filler(master: tk.Tk) -> tk.Toplevel: ...
