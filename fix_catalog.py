import re
from pathlib import Path

INPUT_FILE = "data/shl_product_catalog.json"
OUTPUT_FILE = "data/shl_product_catalog_fixed.json"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Replace newlines that occur inside quoted strings
def fix_json(text):
    result = []
    inside_string = False
    escape = False

    for ch in text:
        if ch == '"' and not escape:
            inside_string = not inside_string

        if inside_string and ch in ("\n", "\r"):
            result.append(" ")
        else:
            result.append(ch)

        escape = (ch == "\\" and not escape)

    return "".join(result)

fixed = fix_json(text)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(fixed)

print("✅ Fixed catalog saved as:")
print(OUTPUT_FILE)