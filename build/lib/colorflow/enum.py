from enum import Enum, auto

class GradientType(Enum):
    LINEAR = auto()
    RADIAL = auto()

class ColorLayer(Enum):
    FOREGROUND = auto()
    BACKGROUND = auto()
    BOTH = auto()
