import sys
import os
from fontTools.ttLib import TTFont

ttFont = TTFont(sys.argv[1])


print("Fixing Italic for", os.path.basename(sys.argv[1]))


def get_name(ID):
    for name in ttFont["name"].names:
        if name.nameID == ID:
            return name.toUnicode()
    return None


def set_name(nameID, value):
    print(f"Setting name ID {nameID} to {value}")
    ttFont["name"].setName(value, nameID, 1, 0, 0)
    ttFont["name"].setName(value, nameID, 3, 1, 0x409)


set_name(1, "Zain Italic")
if get_name(16):
    set_name(16, "Zain Italic")
if get_name(17):
    set_name(17, "Regular")
set_name(2, "Regular")
set_name(3, "1BOU:ZainItalic-Regular:2024")
set_name(4, "Zain Italic Regular")
set_name(6, "ZainItalic-Regular")

# Fix italic angle
ttFont["post"].italicAngle = 0


ttFont.save(sys.argv[1])
