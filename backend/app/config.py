import json
from enum import Enum
import os

module_dir = os.path.dirname(__file__)
FILE_PATH = os.path.join(module_dir, "product_names.json")

with open(FILE_PATH, 'r') as file:
    PRODUCTS = json.load(file)["PRODUCTS"]


class Shapes(Enum):
    VERTICAL_RECTANGLE = "Vertical Rectangle"
    HORIZONTAL_RECTANGLE = "Horizontal Rectangle"
    SQUARE = "Square"
    POLYGON = "Polygon"


class ColumnParams(Enum):
    LEFT = "Left"
    RIGHT = "Right"
    AROUND_MIDDLE = "Around middle"


class RowParams(Enum):
    TOP = "Top"
    BOTTOM = "Bottom"
    MIDDLE = "Middle"
