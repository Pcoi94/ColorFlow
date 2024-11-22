from dataclasses import dataclass
from typing import Tuple
from ..enum import ColorLayer

@dataclass(slots=True, frozen=True)
class Color:
    r: int
    g: int
    b: int

    def __post_init__(self):
        object.__setattr__(self, 'r', max(0, min(255, self.r)))
        object.__setattr__(self, 'g', max(0, min(255, self.g)))
        object.__setattr__(self, 'b', max(0, min(255, self.b)))

    def __str__(self) -> str:
        return f"RGB({self.r}, {self.g}, {self.b})"

    def to_tuple(self) -> Tuple[int, int, int]:
        return (self.r, self.g, self.b)

    def to_hex(self) -> str:
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    def __call__(self, text: str, layer: ColorLayer = ColorLayer.FOREGROUND) -> str:
        r, g, b = self.r, self.g, self.b
        
        _ANSI_TEMPLATE = {
            ColorLayer.FOREGROUND: f"\033[38;2;{r};{g};{b}m{{}}\033[0m",
            ColorLayer.BACKGROUND: f"\033[48;2;{r};{g};{b}m{{}}\033[0m",
            ColorLayer.BOTH: f"\033[38;2;{r};{g};{b};48;2;{r};{g};{b}m{{}}\033[0m"
        }
        
        try:
            return _ANSI_TEMPLATE[layer].format(text)
        except KeyError:
            raise ValueError("Invalid color application")