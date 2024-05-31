import sys
import os
from fontTools.ttLib import TTFont

ttFont = TTFont(sys.argv[1])

print("Fixing names for", os.path.basename(sys.argv[1]))


def get_name(ID):
    for name in ttFont["name"].names:
        if name.nameID == ID:
            return name.toUnicode()
    return None


def set_name(nameID, value):
    print(f"Setting name ID {nameID} to {value}")
    ttFont["name"].setName(value, nameID, 1, 0, 0)
    ttFont["name"].setName(value, nameID, 3, 1, 0x409)


def delete_name(ID):
    ttFont["name"].names = [name for name in ttFont["name"].names if name.nameID != ID]


# Get family name
familyName = get_name(16) or get_name(1)

# Get style name
styleName = get_name(17) or get_name(2)

print("Family name:", familyName)
print("Style name:", styleName)

# Complete implementation of https://github.com/googlettFonts/gf-docs/tree/main/Spec#supported-styles
map = {
    "upright": {
        100: {
            1: {(1, 0, 0): "Family Name", (3, 1, 0x409): "Family Name Thin"},
            2: {(1, 0, 0): "Thin", (3, 1, 0x409): "Regular"},
            16: "Family Name",
            17: "Thin",
            "fsSelection": 6,
            "macStyle": None,
        },
        200: {
            1: {(1, 0, 0): "Family Name", (3, 1, 0x409): "Family Name ExtraLight"},
            2: {(1, 0, 0): "ExtraLight", (3, 1, 0x409): "Regular"},
            16: "Family Name",
            17: "ExtraLight",
            "fsSelection": 6,
            "macStyle": None,
        },
        300: {
            1: {(1, 0, 0): "Family Name", (3, 1, 0x409): "Family Name Light"},
            2: {(1, 0, 0): "Light", (3, 1, 0x409): "Regular"},
            16: "Family Name",
            17: "Light",
            "fsSelection": 6,
            "macStyle": None,
        },
        400: {
            1: "Family Name",
            2: "Regular",
            16: None,
            17: None,
            "fsSelection": 6,
            "macStyle": None,
        },
        500: {
            1: {(1, 0, 0): "Family Name", (3, 1, 0x409): "Family Name Medium"},
            2: {(1, 0, 0): "Medium", (3, 1, 0x409): "Regular"},
            16: "Family Name",
            17: "Medium",
            "fsSelection": 6,
            "macStyle": None,
        },
        600: {
            1: {(1, 0, 0): "Family Name", (3, 1, 0x409): "Family Name SemiBold"},
            2: {(1, 0, 0): "SemiBold", (3, 1, 0x409): "Regular"},
            16: "Family Name",
            17: "SemiBold",
            "fsSelection": 6,
            "macStyle": None,
        },
        700: {
            1: "Family Name",
            2: "Bold",
            16: None,
            17: None,
            "fsSelection": 5,
            "macStyle": 0,
        },
        800: {
            1: {(1, 0, 0): "Family Name", (3, 1, 0x409): "Family Name ExtraBold"},
            2: {(1, 0, 0): "ExtraBold", (3, 1, 0x409): "Regular"},
            16: "Family Name",
            17: "ExtraBold",
            "fsSelection": 6,
            "macStyle": None,
        },
        900: {
            1: {(1, 0, 0): "Family Name", (3, 1, 0x409): "Family Name Black"},
            2: {(1, 0, 0): "Black", (3, 1, 0x409): "Regular"},
            16: "Family Name",
            17: "Black",
            "fsSelection": 6,
            "macStyle": None,
        },
    },
    "italic": {
        100: {
            1: {(1, 0, 0): "Family Name", (3, 1, 0x409): "Family Name Thin"},
            2: {(1, 0, 0): "Thin Italic", (3, 1, 0x409): "Italic"},
            16: "Family Name",
            17: "Thin Italic",
            "fsSelection": 0,
            "macStyle": 1,
        },
        200: {
            1: {(1, 0, 0): "Family Name", (3, 1, 0x409): "Family Name ExtraLight"},
            2: {(1, 0, 0): "ExtraLight Italic", (3, 1, 0x409): "Italic"},
            16: "Family Name",
            17: "ExtraLight Italic",
            "fsSelection": 0,
            "macStyle": 1,
        },
        300: {
            1: {(1, 0, 0): "Family Name", (3, 1, 0x409): "Family Name Light"},
            2: {(1, 0, 0): "Light Italic", (3, 1, 0x409): "Italic"},
            16: "Family Name",
            17: "Light Italic",
            "fsSelection": 0,
            "macStyle": 1,
        },
        400: {
            1: "Family Name",
            2: "Italic",
            16: None,
            17: None,
            "fsSelection": 0,
            "macStyle": 1,
        },
        500: {
            1: {(1, 0, 0): "Family Name", (3, 1, 0x409): "Family Name Medium"},
            2: {(1, 0, 0): "Medium Italic", (3, 1, 0x409): "Italic"},
            16: "Family Name",
            17: "Medium Italic",
            "fsSelection": 0,
            "macStyle": 1,
        },
        600: {
            1: {(1, 0, 0): "Family Name", (3, 1, 0x409): "Family Name SemiBold"},
            2: {(1, 0, 0): "SemiBold Italic", (3, 1, 0x409): "Italic"},
            16: "Family Name",
            17: "SemiBold Italic",
            "fsSelection": 0,
            "macStyle": 1,
        },
        700: {
            1: "Family Name",
            2: "Bold Italic",
            16: None,
            17: None,
            "fsSelection": [5, 0],
            "macStyle": [0, 1],
        },
        800: {
            1: {(1, 0, 0): "Family Name", (3, 1, 0x409): "Family Name ExtraBold"},
            2: {(1, 0, 0): "ExtraBold Italic", (3, 1, 0x409): "Italic"},
            16: "Family Name",
            17: "ExtraBold Italic",
            "fsSelection": 0,
            "macStyle": 1,
        },
        900: {
            1: {(1, 0, 0): "Family Name", (3, 1, 0x409): "Family Name Black"},
            2: {(1, 0, 0): "Black Italic", (3, 1, 0x409): "Italic"},
            16: "Family Name",
            17: "Black Italic",
            "fsSelection": 0,
            "macStyle": 1,
        },
    },
}

