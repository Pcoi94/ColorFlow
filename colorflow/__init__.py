from .core.color import Color
from .core.sequence import ColorSequence

from .enum import GradientType, ColorLayer
from .parser.color_parser import FromRGB, FromHTML, FromHSL, RandomColor

from .utils.mapper import MapCharsToColors
from .utils.color_presets import Presets

__all__ = [
    'Color',
    'ColorSequence',
    
    'GradientType',
    'ColorLayer',
    
    'FromRGB',
    'FromHTML',
    'FromHSL',
    'RandomColor',
    
    'MapCharsToColors',
    'Presets'
]