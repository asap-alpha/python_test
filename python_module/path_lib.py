import json
from pathlib import Path


# for file in Path(r"D:\Projects\python").iterdir():
#     print(file)


for file in Path("D:/Projects/python").rglob("*.json"):
    print(file)

file_path = Path("D:/Projects/python/extra/data.json")
payload = json.loads(file_path.read_text())

if "asap" in payload.get("from", ""):
    print(payload["dlr"])
    payload["dlr"] = "rejected"
    print(payload)
    #
    file_path.write_text(json.dumps(payload, indent=4))
