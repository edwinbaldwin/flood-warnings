
 # importing modules
import helper
import random
import pathlib
import json


# setup
root = pathlib.Path(__file__).parent.parent.resolve()
with open( root / "latest.json", 'r') as filehandle:
    data = json.load(filehandle)
    helper.pprint(data)

# processing
if __name__ == "__main__":
    output = ""
    readme = root / "README.md"
    readme_contents = readme.open().read()
    final_output = helper.replace_chunk(readme_contents,"summary_marker",f"{output}")
    readme.open("w").write(final_output)