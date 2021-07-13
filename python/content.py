
 # importing modules
import helper
import random
import pathlib
import json

string_output  = "<table><thead>\n<tr><th>ID</th><th>Location</th><th>River or Sea</th><th>Description</th>\n</tr>\n</thead>\n<tbody>"
root = pathlib.Path(__file__).parent.parent.resolve()
with open( root / "latest.json", 'r') as filehandle:
    items = json.load(filehandle)
    for item in items["items"]:
        v1 = item['fwdCode']
        v2 = item['lat']
        v3 = item['long']
        try:
          v4 = item['riverOrSea']
        except IndexError:
          v4 = "unknown"   
        v5 = item['description']
        string_output += f"\n<tr><td>{v1}</td><td>{v2},{v3}</td><td>{v4}</td><td>{v5}</td></tr>"
string_output += "</tbody></html>"

# processing
if __name__ == "__main__":
    output = ""
    readme = root / "README.md"
    readme_contents = readme.open().read()
    final_output = helper.replace_chunk(readme_contents,"table_marker",f"{string_output}")
    readme.open("w").write(final_output)
