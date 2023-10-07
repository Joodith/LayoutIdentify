LAYOUT1 = [
    ["G", "M", "N", "B"],
    ["G", "M", "N", "B"],
    ["G", "M", "N", "B"],
    ["G", "M", "N", "B"]
]

LAYOUT2 = [
    ["G", "G", "M", "M"],
    ["G", "G", "M", "M"],
    ["B", "B", "N", "N"],
    ["B", "B", "N", "N"]
]

LAYOUT3 = [
    ["G", "G", "G", "M", "M", "M", "M"],
    ["G", "B", "G", "M", "N", "N", "M"],
    ["G", "G", "G", "M", "N", "N", "M"],
    ["B", "B", "B", "B", "B", "N", "N"]
]

LAYOUT_WITH_UNRECOG_PROD = [
    ["G", "G", "G", "M", "M", "M", "M"],
    ["G", "l", "G", "M", "N", "N", "M"],
    ["G", "G", "G", "M", "N", "N", "M"],
    ["B", "B", "B", "B", "B", "T", "N"]
]

ARRANGE1 = {
    "G": [
        {
            "shape": "Vertical Rectangle",
            "location": "LEFT"
        }
    ],
    "M": [
        {
            "shape": "Vertical Rectangle",
            "location": "LEFT"
        }
    ],
    "N": [
        {
            "shape": "Vertical Rectangle",
            "location": "RIGHT"
        }
    ],
    "B": [
        {
            "shape": "Vertical Rectangle",
            "location": "RIGHT"
        }
    ]
}

ARRANGE2 = {
    "G": [
        {
            "shape": "Square",
            "location": "TOP LEFT"
        }
    ],
    "M": [
        {
            "shape": "Square",
            "location": "TOP RIGHT"
        }
    ],
    "B": [
        {
            "shape": "Square",
            "location": "BOTTOM LEFT"
        }
    ],
    "N": [
        {
            "shape": "Square",
            "location": "BOTTOM RIGHT"
        }
    ]
}
ARRANGE3 = {
    "G": [
        {
            "shape": "Polygon",
            "location": "TOP LEFT"
        }
    ],
    "M": [
        {
            "shape": "Polygon",
            "location": "TOP RIGHT"
        }
    ],
    "B": [
        {
            "shape": "Square",
            "location": "TOP LEFT"
        },
        {
            "shape": "Horizontal Rectangle",
            "location": "BOTTOM "
        }
    ],
    "N": [
        {
            "shape": "Polygon",
            "location": "BOTTOM RIGHT"
        }
    ]
}

ARRANGE_WITH_UNRECOG_PRODUCT = {
    "G": [
        {
            "shape": "Polygon",
            "location": "TOP LEFT"
        }
    ],
    "M": [
        {
            "shape": "Polygon",
            "location": "TOP RIGHT"
        }
    ],
    "l": [
        {
            "error_message": "Product not recognised"
        }
    ],
    "N": [
        {
            "shape": "Square",
            "location": "MIDDLE RIGHT"
        },
        {
            "shape": "Square",
            "location": "BOTTOM RIGHT"
        }
    ],
    "B": [
        {
            "shape": "Horizontal Rectangle",
            "location": "BOTTOM "
        }
    ],
    "T": [
        {
            "error_message": "Product not recognised"
        }
    ]
}

TEST_LAYOUTS = {
    "TC001": {"layout": LAYOUT1, "response": ARRANGE1},
    "TC002": {"layout": LAYOUT2, "response": ARRANGE2},
    "TC003": {"layout": LAYOUT3, "response": ARRANGE3}

}
