
from dataclasses import dataclass
from collections.abc import Callable

@dataclass
class MenuOption():
    def __init__(self, name : str, redirect : Callable):
        self.name = name
        self.redirect = redirect