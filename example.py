from colorflow import Presets, ColorSequence, MapCharsToColors, GradientType

art = """██████╗  ██████╗ ██████╗ ██╗ █████╗ ██╗  ██╗
██╔══██╗██╔════╝██╔═══██╗██║██╔══██╗██║  ██║
██████╔╝██║     ██║   ██║██║╚██████║███████║
██╔═══╝ ██║     ██║   ██║██║ ╚═══██║╚════██║
██║     ╚██████╗╚██████╔╝██║ █████╔╝     ██║
╚═╝      ╚═════╝ ╚═════╝ ╚═╝ ╚════╝      ╚═╝"""

sequence = ColorSequence({
    0: Presets.BrightRed,
    1: Presets.DarkRed
}, start=(0.5, 0), end=(0.5, 1))

map = MapCharsToColors(char_colors={
    "╗": sequence,
    "║": sequence,
    "╝": sequence,
    "╚": sequence,
    "╔": sequence,
    "═": sequence,
}, default_color=Presets.White)

print(map(art) + "\n" + sequence(art))
