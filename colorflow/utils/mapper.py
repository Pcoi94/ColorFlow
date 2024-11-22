from typing import Dict, Union, Optional, Callable

from ..core.color import Color
from ..core.sequence import ColorSequence

def MapCharsToColors(
    char_colors: Dict[str, Union[Color, ColorSequence]], 
    default_color: Optional[Union[Color, ColorSequence]] = None
) -> Callable[[str], str]:
    normalized_colors = {}
    
    for char, colorizer in char_colors.items():
        if not isinstance(colorizer, (Color, ColorSequence)):
            continue
            
        if char.isalpha():
            normalized_colors[char.lower()] = colorizer
            normalized_colors[char.upper()] = colorizer
        else:
            normalized_colors[char] = colorizer

    def color_text(text: str) -> str:
        if not text:
            return text
            
        result = []
        for i, char in enumerate(text):
            colorizer = normalized_colors.get(char, default_color)
            
            if colorizer is None:
                result.append(char)
                continue
                
            if isinstance(colorizer, ColorSequence):
                color = colorizer.at(0 if len(text) == 1 else colorizer._get_position_factor(i, 0, len(text) - 1, 0))
                result.append(color(char))
            else:
                result.append(colorizer(char))
                
        return ''.join(result)
    
    return color_text