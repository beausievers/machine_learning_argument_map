#!/usr/local/bin/python3

import subprocess
from shutil import copyfile

subprocess.call("argdown web-component machine_learning.argdown ml_viz", shell=True)
subprocess.call("argdown html machine_learning.argdown ml_html", shell=True)
subprocess.call("argdown map machine_learning.argdown ml_map --format svg", shell=True)

print("Copying map SVG...")
copyfile("ml_map/machine_learning.svg", "ml_html/machine_learning.svg")

print("Copying argdown source...")
copyfile("machine_learning.argdown", "ml_html/machine_learning.argdown")

print("Modifying HTML...")

with open("ml_viz/machine_learning.component.html", "r") as f:
    viz = f.read()

with open("ml_html/machine_learning.html", "r") as f:
    html = f.read()

target = "<body>"
insert_at = html.find(target) + len(target)

viz = (
    """
<style>
.argdown {font-size: 1.2em}
.argdown-figure {margin: auto !important;}
</style>
"""
    + viz
)

html = html[:insert_at] + viz + html[insert_at:]

with open("ml_html/index.html", "w") as f:
    f.write(html)
