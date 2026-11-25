import os
import shutil

os.makedirs("/output", exist_ok=True)

for name in os.listdir("/output"):
    path = os.path.join("/output", name)
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)

LINE = "Monday morning, Friday's to-do list greeted me like an old friend \u2014 the kind that owes me money and never leaves."

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