# Is it Roman or Italic?
variant = "italic" if "Italic" in styleName else "upright"
weightClass = ttFont["OS/2"].usWeightClass

# Apply style map
if not weightClass in map[variant]:
    raise Exception(f"Weight class {weightClass} is unsupported by this script.")

# Continue
for key in map[variant][weightClass]:
    # Name records
    if type(key) == int:
        # Set name record
        if type(map[variant][weightClass][key]) == str:
            string = map[variant][weightClass][key].replace("Family Name", familyName)
            set_name(key, string)
        elif type(map[variant][weightClass][key]) == dict:
            for a, b, c in map[variant][weightClass][key]:
                string = map[variant][weightClass][key][(a, b, c)].replace(
                    "Family Name", familyName
                )
                ttFont["name"].setName(string, key, a, b, c)
        # Delete name record
        elif map[variant][weightClass][key] == None:
            delete_name(key)
    # Other
    elif type(key) == str:

        values = map[variant][weightClass][key]

        # Read
        if key == "fsSelection":

            if type(values) != list:
                values = [values]

            # Unset bits
            for value in [0, 5, 6]:
                ttFont["OS/2"].fsSelection &= ~(1 << value)

            # Set bits
            for value in values:
                if value != None:
                    ttFont["OS/2"].fsSelection |= 1 << value

        elif key == "macStyle":

            if type(values) != list:
                values = [values]

            for value in [0, 1]:
                ttFont["head"].macStyle &= ~(1 << value)

            for value in values:
                if value != None:
                    ttFont["head"].macStyle |= 1 << value


# Set head version from name ID 5
versionMajor, versionMinor = get_name(5).split(";")[0].split(" ")[1].split(".")
ttFont["head"].fontRevision = float(versionMajor) + float(versionMinor) / 100

# OS/2.fsSelection bit 7 (USE_TYPO_METRICS)
fsSelection = ttFont["OS/2"].fsSelection
fsSelection |= 1 << 7
ttFont["OS/2"].fsSelection = fsSelection

# Set fsType
ttFont["OS/2"].fsType = 0

# Set matrics
ttFont["OS/2"].usWinAscent = 881
ttFont["OS/2"].usWinDescent = 501

# Set copyright
set_name(
    0,
    "Copyright 2024 The Zain Project Authors (https://github.com/googlefonts/zain)",
)

# Set license
set_name(
    13,
    "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://openfontlicense.org",
)
set_name(
    14,
    "https://openfontlicense.org",
)

# Delete trademark
delete_name(7)

ttFont.save(sys.argv[1])
