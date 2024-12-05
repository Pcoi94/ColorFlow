from setuptools import setup, find_packages

setup(
    name="ColorFlow",
    version="2.0.0",
    
    description="A Python library for creating and applying full-color, linear, and circular gradients to text with easy color management.",
    long_description="A Python library for creating stunning color gradients, including full-color, and applying them to text. It supports both linear and circular gradients with comprehensive color management tools.",
    long_description_content_type="text/markdown",
    
    keywords=["python", "color", "flow", "easy", "cmd", "app", "manage", "text", "colour", "ansi", "terminal"],
    
    packages=find_packages(),
    install_requires=["typing", "dataclasses", "enum"],
    
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)