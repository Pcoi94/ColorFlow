from typing import List, Union, overload
from random import randint, choice

from ..core.color import Color
from ..core.sequence import ColorSequence

@overload
def FromRGB(r: int, g: int, b: int) -> Color: ...

def FromRGB(r: int, g: int, b: int) -> Color:
    return Color(r, g, b)

def FromHTML(hex_code: str) -> Color:
    hex_code = hex_code.lstrip('#')
    hex_code = ''.join(c * 2 for c in hex_code) if len(hex_code) == 3 else hex_code
    return Color(*(int(hex_code[i:i+2], 16) for i in (0, 2, 4)))

def FromHSL(h: float, s: float, l: float) -> Color:
    h = h % 360 / 360
    q = l * (1 + s) if l < 0.5 else l + s - l * s
    p = 2 * l - q
    
    def hue_rgb(t: float) -> float:
        t = t % 1
        if t < 1/6: return p + (q - p) * 6 * t
        if t < 1/2: return q
        if t < 2/3: return p + (q - p) * (2/3 - t) * 6
        return p

    return Color(*(int(hue_rgb(h + i) * 255) for i in (1/3, 0, -1/3)))

@overload
def RandomColor(colors: List[Color] = None) -> Color: ...

@overload
def RandomColor(colors: List[Union[Color, ColorSequence]] = None) -> Union[Color, ColorSequence]: ...

def RandomColor(colors = None):
    if not colors:
        return Color(*(randint(0, 255) for _ in range(3)))
    return choice(colors)