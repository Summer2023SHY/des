from tempfile import TemporaryDirectory
from collections.abc import Callable

import global_settings
from cli.menus.main_menu import main_menu

"""
This main file runs the DES application on the command line.
"""

# Initialize settings
global_settings.initialize()

# Maintain a stack for the screens shown (this avoids lots of recursion)
screens: list[Callable[..., None]] = [main_menu]
automata = []

# Opens up a temp directory which is used in the application
with TemporaryDirectory() as temp_dir:
    while len(screens) > 0:
        next_screen = screens[-1]
        next_screen(screens, automata, temp_dir)
