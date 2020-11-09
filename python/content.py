
 # importing modules
import helper
import random
import pathlib
import json

string_output  = "| ID | Location | River or Sea | Description |"
string_output += "\n|- - -|- - -|- - -|- - -|- - -|"
root = pathlib.Path(__file__).parent.parent.resolve()
with open( root / "latest.json", 'r') as filehandle:
    items = json.load(filehandle)
    for item in items["items"]:
        v1 = item['fwdCode']
        v2 = item['lat']
        v3 = item['long']
        v4 = item['riverOrSea']
        v5 = item['description']
        string_output += f"\n | {v1} | {v2},{v3} | {v4} | {v5} |"


# processing
if __name__ == "__main__":
    output = ""
    readme = root / "README.md"
    readme_contents = readme.open().read()
    final_output = helper.replace_chunk(readme_contents,"table_marker",f"{string_output}")
    readme.open("w").write(final_output)