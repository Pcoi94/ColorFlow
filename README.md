# ColorFlow

A Python library for creating stunning color gradients, including full-color, and applying them to text. It supports both linear and circular gradients with comprehensive color management tools.

## Installation

Install ColorFlow using pip:

```bash
pip install colorflow
```

## Color Layers

ColorFlow introduces flexible color layer control, allowing developers to apply colors to text with precision. Developers can choose to color the foreground text, background, or both simultaneously.

```python
from colorflow import Presets, ColorLayer

blue = Presets.Blue

# Foreground coloration (default behavior)
print(blue("Blue Text", layer=ColorLayer.FOREGROUND))

# Background coloration
print(blue("Blue Background", layer=ColorLayer.BACKGROUND))

# Comprehensive color application
print(blue("Blue Everywhere", layer=ColorLayer.BOTH))
```

## Color Creation Methods

The library supports multiple color generation techniques, enabling developers to create colors through various input formats.

```python
from colorflow import FromRGB, FromHTML, FromHSL

# RGB color generation
custom_blue = FromRGB(0, 0, 255)

# HTML hex code parsing
web_red = FromHTML("#FF0000")

# HSL color conversion
pastel_green = FromHSL(120, 0.5, 0.6)

# Maybe i'll had more conversions.
```

## Color Presets

ColorFlow provides a comprehensive collection of predefined colors, simplifying color selection for developers.

```python
from colorflow import Presets

blue = Presets.Blue
red = Presets.Red
green = Presets.Green
```

## Gradient Generation

The library supports both linear and radial color gradients, enabling sophisticated text color transitions.

### Linear Gradient

```python
from colorflow import ColorSequence, Presets, GradientType, ColorLayer

gradient = ColorSequence({
    0: Presets.Blue, 
    1: Presets.Red
}, gradient_type=GradientType.LINEAR)

print(gradient("Smooth color transition", layer=ColorLayer.FOREGROUND))
```

### Radial Gradient

```python
angular_gradient = ColorSequence({
    0: Presets.Blue,
    0.5: Presets.White,
    1: Presets.Red
}, gradient_type=GradientType.RADIAL)

print(angular_gradient("Radial color spread", layer=ColorLayer.FOREGROUND))
```

## Advanced Color Mapping

Developers can create complex color mappings, assigning unique colors to individual characters.

```python
from colorflow import MapCharsToColors, Presets, ColorLayer

mapper = MapCharsToColors({
    'h': Presets.Red,
    'e': Presets.Green,
    'l': Presets.Blue,
    'o': Presets.Purple
}, layer=ColorLayer.BOTH)

print(mapper("hello"))
```

## Random Color Generation

ColorFlow offers random color generation with optional color palette constraints.

```python
from colorflow import RandomColor, Presets

random_color = RandomColor()  # Completely random
specific_colors = RandomColor([Presets.Red, Presets.Green, Presets.Blue])
```

## Coordinate System

Gradient coordinates are normalized between `(0, 0)` and `(1, 1)`:
- `(0, 0)` represents the top-left corner
- `(1, 1)` represents the bottom-right corner
- `(0.5, 0.5)` indicates the center point

## License

Distributed under the MIT License.